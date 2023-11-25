def numPares(number):
    cont = 0
    for i in number:
        if int(i)%2 == 0:
            cont+=1
    return cont

def recur(number,cont):
    x = number//10
    val = number%10
    if number ==0:
        return 1
    if x != 0:
        if val%2 == 0:
            return recur(x,cont+1)
        return recur(x,cont)
    else:
        return cont

def main():
    number = 0#int(input("Ingrese el numero: "))
    print(recur(number,0))

main()