# 모듈: 특정 기능을 .py 파일 단위로 작성한 것입니다.
# 패키지: 특정 기능과 관련된 여러 모듈을 묶은 것입니다. 패키지는 모듈에 네임스페이스(namespace, 이름공간)를 제공합니다.
# 파이썬 표준 라이브러리: 파이썬에 기본으로 설치된 모듈과 패키지, 내장 함수를 묶어서 파이썬 표준 라이브러리(Python Standard Library, PSL)라 부릅니다.

#표준 입력으로 원의 반지름(실수)이 입력됩니다. 
# 입력된 반지름을 이용하여 원의 넓이를 출력하는 프로그램을 만드세요.
# (input에서 안내 문자열은 출력하지 않아야 합니다). 원의 넓이는 반지름 * 반지름 * 원주율로 구합니다.

#judge_import.py
import math as m

p = m.pi

r = float(input())

print(r*r*p)


# 예
# 입력
# 10.0
# 결과
# 314.1592653589793