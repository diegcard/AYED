from random import randint
import math
SEQ = 1
MAX = 90
SIZE = 100

def merge(sq, sq2):
    i, j, result = 0, 0, []
    while i < len(sq) and j < len(sq2):
        if sq[i] <= sq2[j]:
            result.append(sq[i])
            i+=1
        else:
            result.append(sq2[j])
            j+=1
    if i < len(sq):
        result += sq[i:]
    else:
        result += sq2[j:]
    return result

def mergeSort(sq):
    if len(sq) <= 1:
        return sq[:]
    half = len(sq) // 2
    left = mergeSort(sq[:half])
    right = mergeSort(sq[half:])
    return merge(left, right)


def search(lista,n):
    mid = len(lista) //2
    if len(lista) == 0 or (len(lista) == 1 and lista[0] <= n):
        return math.inf
    if lista[mid] <= n:
        return search(lista[mid:],n)
    if lista[mid] > n:
        return min(lista[mid], search(lista[:mid],n))

def main():
    edades = [10,15,20,25,30,35,40,50,60]
    edades = [randint(1, MAX) for i in range(int(SIZE))]
    edades_orde = mergeSort(edades)
    print(edades_orde)
    chica = randint(1,MAX)
    print(chica)
    print(search(edades_orde, chica))
main()