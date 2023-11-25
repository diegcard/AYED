from sys import stdin

def mergeSort(A):
    if len(A) <= 1:
        return (A[:],0)
    mid = len(A)//2
    left_a, cont_1 = mergeSort(A[:mid])
    right_a, cont_2 = mergeSort(A[mid:])
    merged, cont_merged = merge(left_a, right_a)
    return (merged, cont_1+cont_2+cont_merged)

def merge(sq, sq2):
    i, j, result = 0, 0, []
    cont = 0
    while i < len(sq) and j < len(sq2):
        if sq[i] < sq2[j]:
            result.append(sq[i])
            i+=1
        else:
            result.append(sq2[j])
            cont+= len(sq) - i
            j+=1
    if i < len(sq):
        result += sq[i:]
    else:
        result += sq2[j:]
    return result, cont


def main():
    lista = [1,2,3,4,5,7,6,8,9]
    rest = mergeSort(lista)
    print(f"Cantidad de cambios: {rest[1]}")

main()