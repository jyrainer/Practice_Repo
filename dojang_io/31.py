def fib(n):
    if n == 0:
        return 0
    if 1 <= n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


n = int(input())
print(fib(n))



"""
n   답
0   0
1   1
2   1
---------
3   1+1
4   1+ (1+1)
5   (1+1) + (1 + (1+1))
6   (1+ (1+1)) + ((1+1) + (1 + (1+1))
"""