from sys import stdin
def repe(mat):
    normal = []
    for i in mat:
        if i not in normal:
            normal.append(i)
    return normal

def mayor(val):
    mat = []
    rest = []
    for i in val:
        mat.append(i)
    rep_pa = repe(mat)
    cant = []
    for i in range(0, len(rep_pa)):
        acum = 0
        for j in range(0,len(mat)):
            if rep_pa[i] ==  mat[j]:
                acum+=1
        cant.append(acum)
    mayor,pos = 0, 0
    for i in range(0,len(cant)):
        if int(cant[i]) > mayor:
            mayor = cant[i]
            pos = i
    rest.append(rep_pa[pos])
    rest.append(cant[pos])
    return rest
def main():
    n = 0
    while n == 0:
        val = stdin.readline().strip()
        if len(val) > 1:
            x = mayor(val)
            print(str(x[0]) + " -> " + str(x[1]))
        else:
            n = 1
if __name__ == '__main__':
    main()