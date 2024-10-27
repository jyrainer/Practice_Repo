"""
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.

주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

[예제]

N = 5, K = 3 이고, 퍼즐의 모양이 아래 그림과 같이 주어졌을 때
 



길이가 3 인 단어가 들어갈 수 있는 자리는 2 곳(가로 1번, 가로 4번)이 된다.
 


[제약 사항]

1. N은 5 이상 15 이하의 정수이다. (5 ≤ N ≤ 15)

2. K는 2 이상 N 이하의 정수이다. (2 ≤ K ≤ N)


[입력]

입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.

다음 줄부터 각 테스트 케이스가 주어진다.

테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.

테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.

퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.


[출력]

테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""
def find_index(
    array: list,
)-> list:
    """(row,col) 좌표에서 시작하는 왼쪽 혹은 아래쪽으로 갈 수 있는지에 대한 좌표를 구합니다"""
    result = []
    for row in range(1, len(array)):
        for col in range(1, len(array)):
            if array[row][col] == 0:  # 자신이 검은 색이면 넘김
                pass
            elif (array[row][col - 1] == 0) | (array[row -1][col] == 0):  # 왼쪽이나 위쪽이 막혀있다면(0)
                result.append((row,col))
    return result
            
def get_padding(
    array: list,
    padding_size: int,
    padding_info: int = 0
) -> list:
    """검은색(0)으로 패딩을 씌워줍시다"""
    len_new_space = len(array) + padding_size*2
    start_row, start_col = padding_size, padding_size
    
    new_space = [[padding_info]*(len_new_space) for x in range(len_new_space)]
    
    for row in range(len(array)):
        for col in range(len(array)):
            new_space[start_row][start_col+col] = array[row][col]
        start_row += 1
    
    return new_space

def find_num(array:list, locate:list, len_word:int):
    """len_word짜리 단어가 몇개 들어갈까"""
    num = 0
    for avail_locate in locate:
        row, col = avail_locate
        now_row = array[row]
        now_col = [array[i][col] for i in range(len(array))]
        num += 1 if ((sum(now_row[col: col + len_word]) == len_word) and (now_row[col + len_word] == 0) and (now_row[col-1] == 0)) else 0 # 가로의 경우
        num += 1 if ((sum(now_col[row: row + len_word]) == len_word) and (now_col[row + len_word] == 0) and (now_col[row-1] == 0)) else 0 # 세로의 경우
    return num
    
T = int(input())
for test_case in range(1, T + 1):
    len_space, len_word = list(map(int , input().split()))
    space = []
    for _ in range(len_space):
        space.append(list(map(int, input().split())))
    
    new_space = get_padding(space, padding_size = 1)
    
    locate = find_index(new_space)
    result = find_num(new_space, locate, len_word)

    print(f"#{test_case} {result}")