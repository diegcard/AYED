from sys import stdin
M = {}

def sumaMemo(t,lista,c_index,M={}):
    if (t, c_index) in M.keys():
        return M[(t,c_index)]
    M[(t,c_index)] = sumaP(t,lista,c_index,M)
    return M[(t,c_index)]

def sumaP(t,lista,c_index=0, M={}):
    if t == 0:
        return 1
    if c_index >= len(lista) or t < 0:
        return 0
    return sumaMemo(t - lista[c_index], lista, c_index, M) + sumaMemo(t, lista, c_index+1, M)
M = {}
def main():
    line = list(map(int,stdin.readline().strip().split(" ")))
    t = line[0]
    n = line[1]
    lista = line[2:]

    for i in range(int(t)):
        res = sumaMemo(i,lista,0,M)
        print(M)
    resp = sumaMemo(t,lista,0,M)

    print(resp)

main()