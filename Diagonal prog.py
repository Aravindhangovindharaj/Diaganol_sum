X1 = int(input())
X2 = int(input())
matrix = []
for i in range(X1):
    row = []
    for j in range(X2):
        element = int(input())
        row.append(element)
    matrix.append(row)
diagonal_sum = 0
for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]
print(diagonal_sum)
