def hadamard(n, matrix):
    if n == 1:
        return "Hadamard"
    if (n & (n - 1)) != 0:
        return "Imposible"
    for i in range(n):
        for j in range(i+1, n):
            count = 0
            for k in range(n):
                count += (matrix[i][k] != matrix[j][k])
            if count != n // 2:
                return "No Hadamard"
    return "Hadamard"

def main():
    matriz = []
    n = int(input().strip())
    boleanos = input().split(" ")
    count = 0
    for i in range(n):
        mat = []
        for j in range(n):
            mat.append(boleanos[count])
            count+=1
        matriz.append(mat)
    print(hadamard(n, matriz))
main()