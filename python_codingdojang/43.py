# # 정규표현식
# import re

# # 정규표현식은 특정 문자열이 맨 앞에 오는지 맨 뒤에 오는지 판단할 수 있습니다.

# # 문자열 앞에 ^를 붙이면 문자열이 맨 앞에 오는지 판단하고,
# # 문자열 뒤에 $를 붙이면 문자열이 맨 뒤에 오는지 판단합니다(특정 문자열로 끝나는지).

# # ^문자열
# # 문자열$
# # 단, 이때는 match 대신 search 함수를 사용해야 합니다.
# # match 함수는 문자열 처음부터 매칭되는지 판단하지만, search는 문자열 일부분이 매칭되는지 판단합니다.

# # 예) re.search('패턴', '문자열')

# >>> re.search('^Hello', 'Hello, world!')     # Hello로 시작하므로 패턴에 매칭됨
# <_sre.SRE_Match object; span=(0, 5), match='Hello'>
# >>> re.search('world!$', 'Hello, world!')    # world!로 끝나므로 패턴에 매칭됨
# <_sre.SRE_Match object; span=(7, 13), match='world!'>

# hello|world'는 문자열에서 'hello' 또는 'world'가 포함되는지 판단합니다.

# >>> re.match('hello|world', 'hello')    # hello 또는 world가 있으므로 패턴에 매칭됨
# <_sre.SRE_Match object; span=(0, 5), match='hello'>

# >>> re.match('[0-9]*', '1234')    # 1234는 0부터 9까지 숫자가.. 0개 이상 있으므로 패턴에 매칭됨
# <_sre.SRE_Match object; span=(0, 4), match='1234'>
# >>> re.match('[0-9]+', '1234')    # 1234는 0부터 9까지 숫자가.. 1개 이상 있으므로 패턴에 매칭됨
# <_sre.SRE_Match object; span=(0, 4), match='1234'>
# >>> re.match('[0-9]+', 'abcd')    # abcd는 0부터 9까지 숫자가.. 1개 이상 없으므로 패턴에 매칭되지 않음

# >>> re.match('abc?d', 'abd')         # abd에서 c 위치에 c가 0개 있으므로 패턴에 매칭됨
# <_sre.SRE_Match object; span=(0, 3), match='abd'>
# >>> re.match('ab[0-9]?c', 'ab3c')    # [0-9] 위치에 숫자가 1개 있으므로 패턴에 매칭됨
# <_sre.SRE_Match object; span=(0, 4), match='ab3c'>
# >>> re.match('ab.d', 'abxd')         # .이 있는 위치에 문자가 1개 있으므로 패턴에 매칭됨
# <_sre.SRE_Match object; span=(0, 4), match='abxd'>

"""
\d: [0-9]와 같음. 모든 숫자
\D: [^0-9]와 같음. 숫자를 제외한 모든 문자
\w: [a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄 문자
\W: [^a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄 문자를 제외한 모든 문자
>>> re.match('\d+', '1234')          # 모든 숫자이므로 패턴에 매칭됨
<_sre.SRE_Match object; span=(0, 4), match='1234'>
>>> re.match('\D+', 'Hello')         # 숫자를 제외한 모든 문자이므로 패턴에 매칭됨
<_sre.SRE_Match object; span=(0, 5), match='Hello'>
>>> re.match('\w+', 'Hello_1234')    # 영문 대소문자, 숫자, 밑줄 문자이므로 패턴에 매칭됨
<_sre.SRE_Match object; span=(0, 10), match='Hello_1234'>
>>> re.match('\W+', '(:)')    # 영문 대소문자, 숫자, 밑줄문자를 제외한 모든 문자이므로 패턴에 매칭됨
<_sre.SRE_Match object; span=(0, 3), match='(:)'>
"""

# >>> re.match('[a-zA-Z0-9 ]+', 'Hello 1234')     # ' '로 공백 표현
# <_sre.SRE_Match object; span=(0, 10), match='Hello 1234'>
# >>> re.match('[a-zA-Z0-9\s]+', 'Hello 1234')    # \s로 공백 표현
# <_sre.SRE_Match object; span=(0, 10), match='Hello 1234'>

# practice_regular_expression.py
# import re
 
# p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
# emails = ['python@mail.example.com', 'python+kr@example.com',              # 올바른 형식
#           'python-dojang@example.co.kr', 'python_10@example.info',         # 올바른 형식
#           'python.dojang@e-xample.com',                                    # 올바른 형식
#           '@example.com', 'python@example', 'python@example-com']          # 잘못된 형식
 
# for email in emails:
#     print(p.match(email) != None, end=' ')
# 실행 결과
# True True True True True False False False
# 정답

''
# 표준 입력으로 URL 문자열이 입력 입력됩니다. 
# 입력된 URL이 올바르면 True, 잘못되었으면 False를 출력하는 프로그램을 만드세요. 
# 이 심사문제에서 판단해야 할 URL의 규칙은 다음과 같습니다.

# http:// 또는 https://로 시작
# 도메인은 도메인.최상위도메인 형식이며 영문 대소문자, 숫자, -로 되어 있어야 함
# 도메인 이하 경로는 /로 구분하고, 영문 대소문자, 숫자, -, _, ., ?, =을 사용함
import re

input_url = input()

#p = re.compile('^(http://|https://)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/[a-zA-Z0-9-_.?=]+$')
p = re.compile('^(https?://)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*')
print(p.match(input_url) != None)
# 입력
# http://www.example.com/hello/world.do?key=python
# 결과
# True
# 입력
# https://example/hello/world.html
# 결과
# False