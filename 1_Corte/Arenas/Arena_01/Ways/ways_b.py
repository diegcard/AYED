from sys import stdin

def chan(numero):
    denominaciones = [1, 5, 10, 25, 50]
    ways = [0 for i in range(numero+1)]
    ways[0] = 1
    for moneda in denominaciones:
        for i in range(moneda,numero+1):
            ways[i] += ways[i-moneda]
    return ways[numero]

def main():
    numero = int(stdin.readline().strip())
    numero = int(numero)
    while numero:
        numero = int(numero)
        change = chan(numero)
        if change == 1:
            print("There is only {} way to produce {} cents change.".format(change,numero))
        else: print("There are {} ways to produce {} cents change.".format(change, numero))
        numero = stdin.readline().strip()
main()
