from functools import reduce

def cube(y):
    return y * y * y;

g = lambda x: x * x * x
print(g(7)) # 343

print(cube(7)) # 343

# Python code to illustrate filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0), li))
print(final_list) #[5, 7, 97, 77, 23, 73, 61]

# map() with lambda()  to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list) #[10, 14, 44, 194, 108, 124, 154, 46, 146, 122]

# reduce() with lambda() to get sum of a list

li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum) # 193

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product) # 24