"""
퀴즈 대회에 참가해서 우승을 하게 되면 보너스 상금을 획득할 수 있는 기회를 부여받는다.

우승자는 주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.

예를 들어, 다음 그림과 3, 2, 8, 8, 8 의 5개의 숫자판들이 주어지고 교환 횟수는 2회라고 하자.

교환전>



처음에는 첫번째 숫자판의 3과 네 번째 숫자판의 8을 교환해서 8, 2, 8, 3, 8이 되었다.
 


다음으로, 두 번째 숫자판 2와 마지막에 있는 8을 교환해서 8, 8, 8, 3, 2이 되었다.



정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.

숫자판의 오른쪽 끝에서부터 1원이고 왼쪽으로 한자리씩 갈수록 10의 배수만큼 커진다.

위의 예에서와 같이 최종적으로 숫자판들이 8,8,8,3,2의 순서가 되면 88832원의 보너스 상금을 획득한다.

여기서 주의할 것은 반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.

다음과 같은 경우 1회의 교환 횟수가 주어졌을 때 반드시 1회 교환을 수행하므로 결과값은 49가 된다.



94의 경우 2회 교환하게 되면 원래의 94가 된다.

정해진 횟수만큼 숫자판을 교환했을 때 받을 수 있는 가장 큰 금액을 계산해보자.

[입력]

가장 첫 줄은 전체 테스트 케이스의 수이다.

최대 10개의 테스트 케이스가 표준 입력을 통하여 주어진다.

각 테스트 케이스에는 숫자판의 정보와 교환 횟수가 주어진다.

숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 최대 교환 횟수는 10번이다.

[출력]

각 테스트 케이스마다, 첫 줄에는 “#C”를 출력해야 하는데 C는 케이스 번호이다.

같은 줄에 빈 칸을 하나 사이에 두고 교환 후 받을 수 있는 가장 큰 금액을 출력한다.
"""

from collections import deque
import copy

def number2list(number:int)->list:
    """235 -> [2,3,5]"""
    return [int(x) for x in str(number)]

def list2number(number_list:list)->int:
    """[2,3,5] -> 235"""
    result = ""
    for i in range(len(number_list)):
        result += str(number_list[i])
    return int(result)
    # return int("".join(map(str, number_list)))

def make_avail_pair(number:int) -> list:
    number_list = number2list(number)
    
    avail_list = []
    for i in range(len(number_list)-1):
        for j in range(i+1,len(number_list)):
            print(i,j)
            number_list = number2list(number)
            temp = number_list[i]
            number_list[i] = number_list[j]
            number_list[j] = temp
            avail_list.append(list2number(number_list))
            
    return avail_list
            
def find_max_prize(start_number: int, num_exchange:int) -> int:
    # init
    number_list = number2list(start_number)
    len_number_list = len(number_list)
    
    # queue 정의
    queue = deque([(number_list, num_exchange)])
    visited = set()
    visited.add((start_number, num_exchange))
    
    max_value = 0
    
    while queue:
        current_list, remaining_exchanges = queue.pop()
        current_value = list2number(current_list)
        
        # 교환 다 쓸 경우 최대 값 갱신
        if remaining_exchanges == 0:
            max_value = max(max_value, current_value)
            continue
            
        # 가능한 모든 위치 숫자 쌍을 교환
        for i in range(len_number_list-1):
            for j in range(i+1, len_number_list):
                # 교환
                new_list = current_list[:]
                new_list[i], new_list[j] = new_list[j], new_list[i]
                new_value = list2number(new_list)
                
                # 방문 여부 체크
                if (new_value, remaining_exchanges - 1) not in visited:
                    visited.add((new_value, remaining_exchanges - 1))
                    queue.append((new_list, remaining_exchanges - 1))
    return max_value
            
    

T = int(input())

for test_case in range(1, T + 1):
    start_number, num_exchange = list(map(int, input().split()))
    result = find_max_prize(start_number, num_exchange)
    print(f"#{test_case} {result}")