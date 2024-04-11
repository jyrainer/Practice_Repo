# # # 데코레이터
# # def trace(func):                             # 호출할 함수를 매개변수로 받음
# #     def wrapper():
# #         print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
# #         func()                               # 매개변수로 받은 함수를 호출
# #         print(func.__name__, '함수 끝')
# #     return wrapper                           # wrapper 함수 반환
 
# # @trace    # @데코레이터
# # def hello():
# #     print('hello')
 
# # @trace    # @데코레이터
# # def world():
# #     print('world')
 
# # hello()    # 함수를 그대로 호출
# # world()    # 함수를 그대로 호출

# # decorator_parameter.py
# def is_multiple(x):              # 데코레이터가 사용할 매개변수를 지정
#     def real_decorator(func):    # 호출할 함수를 매개변수로 받음
#         def wrapper(a, b):       # 호출할 함수의 매개변수와 똑같이 지정
#             r = func(a, b)       # func를 호출하고 반환값을 변수에 저장
#             if r % x == 0:       # func의 반환값이 x의 배수인지 확인
#                 print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
#             else:
#                 print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
#             return r             # func의 반환값을 반환
#         return wrapper           # wrapper 함수 반환
#     return real_decorator        # real_decorator 함수 반환
 
# @is_multiple(3)     # @데코레이터(인수)
# def add(a, b):
#     return a + b
 
# print(add(10, 20))
# print(add(2, 5))
# # 실행 결과
# # add의 반환값은 3의 배수입니다.
# # 30
# # add의 반환값은 3의 배수가 아닙니다.
# # 7

# 표준 입력으로 HTML 태그 이름 두 개가 입력됩니다.
# 다음 소스 코드에서 함수의 반환값을 HTML 태그로 감싸는 데코레이터를 만드세요.
# HTML 태그는 웹 페이지에 사용하는 문법이며 <span>문자열</span>,
# <p>문자열</p>처럼 <태그이름>으로 시작하며 </태그이름>으로 끝납니다.

#judge_decorator.py
###
def html_tag(char):
    def real_deco(func):
        def wrapper():
            return f"<{char}>{func()}</{char}>"
        return wrapper
    return real_deco
###
a, b = input().split()
 
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())
# 예
# 입력
# p span
# 결과
# <p><span>Hello, world!</span></p>
# 입력
# b i
# 결과
# <b><i>Hello, world!</i></b>