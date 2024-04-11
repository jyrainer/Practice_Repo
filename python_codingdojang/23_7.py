# 입력
row, col = map(int,input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))

# 정수화    
for j in range(col):
    for k in range(row):
        if matrix[j][k] == '.':
            matrix[j][k] = 0
        elif matrix[j][k] == '*':
            matrix[j][k] = 1

# 패딩
pad_matrix = []
for l in range(col+2):
    temp_matrix =[]
    for m in range(row+2):
        temp_matrix.append(0)
    pad_matrix.append(temp_matrix)

# 대입
for j in range(col):
    for k in range(row):
        if matrix[k][j] == 1:
            for a in range(-1,2):
                for b in range(-1,2):
                    pad_matrix[k+b+1][j+a+1] += 1
# 디코딩
for j in range(col):
    for k in range(row):
        if matrix[k][j] == 1:
            pad_matrix[k+1][j+1] = '*'

# 출력            
for j in range(col):
    for k in range(row):
        print(pad_matrix[j+1][k+1],end='')
    print()