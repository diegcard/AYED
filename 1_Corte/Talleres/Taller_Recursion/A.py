from sys import stdin
import random
def ordenar(arr=[]):
    print(arr)
    if len(arr) <= 1:
        return arr
    mn = min(arr)
    arr.remove(mn)
    return [mn] + ordenar(arr)

def main():
    lista = [9,8,7,6,5,4,3,2,1]
    print(ordenar(lista))
main()
