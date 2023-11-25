from sys import stdin
def sumacol(lista,n,n1):
    """
    esta funcion recibe una lista 2D junto a 2 int el primero hace referencia al numero de filas\
    y el segundo al numero de columnas y suma los valores de las columnas para esto se inicia\
    separando cada fila y luego se intera fila por fila con cada uno de los valores de la respectiva columna
    (list 2D, int, int) -> list, int)
    
    """
    suma = 0
    suma_columnas = [0] * n1
    for fila in lista:
        for i in range(n1):
            suma_columnas[i] += fila[i]
    for i in suma_columnas:
        suma += i
    return suma_columnas,suma

def main():  
    matriz = []
    m,n = list(map(int, stdin.readline().strip().split(",")))
    for _ in range(int((n[0]))):
        matriz.append(list(map(int,stdin.readline().strip().split(","))))
    resultado = sumacol((matriz), m, n)
    vector = ",".join(str(i) for i in resultado[0])
    print("vector:", vector)
    print("suma:",resultado[1])
main() 