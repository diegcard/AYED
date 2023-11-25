
def suma(line,lista):
    cas = 0
    i = 0
    for case in range(len(lista)**2):
        suma = line
        for j in range(len(lista)):
            print(lista[i])
            if i+1 == len(lista):
                i = 0
                break
            suma = suma-lista[i]
            print("la suma es ", suma)
            if suma == 0:
                print("Paso")
                cas+=1
                i+=1
                break
            if suma != 0:
                i+=1
            if suma < 0:
                i = 0
    return cas


def main():
    line = 4
    lista = [4, 3, 2, 2, 1, 1]
    print("el total es: ",suma(line,lista))
if __name__ == '__main__':
    main()