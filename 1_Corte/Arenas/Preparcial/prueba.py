from sys import stdin

def waysMemo(monto, coins, c_index, M={}):
    if (monto, c_index) in M.keys():
        return M[(monto, c_index)]
    M[(monto, c_index)] = waysP(monto, coins, c_index, M)
    return M[(monto,c_index)]

def waysP(monto, coins, c_index=0, M={}):
    if monto == 0:
        return 1
    if c_index >= len(coins) or monto < 0:
        return 0
    return waysMemo(monto - coins[c_index], coins, c_index, M) + waysMemo(monto, coins, c_index+1, M)

M = {}
def main():
    line = 4#stdin.readline().strip()
    coins = [4, 3, 2, 2, 1, 1]
    #while line:
    #for i in range(int(line)):
    #    resp = waysMemo(i, coins, 0, M)
    res = waysMemo(int(line), coins, 0, M)
    #if res == 1:
    #    print("There is only 1 way to produce {} cents change.".format(line))
    #else:
    #    print("There are {} ways to produce {} cents change.".format(res,line))
    print(res)
    for clave, valor in M.items():
        print(str(clave) + ": " + str(valor))
    #line = stdin.readline().strip()

main()