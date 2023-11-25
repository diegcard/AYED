from sys import stdin
def bubble_sort(lista):
    count = 0
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                count = count + 1
    return count

def main():
    for i in range(int(stdin.readline().strip())):
        train = stdin.readline().strip()
        valores = list(map(int,stdin.readline().strip().split()))
        print("Optimal train swapping takes {} swaps.".format(bubble_sort(valores)))

main()

