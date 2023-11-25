#Alison Geraldine Valderrama Munar
#100093218
from sys import stdin
def waysMemo(x, coins, index, M={}):
    if (x, index) in M.keys():
        return M[(x, index)]
    M[(x, index)] = waysP(x, coins, index, M)
    return M[(x,index)]

def waysP(x, coins, index=0, M={}):
    if x == 0:
        return 1
    if index >= len(coins) or x < 0:
        return 0
    return waysMemo(x - coins[index], coins, index, M) + waysMemo(x, coins, index+1, M)

M = {}
def main():
    line = stdin.readline().strip()
    coins = [1, 5, 10, 25, 50]
    while line:
        for i in range(int(line)):
            resp = waysMemo(i, coins, 0, M)
        res = waysMemo(int(line), coins, 0, M)
        if res == 1:
            print("There is only 1 way to produce {} cents change.".format(line))
        else:
            print("There are {} ways to produce {} cents change.".format(res,line))
        line = stdin.readline().strip()

main()