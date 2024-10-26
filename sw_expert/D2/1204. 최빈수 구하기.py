"""
어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계 자료를 만들려고 한다.

이때, 이 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데, 여기서 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미한다.

다음과 같은 수 분포가 있으면,

10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

최빈수는 8이 된다.

최빈수를 출력하는 프로그램을 작성하여라 (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
"""

T = int(input())
for test_case in range(1, T + 1):
    _ = int(input())
    score_list = list(map(int, input().split()))
    score_list.sort(reverse=True)
    board_list = []
    before_num = 101
    iter_num = 0
    for score in score_list:
        if iter_num > 500:  # 500회 이상 반복시 바로  return
            max_num = score
            break
        elif score == before_num:  #  반복시
            iter_num += 1
            continue
        elif score != before_num:
            board_list.append((iter_num, before_num))  # 기록갱신
            before_num = score
            iter_num = 1
            continue
    max_iter = 0
    for index, board in enumerate(board_list):
        if board[0] > max_iter:
            max_num = board[1]
            max_iter = board[0]
    print(f"#{test_case} {max_num}")