"""
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.

다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.


[예제]

N이 3일 경우,
 



N이 4일 경우,
 


[제약사항]

달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

T = int(input())

def print_square(array: list):
    if len(array) == 1:
        print("1")
    else:
        for row in range(len(array)):
            row_str = str(array[row][0])
            for col in range(len(array)):
                if col != 0:
                    row_str += str(" "+ str(array[row][col]))
            print(row_str)

for test_case in range(1, T + 1):
    len_square = int(input())
    square = [[0] * len_square for _ in range(len_square)]
    
    rule_square = [] # 규칙 발견
    for index in range(len_square,0,-1):
        rule_square.extend([index, index-1]) if index -1 != 0 else rule_square.extend([index])
    
    now_row = 0  # 현재 행
    now_col = 0  # 현재 열
    
    last_row = len_square - 1
    last_col = len_square - 1
    
    forward_row = True
    forward_col = True
    
    now_num = 1

    for index, rule in enumerate(rule_square):  #1행, 마지막열, 마지막행, 1열, 2행... 이순으로 감
        if index % 2 == 0:  # 짝수는 행을 처리함
            if forward_row:
                for number in range(rule):
                    square[now_row][now_col] = now_num
                    now_col += 1
                    now_num += 1
                forward_row = not(forward_row)
                now_col -= 1
                now_row += 1
            else:
                for number in range(rule):
                    square[now_row][now_col] = now_num
                    now_col -= 1
                    now_num += 1
                forward_row = not(forward_row)
                now_col += 1
                now_row -= 1
            
        elif index % 2 == 1:  # 홀수는 열을 처리함
            if forward_col:
                for number in range(rule):
                    square[now_row][now_col] = now_num
                    now_row += 1
                    now_num += 1
                forward_col = not(forward_col)
                now_row -= 1
                now_col -= 1
            else:
                for number in range(rule):
                    square[now_row][now_col] = now_num
                    now_row -= 1
                    now_num += 1
                forward_col = not(forward_col)
                now_row += 1
                now_col += 1
    print(f"#{test_case}")
    print_square(square)