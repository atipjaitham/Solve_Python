m, n = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(m)]
matrix2 = [list(map(int, input().split())) for _ in range(m)]

result = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(matrix1[i][j]+matrix2[i][j])
    result.append(row)

for row in result:
    print(' '.join(map(str, row)))
