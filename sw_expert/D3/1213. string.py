"""
주어지는 영어 문장에서 특정한 문자열의 개수를 반환하는 프로그램을 작성하여라.

Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition.

위 문장에서 ti 를 검색하면, 답은 4이다.
"""

try:
    while True:
        test_case = int(input())
        input_str = input()
        context_str = input()
        len_input_str = len(input_str)
        len_context_str = len(context_str)
 
        result_count = 0
 
        for index, chara in enumerate(context_str):
            if len_context_str - index < len_input_str:
                break
            elif context_str[index: index+len_input_str] == input_str:
                result_count += 1
        print(f"#{test_case} {result_count}")
except:
    pass