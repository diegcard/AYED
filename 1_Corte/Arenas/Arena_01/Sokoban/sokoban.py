from sys import stdin


def posin(matriz):
    ju_i, ju_j = 0, 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == "w" or matriz[i][j] == "W":
                ju_i = i
                ju_j = j
    return ju_i, ju_j


def down(matriz):
    ju_i, ju_j = posin(matriz)
    if matriz[ju_i+1][ju_j] != "#":
        if matriz[ju_i][ju_j] == "w" and matriz[ju_i + 1][ju_j] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i + 1][ju_j] = "w"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i + 1][ju_j] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i + 1][ju_j] = "W"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i + 1][ju_j] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i + 1][ju_j] = "W"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i + 1][ju_j] == "b" and matriz[ju_i + 2][ju_j] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i + 1][ju_j] = "w"
            matriz[ju_i + 2][ju_j] = "b"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i + 1][ju_j] == "b" and matriz[ju_i + 2][ju_j] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i + 1][ju_j] = "w"
            matriz[ju_i + 2][ju_j] = "B"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i + 1][ju_j] == "B" and matriz[ju_i + 2][ju_j] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i + 1][ju_j] = "W"
            matriz[ju_i + 2][ju_j] = "B"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i + 1][ju_j] == "B" and matriz[ju_i + 2][ju_j] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i + 1][ju_j] = "W"
            matriz[ju_i + 2][ju_j] = "b"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i + 1][ju_j] == "b" and matriz[ju_i + 2][ju_j] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i + 1][ju_j] = "w"
            matriz[ju_i + 2][ju_j] = "B"



        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i+1][ju_j] == "B" and matriz[ju_i+2][ju_j] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i+1][ju_j] = "W"
            matriz[ju_i+2][ju_j] = "B"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i+1][ju_j] == "B" and matriz[ju_i+2][ju_j] == ".":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i+1][ju_j] = "W"
            matriz[ju_i+2][ju_j] = "b"
    return matriz


def up(matriz):
    ju_i, ju_j = posin(matriz)
    if matriz[ju_i - 1][ju_j] != "#":
        if matriz[ju_i][ju_j] == "w" and matriz[ju_i - 1][ju_j] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i - 1][ju_j] = "w"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i - 1][ju_j] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i - 1][ju_j] = "W"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i - 1][ju_j] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i - 1][ju_j] = "W"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i - 1][ju_j] == "b" and matriz[ju_i - 2][ju_j] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i - 1][ju_j] = "w"
            matriz[ju_i - 2][ju_j] = "b"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i - 1][ju_j] == "b" and matriz[ju_i - 2][ju_j] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i - 1][ju_j] = "w"
            matriz[ju_i - 2][ju_j] = "B"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i - 1][ju_j] == "B" and matriz[ju_i - 2][ju_j] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i - 1][ju_j] = "W"
            matriz[ju_i - 2][ju_j] = "B"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i - 1][ju_j] == "B" and matriz[ju_i - 2][ju_j] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i - 1][ju_j] = "W"
            matriz[ju_i - 2][ju_j] = "b"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i - 1][ju_j] == "b" and matriz[ju_i - 2][ju_j] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i - 1][ju_j] = "w"
            matriz[ju_i - 2][ju_j] = "B"


        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i-1][ju_j] == "B" and matriz[ju_i-2][ju_j] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i-1][ju_j] = "W"
            matriz[ju_i-2][ju_j] = "B"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i-1][ju_j] == "B" and matriz[ju_i-2][ju_j] == ".":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i-1][ju_j] = "W"
            matriz[ju_i-2][ju_j] = "b"
    return matriz


