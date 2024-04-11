# x = lambda x: x+5

# print(x(5))

files = input().split()
 
print(list(map(lambda x: x.zfill(4+len(x.split('.')[1])),files)))