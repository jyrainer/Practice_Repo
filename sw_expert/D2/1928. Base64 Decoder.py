"""
다음과 같이 Encoding 을 한다.

1. 우선 24비트 버퍼에 위쪽(MSB)부터 한 byte씩 3 byte의 문자를 집어넣는다.

2. 버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고, 각각의 값을 아래 [표-1] 의 문자로 Encoding 한다.

입력으로 Base64 Encoding 된 String 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성하시오.
"""
Base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def char2int(char: str) -> int:
    return Base64_table.find(char)

def int2char(inter: int) -> str:
    return list(Base64_table)[inter]

def int2byte(inter: int) -> str:
    """6비트까지만 가능
    Example:
        "000011"
    """
    max_coef = 5
    result_str = ""
    for _ in range(6):
        if inter >= 2**max_coef:
            result_str += "1"
            inter -= 2**max_coef
        else:
            result_str += "0"
        max_coef -= 1
    return result_str

def byte2int(byte: str) -> int:
    coef = 7
    result = 0
    for each_bit in byte:
        if int(each_bit) == 1:
            result += 2**coef
        coef -= 1
    return result

T = int(input())

for test_case in range(1, T + 1):
    encoded_context = str(input())
    result_str = ""
    for index in range(len(encoded_context) // 4):
        encoded_4char = encoded_context[index*4: index*4+4]
        buffer_24bit = ""
        for each_char in encoded_4char:
            index_char = char2int(each_char)
            byte_6 = int2byte(index_char)
            buffer_24bit += byte_6
        buffer_3byte = [buffer_24bit[0:8], buffer_24bit[8:16], buffer_24bit[16:24]]
        buffer_3byte_to_int = [chr(byte2int(x)) for x in buffer_3byte]
        for decoded_char in buffer_3byte_to_int:
            result_str += decoded_char
    print(f"#{test_case} {result_str}")