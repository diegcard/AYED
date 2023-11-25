def main():
    while True:
        w, h, n = [int(x) for x in input().strip().split()]
        if w == 0 and h == 0 and n == 0:
            break
        campos = [[0 for j in range(h + 1)] for i in range(w + 1)]

        for i in range(n):
            x1, y1, x2, y2 = [int(x) for x in input().strip().split()]
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    campos[x][y] = 1
        vacio = 0
        for i in range(1, w + 1):
            for j in range(1, h + 1):
                if campos[i][j] == 0:
                    vacio += 1
        if vacio == 0:
            print("No hay lugares vacíos.")
        elif vacio == 1:
            print("Hay un lugar vacío.")
        else:
            print("Hay", vacio, "plazas vacías.")
main()