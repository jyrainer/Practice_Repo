"""
1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.


[예제 풀이]

N이 5일 경우,

1 – 2 + 3 – 4 + 5 = 3

N이 6일 경우,

1 – 2 + 3 – 4 + 5 – 6 = -3


[제약사항]

N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스에는 N이 주어진다.


[출력]

각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 누적된 값을 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

"""짝수는 -, 홀수는 +"""
def even_number(num: int) -> bool:
    return num % 2 == 0


def cal_problem(target_num: int) -> int:
    result_num = 0
    while target_num != 0:
        result_num = result_num - target_num if even_number(target_num) else result_num + target_num
        target_num -= 1
    return result_num

T = int(input())
for test_case in range(1, T + 1):
    target_number = int(input())
    print(f"#{test_case} {cal_problem(target_number)}")