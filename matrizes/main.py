M = int(input("Quantas linhas vai ter a matriz? "))
N = int(input("Quantas colunas vai ter a matriz? "))

mat: list[list[int]] = [[0 for _ in range(N)] for _ in range(M)]

for i in range(0, M):
    for j in range(0, N):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print ("Matriz digitada: ")

for i in range(0, M):
    for j in range(0, N):
        print(f"{mat[i][j]} ", end="")
    print()

## =================================== OU ========================================== ##

M = int(input("Quantas linhas vai ter a matriz? "))
N = int(input("Quantas colunas vai ter a matriz? "))

mat = []

for i in range(M):

    linha = []

    for j in range(N):
        valor = int(input(f"Elemento [{i},{j}]: "))
        linha.append(valor)

    mat.append(linha)

print("\nMatriz digitada:")

for linha in mat:
    for valor in linha:
        print(valor, end=" ")
    print()