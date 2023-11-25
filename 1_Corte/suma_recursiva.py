def suma(arr):
    return 0 if len(arr) == 0 else arr[0] + suma(arr[1:])
def suma_pila(arr, index=0, sum=0):
    return sum if index >= len(arr) else suma_pila(arr, index+1, sum+arr[index])
