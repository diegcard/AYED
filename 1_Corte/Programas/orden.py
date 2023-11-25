from sys import stdin
def merge(izq,der):
    i,j,list = 0 , 0 , []
    while i < len(izq) and j<len(der):
       if izq[i] <= der[j]:
            list.append(izq[i])
            i+=1
       else:
           list.append(der[j])
           j += 1
    if i < len(izq):
        list.extend(izq[i:])
    if j < len(der):
        list.extend(der[j:])
    return list

def mergesort(lista):
    mid = len(lista)//2
    if len(lista) <= 1:
        return lista[:]
    izq = mergesort(lista[mid:])
    der = mergesort(lista[:mid])
    return merge(izq,der)


iz = [2,5,7,8,10,12,15]
der = [1,3,6,9]

desord = [5,9,8,7,4,5,2,3,6,5,4,1,8,1,5,4,5,4,54,58,74,21,12,36,2,7,4,5,8,7,4,7,8,5,8,4,58,7,4,5,1,2,1,2,3,2,1,4,5,7,8,5,9,5,8,7,4,5,8,95]
#print(merge(iz,der))
print(mergesort(desord))