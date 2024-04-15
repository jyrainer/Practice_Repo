## 모듈 위치 참조 순서
1. 현재 디렉터리
2. 쉘 변수 PYTHONPATH의 각 디렉토리를 검색
3. 기본 경로 검색 (Unix의 경우 /usr/local/lib/python/, 윈도우의 경우 c:\python20\lib)

## dir() 내장함수
- 실행 시 모듈에 정의된 모든 모듈, 변수 및 함수의 이름을 return
    ```
     from math import sin
    content = dir()
    print("from math import sin = ") 
    print(content) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'content', 'sin']
    ```

### reload()
- 모듈의 최상위 코드를 재실행.
    ```
    reload(module_name)
    ```

### 숫자형 함수
- from math import *
    ```
    abs(x) : X의 절대값을 반환
    ceil(x) : x보다 작지 않은 최소 정수 (높임), ceil(2.1) = 3
    cmp(x, y) : x <y의 경우는 -1, x == y의 경우는 0, x> y의 경우는 1, Python 2.x에서만 사용 가능
    exp(x) : The exponential of x: ex
    fabs(x) : 실수 x의 절대 값
    floor(x) : x보다 크지 않은 가장 큰 정수 (내림). floor(2.1)=2
    log(x) : x> 0에 대한 x의 자연 로그
    log10(x) : x> 0에 대한 x의 base-10인 대수입니다.
    max(x1, x2,...) : x1,x2… 중 가장 큰 인수
    min(x1, x2,...) : X1,x2… 중 가장 작은 인수
    modf(x) : 두 항목 튜플의 x 부분 및 정수 부분. 두 부분의 부호는 x와 같습니다. 정수 부분은 float 형식으로 반환됩니다.
        >>> modf(1)
        (0.0, 1.0)
        >>> modf(5)
        (0.0, 5.0)
        >>> modf(5.2)
        (0.20000000000000018, 5.0)
    pow(x, y) : x ** y의 값. (=x^y)  x의 y승 예를 들어 pow(2,3)=8
    round(x [,n]) : 소수점에서 n 자릿수로 반올림 한 값. round (0.5)는 1.0이고 round (-0.5)는 -1.0이다
    sqrt(x) : x> 0에 대한 x의 제곱근
    ```

## 내장 문자열 함수
    capitalize() : 문자열의 첫 글자를 대문자로 바꿉니다.
    center(길이, 추가할 문자) : 원래 문자열 앞뒤에 주어진 길이가 되도록 추가할 문자를 채워서 반환합니다.
    count(str, beg= 0,end=len(string)) : 문자열에 시작 인덱스 beg와 종료 인덱스 end 사이에 주어진 문자열 str이 몇 번 발생하는지 계산
    endswith(suffix, beg=0, end=len(string)) : 문자열 또는 부분 문자열 (시작 색인 beg 및 종료 색인 end가 지정된 경우)이 접미어로 끝나는 지 여부를 결정합니다. 있으면 true를 반환하고 그렇지 않으면 false를 반환합니다.
    expandtabs(tabsize=8) :  문자열의 탭을 여러 공백으로 확장합니다. 탭 크기가 제공되지 않으면 탭 당 8 공백이 기본값입니다.
    find(str, beg=0 end=len(string)) : 문자열의 beg에서 end까지 부분 문자열이 발생하는지 확인합니다. 발견되면 색인을 반환하고 그렇지 않으면 -1을 반환합니다.
    index(str, beg=0, end=len(string)) : find ()와 동일하지만, str이 발견되지 않으면 예외 에러가 발생합니다.
    isalnum() : 문자열이 1 문자 이상이고 모든 문자가 영숫자의 경우는 true, 그렇지 않은 경우는 false를 돌려줍니다.
    isalpha() : 문자열이 1 문자 이상이고 모든 문자가 영문자의 경우는 true, 그렇지 않은 경우는 false를 돌려줍니다.
    isdigit() : 문자열에 숫자 만 포함되어 있으면 true를 반환하고 그렇지 않으면 false를 반환합니다.
    islower() : 문자열이 1 문자 이상이고 모든 문자가 소문자인 경우는 true, 그렇지 않은 경우는 false를 리턴.
    isnumeric() : 유니코드 문자열에 숫자만 포함되어 있으면 true를 반환하고 그렇지 않으면 false를 반환.
    isspace() : 문자열에 공백 문자가 있으면 true를 그렇지 않으면 false를 리턴.
    istitle() : 첫문자는 대문자 나머지는 소문자인 "titlecased"가 올바르게 지정되어 있는 경우는 true, 그렇지 않은 경우는 false
    isupper() : 문자열이 1 문자 이상이고 모든 문자가 대문자인 경우는 true, 그렇지 않은 경우는 false를 리턴.
    join(seq) : 문자열 seq에 있는 문자열을 분리 문자열로 연결
    len(string) : 문자열의 길이
    ljust(width[, fillchar]) : 원래 문자열 왼쪽에 총 width 열 공백으로 채워진 문자열을 반환.
    lower() : 모든 대문자를 소문자로 변환
    lstrip() : 문자열의 모든 선행 공백을 제거
    maketrans() : translate 함수에서 사용할 변환 테이블을 반환
    max(str) : 문자열 str에서 최대 알파벳 문자를 반환
    min(str) : 문자열 str에서 최소 알파벳 문자를 반환
    replace(old, new [, max]) : 문자열에서 모든 old 항목을 new 로 변경.
    rfind(str, beg=0,end=len(string)) : find ()와 동일하지만 문자열 뒤에서 검색
    rindex( str, beg=0, end=len(string)) : index ()와 같지만 문자열 뒤에서 검색
    rjust(width,[, fillchar]) : 원래 문자열 오른쪽에 총 width 열 공백으로 채워진 문자열을 반환.
    rstrip() : 문자열의 모든 공백을 제거
    split(str="", num=string.count(str)) : 구분 기호 str (제공되지 않은 경우 공백)에 따라 문자열을 분할하고 하위 문자열 목록을 반환
    splitlines( num=string.count('\n')) : 문자열을 모두 (또는 num) NEWLINE에서 분할하고 NEWLINE이 제거 된 각 줄의 목록을 반환
    startswith(str, beg=0,end=len(string)) : 문자열이 부분문자열 str로 시작하는지 판단. 있으면 true를 반환하고 그렇지 않으면 false를 반환
    strip([chars]) : 문자열에 대해 lstrip () 및 rstrip ()을 수행
    swapcase() : 문자열의 모든 대소문자를 스왑
    title() : 문자열의 "titlecased"버전을 반환. 즉, 모든 단어는 대문자로 시작하고 나머지는 소문자로 변환됩니다.
    translate(table, deletechars="") : 문자열을 변환 테이블 str(256 문자)에 따라 변환하고 deletechars의 문자를 제거.
    upper() : 문자열의 소문자를 대문자로 변환
    zfill (width) : 총 width 문자에 0으로 왼쪽 패딩 된 원래 문자열을 반환
    isdecimal() : 유니코드 문자열에 decimal 문자 만 들어 있으면 true를 그렇지 않으면 false를 반