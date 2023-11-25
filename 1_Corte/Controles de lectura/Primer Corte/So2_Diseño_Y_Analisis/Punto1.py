"""
Dado un arreglo de n enteros, cuyos valores van de decremento y luego en aumento, encontrar el menor numero de el arreglo
"""
def buscar_menor(array):
    if array[-1] < array[-2]:
        return array[-1]
    else:
        array.pop(-1)
        return buscar_menor(array)

"""
Dado un arreglo de n-1 enteros ordenados, cuyos valores de 1 a n encontrar el numero faltante del arreglo
"""
def faltante(array):
    longitud = len(array)+1
    if (longitud *(longitud+1) // 2) != sum(array):
        val = (longitud * (longitud + 1) // 2) - sum(array)
        return val
    return faltante(array)

"""
Potencia de un numero
"""
def potencia(n,ex):
    if ex == 0:
        return 1
    elif ex % 2 == 0:
        rest = potencia(n,ex//2)
    else:
        rest = potencia(n,(ex - 1)//2)
        return rest*rest*n

"""
Dado un numero x, encontrar el numero menor n tal que la suma de los bits de cada numero
desde 1 hasta n sea al menos x
"""
def buscar_n(x)
    n=0
    sum_val = 0
    while sum_val < x:
        n+=1
        sum_val+=bin(n).count("1")
    return n