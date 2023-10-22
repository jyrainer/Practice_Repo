input_1, input_2 = map(int,input().split())

a = {1,input_1}
b = {1,input_2}


# def find_low(large_num, divid_num):
#     divid_count = 0
#     while large_num >= 2:
#         if (large_num % divid_num) == 0 :
#             large_num //= divid_num
#             divid_count += 1
#         else :
#             return large_num, divid_count
#     return large_num, divid_count

# def find_low_set(input, a):
#     for i in range(2,input):
#         k, d = find_low(input,i)     # k 는 나눠떨어진 값. 100을 2로나누면. 50->25. 25만 남음
#         if input == k:            # 안나눠 떨어진 경우임
#             continue
#         if input != k :           # 나누어지긴 함
#             for c in range(1,d+1):
#                 a |= {i**c}            
#             input = k
#             pass
#         if k <= i :                 # 만약 k가 나눌  i보다 더 작아버리면
#             return a
        
# def find_all_low_set(a):
#     results = set()
#     for i in a:
#         temp_set = set()
#         for result in results:
#             product = i * result
#             if product <= 100:
#                 temp_set.add(product)
#         temp_set.add(i)
#         results.update(temp_set)
#     return results

# a = find_all_low_set(find_low_set(input_1, a))
# b = find_all_low_set(find_low_set(input_2, b))

def find_low_set(num, set_function):
    for i in range(2,num) :
        if num % i == 0:
            set_function |= {i}
        else:
            continue
    return set_function



a = find_low_set(input_1, a)
b = find_low_set(input_2, b)

print(a,b)
divisor = a & b
 
result = 0
if type(divisor) == set:
    result = sum(divisor)
 
print(result)