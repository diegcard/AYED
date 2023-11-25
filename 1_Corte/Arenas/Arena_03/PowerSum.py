from sys import  stdin

def PowerSumMemo(x,k,n, M={}):
    if (x,k,n) in M.keys():
        return M[(x,k,n)]
    M[(x, k, n)] = PowerSumP(x,k,n, M)
    return M[(x, k, n)]

def PowerSumP(x,k,n, M={}):
    pnum = n**k
    if x == 0:
        return 1
    if x < 0 or pnum > x:
        return 0
    return PowerSumMemo(x-pnum, k, n+1, M) + PowerSumMemo(x, k, n+1, M)

def PowerSum(x,k,n):
    pnum = n**k
    if x == 0:
        return 1
    if x < 0 or pnum > x:
        return 0
    return PowerSum(x-pnum, k, n+1,) + PowerSum(x, k, n+1)

def main():
    M = {}
    line = stdin.readline().strip()
    while line:
        x = int(line)
        k = int(stdin.readline().strip())
        for i in range(int(line)):
            rest = PowerSumMemo(i, k, 1, M)
        print(PowerSumMemo(x, k, 1, M))
        line = stdin.readline().strip()

main()