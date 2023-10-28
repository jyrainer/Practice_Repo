# import math
# import collections
 
# Point2D = collections.namedtuple('Point2D', ['x', 'y'])    # namedtuple로 점 표현
 
# p1 = Point2D(x=30, y=20)    # 점1
# p2 = Point2D(x=60, y=50)    # 점2
 
# a = p1.x - p2.x    # 선 a의 길이
# b = p1.y - p2.y    # 선 b의 길이
 
# c = math.sqrt((a * a) + (b * b))
# print(c)    # 42.42640687119285

"""
표준 입력으로 x, y 좌표 4개가 입력되어 Point2D 클래스의 인스턴스 리스트에 저장됩니다.
여기서 점 4개는 첫 번째 점부터 마지막 점까지 순서대로 이어져 있습니다.
다음 소스 코드를 완성하여 첫 번째 점부터 마지막 점까지 연결된 선의 길이가 출력되게 만드세요.

judge_line_length.py
"""
import math
 
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
 
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

##
def p2p(point_1_x, point_1_y, point_2_x, point_2_y) :
    return (abs(point_1_x - point_2_x)**2 + abs(point_1_y - point_2_y)**2)**(1/2)

length = p2p(p[0].x, p[0].y, p[1].x, p[1].y) + p2p(p[1].x, p[1].y, p[2].x, p[2].y) + p2p(p[2].x, p[2].y, p[3].x, p[3].y)
##


print(length)

# 예
# 입력
# 10 10 20 20 30 30 40 40
# 결과
# 42.42640687119285