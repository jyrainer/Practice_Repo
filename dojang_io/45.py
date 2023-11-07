#표준 입력으로 정수가 입력됩니다. 
# 주어진 calcpkg 패키지를 활용하여 입력된 정수의 제곱근과
# 입력된 정수를 반지름으로 하는 원의 넓이가 출력되게 만드세요.
# 제곱근은 calcpkg 패키지에서 operation 모듈의 squareroot 함수를 사용하고,
# 원의 넓이는 calcpkg 패키지에서 geometry 모듈의 circle_area 함수를 사용하세요
# (calcpkg 패키지를 사용하지 않고 계산하면 결과가 맞더라도 틀린 것으로 처리됩니다.
# 반드시 calcpkg 패키지를 사용하세요).

# calcpkg/__init__.py
# # 내용이 비어 있음
# calcpkg/operation.py
# import math
 
# def squareroot(n):
#     return math.sqrt(n)
# calcpkg/geometry.py
# import math
 
# def circle_area(radius):
#     return radius * radius * math.pi
# judge_package.py

##
from calcpkg.operation import squareroot
from calcpkg.geometry import circle_area

n = float(input())

print(squareroot(n))
print(circle_area(n))

##
# 표준 입력
# 2
# 표준 출력
# 1.4142135623730951
# 12.566370614359172