from sys import stdin
def contar_minas(matrix,fil,col):
    cont_min = 0
    for i in range(fil-1, fil+2):
        for j in range(col-1, col+2):
            if (0 <= i < len(matrix)) and (0 <= j < len(matrix[0])):
                if matrix[i][j] == "*":
                    cont_min += 1
    return str(cont_min)

def traducir(matrix):
    fillen = len(matrix)
    columlen = len(matrix[0])
    matrix_fin = []
    for i in range(fillen):
        minas = []
        for j in range(columlen):
            if matrix[i][j] == "*":
                minas.append("*")
            else:
                minas.append(contar_minas(matrix,i,j))
        matrix_fin.append(minas)
    return matrix_fin

def main():
    dimension = (stdin.readline().strip()).split(" ")
    casos = 0
    fil = int(dimension[0])
    col = int(dimension[1])
    while fil != 0 and col != 0:
        matrix = []
        for i in range(fil):
            texto = (stdin.readline().strip())
            fila = []
            for j in texto:
                fila.append(j)
            matrix.append(fila)
        resulmatrix = traducir(matrix)
        casos += 1
        print("Field #" + str(casos)+":")
        for i in range(len(resulmatrix)):
            for j in range(len(resulmatrix[0])):
                if j != len(resulmatrix[0])-1:
                    print(resulmatrix[i][j], end="")
                else:
                    print(resulmatrix[i][j], end=" ")
            print()
        dimension = (stdin.readline().strip()).split(" ")
        fil = int(dimension[0])
        col = int(dimension[1])
        if fil != "0" and col != "0":
            print(" ")
main()


