
def menor(lista):
    men = lista[0]
    longitud = len(lista)
    for i in range(1,longitud):
        valor = lista[i]
        if valor > men:
            men = valor
    print(men)

lista = [5,8,9,5,6,3,2,1]
lista = list(map(str,lista))
print(",".join(lista))
