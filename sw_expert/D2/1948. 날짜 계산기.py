"""
월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.


[제약 사항]

월은 1 이상 12 이하의 정수이다. 각 달의 마지막 날짜는 다음과 같다.

1/31, 2/28, 3/31, 4/30, 5/31, 6/30, 7/31, 8/31, 9/30, 10/31, 11/30, 12/31

두 번째 날짜가 첫 번째 날짜보다 항상 크게 주어진다.


[입력]

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.

첫 번째 수가 월을 나타내고 두 번째 수가 일을 나타낸다. 그 다음 같은 형식으로 두 번째 날짜가 주어진다.


[출력]

출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
"""

T = int(input())
total_day_each_month = [0, 31,28,31,30,31,30,31,31,30,31,30,31]  # 인덱스 접근 편하게 1월->31

for test_case in range(1, T + 1):
    start_month, start_day, end_month, end_day = list(map(int, input().split()))
    d_day = 0
    
    if start_month == end_month:  #  시작월, 끝월 같으면 바로 d-day 값
        d_day = end_day - start_day + 1
    else:
        for now_month in range(end_month,start_month-1,-1):  #  마지막월부터 하나씩 내려옴
            if start_month == now_month:  # 같은 월(마지막케이스)일 때, 해당달 마지막-첫째날
                d_day += total_day_each_month[now_month] - start_day + 1
                break
            elif now_month == end_month:  # 지금 처리하는 달이 마지막 달인데 앞에 남은경우 end_day만큼 추가
                d_day += end_day
            else:  # 지금 처리하는 달이 start_month가 아닌경우는 처리하는 달의 날만큼 추가
                d_day += total_day_each_month[now_month]
    print(f"#{test_case} {d_day}")
    """
    다른방법
    for t in range(1,T+1):
        m1, d1, m2, d2= map(int,input().split())
        total_days1 = sum(days[:m1]) + d1
        total_days2 = sum(days[:m2]) + d2

        days_diff = total_days2 - total_days1 +1

        print(f"#{t} {days_diff}")
    """