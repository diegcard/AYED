from sys import stdin

def func(monedas,matrix):
    for i in range(1,len(monedas)):
        for j in range(monedas[i],30000+1):
            matrix[j] += matrix[j-monedas[i]]
    return matrix

def main():
    monedas = [1, 5, 10, 25, 50]
    matrix = [1 for i in range(30000+1)]
    forma = func(monedas, matrix)
    cambio = stdin.readline().strip()
    while cambio != "":
        total_caminos = forma[int(cambio)]
        if total_caminos == 1:
            print("There is only", total_caminos, "way to produce", cambio, "cents change.")
        else:
            print("There are", total_caminos, "ways to produce", cambio, "cents change.")
        cambio = stdin.readline().strip()
main()