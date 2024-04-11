# # # 코루틴

# # #coroutine_consumer.py
# # def number_coroutine():
# #     while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
# #         x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
# #         print(x)
 
# # co = number_coroutine()
# # next(co)      # 코루틴 안의 yield까지 코드 실행(최초 실행)
 
# # co.send(1)    # 코루틴에 숫자 1을 보냄
# # co.send(2)    # 코루틴에 숫자 2을 보냄
# # co.send(3)    # 코루틴에 숫자 3을 보냄


# def find(word):
#     result = False
#     while True:
#         line = (yield result)
#         result = word in line
        
# f = find('Python')
# next(f)
 
# print(f.send('Hello, Python!'))
# print(f.send('Hello, world!'))
# print(f.send('Python Script'))
 
# f.close()

# 표준 입력으로 사칙연산 계산식이 여러 개 입력됩니다.
# 다음 소스 코드에서 각 계산식의 결과를 구하는 코루틴을 만드세요.
# 계산식은 문자열 형태이며 값과 연산자는 공백으로 구분됩니다.
# 그리고 값은 정수로 변환하여 사용하고, 나눗셈은 / 연산자를 사용하세요.

#judge_coroutine.py
###


def calc():
    result = 0
    while True:
        expressions = (yield result)
        num_1, cal, num_2 = expressions.split()
        num_1, num_2 = int(num_1), int(num_2)
        if cal == '+':
            result = num_1 + num_2
        elif cal == '-':
            result = num_1 - num_2
        elif cal == '*':
            result = num_1 * num_2
        elif cal == '/':
            result = num_1 / num_2

###
expressions = input().split(', ')
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()
# 예
# 입력
# 1 + 2, 4 - 9
# 결과
# 3
# -5
# 입력
# 3 * 4, 10 / 5, 20 + 39
# 결과
# 12
# 2.0
# 59