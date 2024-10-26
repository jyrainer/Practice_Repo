"""
숫자 N은 아래와 같다.

N=2a x 3b x 5c x 7d x 11e

N이 주어질 때 a, b, c, d, e 를 출력하라.
"""

T = int(input())
target_list = [2,3,5,7,11]


for test_case in range(1, T + 1):
    abcde_list = []
    N = int(input())
    while N != 1:
        for target_num in target_list:
            iter_num = 0
            while N % target_num == 0:
                N /= target_num
                iter_num += 1
            abcde_list.append(iter_num)
            
    print(f"#{test_case} {abcde_list[0]} {abcde_list[1]} {abcde_list[2]} {abcde_list[3]} {abcde_list[4]}")