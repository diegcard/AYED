
def suma_rango(arr, suma, i, j):
    if len(arr) <= 1:
        return arr[0]
    if i != j:
        return suma_rango(arr,suma+arr[i],i+1,j)
    return suma
def main():
    arr = [1,2,3,4,5]
    i = 4
    j = len(arr)
    print(suma_rango(arr,0,i,j))

main()