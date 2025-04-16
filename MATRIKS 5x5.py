A = [
    [2, 4, 6, 8, 10],
    [1, 3, 5, 7, 9],
    [9, 7, 5, 3, 1],
    [10, 20, 30, 40, 50],
    [5, 10, 15, 20, 25]
]

B = [
    [1, 0, 2, 1, 3],
    [2, 1, 0, 2, 1],
    [3, 2, 1, 0, 2],
    [4, 3, 2, 1, 0],
    [5, 4, 3, 2, 1]
]

hasil = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        for k in range(5):
            hasil[i][j] += A[i][k] * B[k][j]

for row in hasil:
    print(row)
