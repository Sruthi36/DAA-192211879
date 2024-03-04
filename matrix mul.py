A = [[1,2,3],[4,5,6]]
B = [[1,2,6],[4,5,7],[7,8,9]]
C = [[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
for l in C:
    print(l)
