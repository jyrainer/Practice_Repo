# def generator():
#     x = [1, 2, 3]
#     yield from x
    
    
# for i in generator():
#     print(i)

# 40.5 연습문제: 파일 읽기 제너레이터 만들기
# 다음 소스 코드에서 words.txt 파일을 한 줄씩 읽은 뒤 내용을 함수 바깥에 전달하는 제너레이터를 작성하세요.
# 파일의 내용을 출력할 때 파일에서 읽은 \n은 출력되지 않아야 합니다(단어 사이에 줄바꿈이 두 번 일어나면 안 됨).

# words.txt
# compatibility
# experience
# photography
# spotlight
# practice_generator.py
# def file_read():
#     with open('dojang_io/file/words.txt') as file:
#         word_list = file.readlines()
#         for index, words in enumerate(word_list):
#             word_list[index] = words.strip('\n')
#         yield from word_list
                                   
 
# for i in file_read():
#     print(i)
# 실행 결과
# compatibility
# experience
# photography
# spotlight



#표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 10~1000,
# 두 번째 입력 값의 범위는 100~1000이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 
# 다음 소스 코드에서 첫 번째 정수부터 두 번째 정수 사이의 소수(prime number)를 생성하는 제너레이터를 만드세요.
# 소수는 1과 자기자신만으로 나누어 떨어지는 1보다 큰 양의 정수입니다.

#judge_generator.py

###
def prime_number_generator(start, stop):
    current = start
    num_list = []
    for num in range(start, stop+1):
        if prime_dist(current):
            num_list.append(current)
        current += 1
    yield from num_list
            
def prime_dist(num):
    for i in range(2, num):
        if num % i != 0:
            continue
        else :
            return
    return num
    
###
start, stop = map(int, input().split())
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')
# 예
# # 입력
# # 50 100
# # 결과
# # <class 'generator'>
# # 53 59 61 67 71 73 79 83 89 97 
# # 입력
# # 950 1000
# # 결과
# # <class 'generator'>
# # 953 967 971 977 983 991 997 