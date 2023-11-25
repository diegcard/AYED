from sys import stdin
import math
def cupido(alturasP, altura):
    mid = len(alturasP) // 2
    if len(alturasP) == 0:
        return -math.inf
    if alturasP[mid] >= altura:
        return cupido(alturasP[:mid], altura)
    return max(alturasP[mid], cupido(alturasP[mid + 1:], altura))

def main():
    cant = stdin.readline().strip()
    alturasP = list(map(int,stdin.readline().strip().split(" ")))
    consult = int(stdin.readline().strip())
    alturas = stdin.readline().strip().split()
    for c in range(consult):
        rest = cupido(alturasP, int(alturas[c]))
        if  rest == -math.inf:
            print("X")
        else:
            print(rest)

main()
