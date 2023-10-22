x, y = map(int, input().split())

def calc(num_1, num_2) :
    return num_1+num_2, num_1-num_2, num_1*num_2, num_1/num_2




a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))