A = [
    [1, 2],
    [3, 4],
]

k = 2

for linha in range(len(A)):
    for coluna in range(len(A[linha])):
        # A[linha][coluna] = A[linha][coluna] * k
        A[linha][coluna] *= k
    print(A[linha])

# for linha in A:
#     print(linha)
