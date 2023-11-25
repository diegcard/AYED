import math

def binary(lista,n):
    mid = len(lista) //2
    if lista[mid] == n:
        return True
    if lista[mid] != n and len(lista) == 1:
        return False
    if len(lista) > 0 and n > lista[mid]:
        return binary(lista[mid:],n)
    if len(lista) > 0 and n < lista[mid]:
        return binary(lista[:mid],n)

def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    n = 4
    print(binary(lista,n))
    if binary(lista,n):
        print(f"El numero {n} si se encuentra en la lista")
    else:
        print(f"El numero {n} no se encuentra en la lista")
main()