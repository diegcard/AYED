def merge(sq, sq2):
    i, j, result = 0, 0, []
    cont = 0
    while i < len(sq) and j < len(sq2):
        if sq[i] < sq2[j]:
            result.append(sq[i])
            i+=1
        else:
            result.append(sq2[j])
            cont+=len(sq)-i
            j+=1
    if i < len(sq):
        result += sq[i:]
    else:
        result += sq2[j:]
    return result,cont

def mergeSort(sq):
    if len(sq) <= 1:
        return sq[:],0
    half = len(sq) // 2
    left = mergeSort(sq[:half])
    right = mergeSort(sq[half:])
    mergea = merge(left, right)
    cont = left[1] + right[1] + mergea[1]
    return mergea[0] ,cont

def main():

    lista = [1,2,3,4,5,7,6,8,9]
    rest,cont = mergeSort(lista)
    print(cont)
if __name__ == '__main__':
    main()