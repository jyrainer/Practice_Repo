from func import * 
from torchvision.io import read_image, ImageReadMode
import torch
import tensorrt as trt

class TRTInference:
    def __init__(self, engine_path):
        self.logger = trt.Logger(trt.Logger.ERROR)
        with open(engine_path, "rb") as f, trt.Runtime(self.logger) as runtime:
            self.engine = runtime.deserialize_cuda_engine(f.read())
        self.context = self.engine.create_execution_context()

        # I/O 메타데이터
        self.io_tensor_num = self.engine.num_io_tensors
        self.tensor_names  = [self.engine.get_tensor_name(i) for i in range(self.io_tensor_num)]
        self.inp_names     = [n for n in self.tensor_names if self.engine.get_tensor_mode(n) == trt.TensorIOMode.INPUT]
        self.out_names     = [n for n in self.tensor_names if self.engine.get_tensor_mode(n) == trt.TensorIOMode.OUTPUT]
        assert len(self.inp_names) == 1, "This example assumes a single input."

        # I/O dtype
        self.trt_input_dtypes   = [self.engine.get_tensor_dtype(n) for n in self.inp_names]
        self.torch_input_dtypes = [trt_to_torch_dtype(dt) for dt in self.trt_input_dtypes]
        self.trt_output_dtypes   = [self.engine.get_tensor_dtype(n) for n in self.out_names]
        self.torch_output_dtypes = [trt_to_torch_dtype(dt) for dt in self.trt_output_dtypes]

    def _resolve_neg1(self, shape, batch):
        # TensorRT가 -1(동적)을 줄 경우 배치로 치환
        return tuple(batch if int(d) == -1 else int(d) for d in shape)

    def infer(self, image: torch.Tensor):
        # 1) 전처리 (B,3,H,W) float on CUDA
        x = preprocess_image(image)  # (B,3,336,336), float32, cuda, contiguous
        # 2) 엔진 입력 dtype에 맞춰 캐스팅/연속화
        want_dtype = self.torch_input_dtypes[0]
        if x.dtype != want_dtype:
            x = x.to(want_dtype)
        if not x.is_contiguous():
            x = x.contiguous()

        # 3) 입력 shape 설정
        input_name = self.inp_names[0]
        self.context.set_input_shape(input_name, tuple(x.shape))

        # 4) 출력 텐서들 shape 계산 & 할당 (각 출력별 개별 shape)
        out_tensors = {}
        B = x.shape[0]
        for name, dt in zip(self.out_names, self.torch_output_dtypes):
            dims = self.context.get_tensor_shape(name)  # tensorrt.Dims
            out_shape = self._resolve_neg1(dims, batch=B)
            out_tensors[name] = torch.empty(out_shape, dtype=dt, device="cuda")

        # 5) 바인딩 주소 등록
        bindings = [0] * self.io_tensor_num
        bindings[self.tensor_names.index(input_name)] = int(x.data_ptr())
        for name in self.out_names:
            bindings[self.tensor_names.index(name)] = int(out_tensors[name].data_ptr())

        for i in range(self.io_tensor_num):
            name = self.tensor_names[i]
            self.context.set_tensor_address(name, bindings[i])

        # 6) 실행
        ok = run_v3(self.context)
        if not ok:
            raise RuntimeError("TensorRT inference failed.")

        # 7) 반환
        if len(self.out_names) == 1:
            return out_tensors[self.out_names[0]]
        return out_tensors

if __name__ == "__main__":
    import cv2 
    import torch
    from PIL import Image
    import core.vision_encoder.pe as pe
    import core.vision_encoder.transforms as transforms
    from pia.ai.tasks.T2VRet.base import T2VRetConfig
    from pia.model import PiaTorchModel, PiaONNXTensorRTModel
    print("CLIP configs:", pe.CLIP.available_configs())
    # CLIP configs: ['PE-Core-G14-448', 'PE-Core-L14-336', 'PE-Core-B16-224']
    # engine_path = "trt_export/vision_x64.engine"
    engine_path = "/home/yangro/codes/Product-AI-mono/assets/model//PE-Core-L14-336_vision_dynamic.engine"
    
    # image_path = "/home/yangro/codes/Product-AI-mono/0.jpg"
    image_path = "assets/dog.jpg"
    # image_path = "assets/cat.jpg"
    model_config = T2VRetConfig(
            model_path="/home/yangro/codes/Product-AI-mono/assets/model/PE-Core-L14-336.pt",  
            # model_path="/home/yangro/.cache/huggingface/hub/models--facebook--PE-Core-L14-336/snapshots/bafb0f76541d399057e980a25947f67acec76575/PE-Core-L14-336.pt",  
            device="cuda",
            tile_config=None,
            model_name="PE-Core-L14-336",
            temporal_size=1,
            img_size=[None, None],
        )
    pia_torch_model = PiaTorchModel(
            target_task="RET",
            target_model="PerceptionEncoder",
            config=model_config,
        )
    model = pe.CLIP.from_config("PE-Core-L14-336", pretrained=True)  # Downloads from HF
    model = model.cuda()

    preprocess = transforms.get_image_transform(model.image_size)
    tokenizer = transforms.get_text_tokenizer(model.context_length)

    image = preprocess(Image.open(image_path)).unsqueeze(0).cuda()
    text = tokenizer(["a diagram", "a dog", "a cat"]).cuda()
    cv_image = cv2.imread(image_path)
    cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)[None, ::]
    pia_torch_ret = pia_torch_model(cv_image)
    pia_torch_ret = pia_torch_ret / pia_torch_ret.norm(dim=-1, keepdim=True)  # Normalize
    with torch.no_grad(), torch.autocast("cuda"):
        image_features, text_features, logit_scale = model(image, text)
        text_probs = (logit_scale * image_features @ text_features.T).softmax(dim=-1)



    image = read_image(image_path, mode=ImageReadMode.RGB)  # (C,H,W), uint8, CPU
    trt_infer = TRTInference(engine_path)
    trt_ret = trt_infer.infer(image)

    diff = trt_ret - image_features 
    pia_clip_diff = image_features - pia_torch_ret
    print(f"pia vs clip MAE:{pia_clip_diff.abs().mean().item():.6f}")
    print(f"pia vs clip MSE:{pia_clip_diff.pow(2).mean().item():.6f}")

    print(f"TRT vs clip MAE:{diff.abs().mean().item():.6f}")
    print(f"TRT vs clip MSE:{diff.pow(2).mean().item():.6f}")

    print(f"pia vs clip similarity:{(pia_torch_ret @ image_features.T).item():.4f}")
    print(f"TRT vs clip similarity:{(trt_ret @ image_features.T).item():.4f}")
    print(f"TRT vs pia similarity:{(trt_ret @ pia_torch_ret.T).item():.4f}")

    if isinstance(trt_ret, dict):
        print({k: v.shape for k, v in trt_ret.items()})
    else:
        print("TRT Inference Result:", trt_ret.shape)
        print(trt_ret)
 