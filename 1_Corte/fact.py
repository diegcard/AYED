from sys import stdin

def FactMemo(n,M={}):
    if (n) in M.keys():
        return M[(n)]
    M[(n)] = factorialP(n, M)
    return M[(n)]

def factorialP(n, M={}):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * FactMemo(n-1)

def mi():
    M = {}
    n = int(input())
    while n != 0:
        print(FactMemo(n, M))
        for i in range(n):
            FactMemo(i, M)
        print(M)
        n = int(input())
mi()
