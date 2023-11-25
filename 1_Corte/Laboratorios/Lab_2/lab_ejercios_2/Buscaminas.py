from sys import stdin

def obtener_vecinos(matriz, i, j):
    filas = len(matriz)
    columnas = len(matriz[0])
    count = 0
    vecinos = []
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x >= 0 and x < filas and y >= 0 and y < columnas and (x != i or y != j):
                vecinos.append(matriz[x][y])
    for l in range(len(vecinos)):
        if vecinos[l] == "*":
            count+=1
    return count

def transformar_matriz(matriz):
    len_fila = len(matriz)
    len_colum = len(matriz[0])
    for i in range(0,len_fila):
        for j in range(0,len_colum):
            if matriz[i][j] == ".":
                matriz[i][j] = obtener_vecinos(matriz,i,j)
    return matriz

def main():
    filas_columnas = stdin.readline().strip().split(" ")
    count = 1
    while int(filas_columnas[0]) != 0 and int(filas_columnas[1]) != 0:
        if count > 1: print()
        matriz = []
        for i in range(int(filas_columnas[0])):
            columns: list[str] = [] #Verify
            row = stdin.readline().strip()
            for j in row:
                columns.append(j)
            matriz.append(columns)
        mat = transformar_matriz(matriz)
        print("Field #"+ str(count) + ":")
        for ma in mat:
            fila = "".join(str(elemen) for elemen in ma)
            print(fila)
        count+=1
        filas_columnas = stdin.readline().strip().split(" ")

if __name__ == '__main__':
    main()
