from sys import stdin
def wonder(datos):
    matriz = []
    count = 2
    if datos == 1: return [[1]]
    else:
        variable_ini = [1]
        matriz.append(variable_ini)
        for i in range(datos-1):
            for j in range(count-1):
                matriz[j].insert(0,count), matriz[j].append(count)
            temporal = [count for i in range(len(matriz)+2)]
            matriz.append(temporal), matriz.insert(0,temporal)
            count+=1
    return matriz

def main():
    datos = int(stdin.readline().strip())
    rest = wonder(datos)
    for i in rest:
        print(*i)
if __name__ == '__main__':
    main() 
