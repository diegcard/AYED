from sys import stdin
def PoweSumMemo(x,k,n=1,M={}):
    if (x,k,n) in M.keys():
        return M[(x,k,n)]
    M[(x, k, n)] = PowerSumP(x,k,n,M)
    return M[(x, k, n)]

def PowerSumP(x,k,n=1,M={}):
    pnum = n**k
    if x == 0:
        return 1
    if x < 0 or pnum > x:
        return 0
    return PoweSumMemo(x-pnum,k,n+1,M) + PoweSumMemo(x,k,n+1,M)

def PowerSum(x,k,n=1):
    pnum = n**k
    if x == 0:
        return 1
    if x < 0 or pnum > x:
        return 0
    return PowerSum(x-pnum,k,n+1) + PowerSum(x,k,n+1)

def main():
    M = {}
    line = (stdin.readline().strip())
    while line:
        line = int(line)
        k = int(stdin.readline().strip())
        for i in range(line):
            rest = PowerSumP(i, k, 1, M)
        rest = PowerSumP(line,k,1,M)
        print(rest)
        line = (stdin.readline().strip())
main()