def left(matriz):
    ju_i, ju_j = posin(matriz)
    if matriz[ju_i][ju_j - 1] != "#":
        if matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j - 1] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j - 1] = "w"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j - 1] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j - 1] = "W"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i][ju_j - 1] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i][ju_j - 1] = "W"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j - 1] == "b" and matriz[ju_i][ju_j - 2] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j - 1] = "w"
            matriz[ju_i][ju_j - 2] = "b"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j - 1] == "b" and matriz[ju_i][ju_j - 2] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j - 1] = "w"
            matriz[ju_i][ju_j - 2] = "B"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j - 1] == "B" and matriz[ju_i][ju_j - 2] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j - 1] = "W"
            matriz[ju_i][ju_j - 2] = "B"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j - 1] == "B" and matriz[ju_i][ju_j - 2] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j - 1] = "W"
            matriz[ju_i][ju_j - 2] = "b"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i][ju_j - 1] == "b" and matriz[ju_i][ju_j - 2] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i][ju_j - 1] = "w"
            matriz[ju_i][ju_j - 2] = "B"


        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i][ju_j - 1] == "B" and matriz[ju_i][ju_j - 2] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i][ju_j - 1] = "W"
            matriz[ju_i][ju_j - 2] = "B"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i][ju_j - 1] == "B" and matriz[ju_i][ju_j - 2] == ".":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i][ju_j - 1] = "W"
            matriz[ju_i][ju_j - 2] = "b"
    return matriz


def right(matriz):
    ju_i, ju_j = posin(matriz)
    if matriz[ju_i][ju_j + 1] != "#":
        if matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j + 1] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j + 1] = "w"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j + 1] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j + 1] = "W"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i][ju_j + 1] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i][ju_j + 1] = "W"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j + 1] == "b" and matriz[ju_i][ju_j + 2] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j + 1] = "w"
            matriz[ju_i][ju_j + 2] = "b"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j + 1] == "b" and matriz[ju_i][ju_j + 2] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j + 1] = "w"
            matriz[ju_i][ju_j + 2] = "B"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j + 1] == "B" and matriz[ju_i][ju_j + 2] == "+":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j + 1] = "W"
            matriz[ju_i][ju_j + 2] = "B"

        elif matriz[ju_i][ju_j] == "w" and matriz[ju_i][ju_j + 1] == "B" and matriz[ju_i][ju_j + 2] == ".":
            matriz[ju_i][ju_j] = "."
            matriz[ju_i][ju_j + 1] = "W"
            matriz[ju_i][ju_j + 2] = "b"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i][ju_j + 1] == "b" and matriz[ju_i][ju_j + 2] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i][ju_j + 1] = "w"
            matriz[ju_i][ju_j + 2] = "B"


        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i][ju_j + 1] == "B" and matriz[ju_i][ju_j + 2] == "+":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i][ju_j + 1] = "W"
            matriz[ju_i][ju_j + 2] = "B"

        elif matriz[ju_i][ju_j] == "W" and matriz[ju_i][ju_j + 1] == "B" and matriz[ju_i][ju_j + 2] == ".":
            matriz[ju_i][ju_j] = "+"
            matriz[ju_i][ju_j + 1] = "W"
            matriz[ju_i][ju_j + 2] = "b"
    return matriz


def win(total, total_b):
    if total == total_b:
        return True
    else:
        return False


def contarb_B(matriz, letra):
    count = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == str(letra):
                count += 1
    return count


def instrucciones(matriz, pasos):
    cant_1B = (contarb_B(matriz, "B"))
    cant_1W = (contarb_B(matriz, "W"))
    cant_1mas = (contarb_B(matriz, "+"))
    rest_total = cant_1B + cant_1W + cant_1mas
    for i in range(len(pasos)):
        if win(rest_total, contarb_B(matriz, "B")):
            break
        if pasos[i] == "D":
            matriz = down(matriz)
        elif pasos[i] == "U":
            matriz = up(matriz)
        elif pasos[i] == "L":
            matriz = left(matriz)
        elif pasos[i] == "R":
            matriz = right(matriz)
    return matriz


def main():
    cases = list(map(int, stdin.readline().strip().split()))
    count = 1
    while cases[0] != 0 and cases[1] != 0:
        matriz = []
        for i in range(cases[0]):
            temp = []
            for i in stdin.readline().strip():
                temp.append(i)
            matriz.append(temp)
        pasos = [str(i) for i in stdin.readline().strip()]
        rest = instrucciones(matriz, pasos)
        if win((contarb_B(matriz, "+"))+(contarb_B(matriz, "W"))+(contarb_B(matriz, "B")), contarb_B(rest, "B")):
            print("Game {}: complete".format(count))
        else:
            print("Game {}: incomplete".format(count))
        count += 1
        for fila in rest:
            print("".join(map(str, fila)))
        cases = list(map(int, stdin.readline().strip().split()))

main()
