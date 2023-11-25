from sys import stdin

def main():
    rango = list(map(int, stdin.readline().strip().split()))
    contador = 1
    while rango[0] > 0 and rango[1] > 0:
        print("Game 1")
        matrix = []
        for i in range(int(rango[0])):
            temp = []
            for j in stdin.readline().strip():
                temp.append(j)
            matrix.append(temp)
        instuciones = []
        for i in stdin.readline().strip():
            instuciones.append(i)

        print(instuciones)
        for i in matrix:
            print(*i)
main()
