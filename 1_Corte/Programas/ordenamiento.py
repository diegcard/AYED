def merge(izq,der):
    i,j,lista = 0,0,[]
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            lista.append(izq[i])
            i+=1
        else:
            lista.append(der[j])
            j+=1
    if i < len(izq):
        lista.extend(izq[i:])
    if j < len(der):
        lista.extend(der[j:])
    return lista

def merge_sort(lista):
    mid = len(lista)//2
    if len(lista)==1:
        return lista
    left = merge_sort(lista[mid:])
    right = merge_sort(lista[:mid])
    return merge(left,right)




listadersordena = [9,8,5,4,7,8,5,2,12,365,47,5,2,3,10,0,0,3,2,1,4,5,6,98,7,5]

izq = [2,3,6,9,10]
der = [1,4,5,8,20,58]

#print(merge(izq,der))

print(merge_sort(listadersordena))