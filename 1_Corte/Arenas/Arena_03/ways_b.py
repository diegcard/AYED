from sys import stdin
import math

def cutRod(L, config):
    if L == 0 or L < min(config.keys()):
        return 0
    max_profit = -math.inf
    for cut in config.keys():
        profit = config[cut]
        if cut <= L:
            max_profit = max(max_profit, profit + cutRod(L-cut, config))
    return max_profit

def cutRod_m(L, config, M):
    if L == 0 or L < min(config.keys()):
        return 0
    max_profit = -math.inf
    for cut in config.keys():
        profit = config[cut]
        if cut <= L:
            max_profit = max(max_profit, profit + cutRod_mem(L-cut, config, M))
    return max_profit

def cutRod_mem(L, config, M):
    key = (L, str(config))
    if key in M.keys():
        return M[key]
    M[key] = cutRod_m(L, config, M)
    return M[key]

M = {}

def printPrettyDict(dct):
    for key in dct.keys():
        print(key, ':', dct[key])

def main():
    line = stdin.readline().strip()
    while line:
      config = {}
      n_config = int(line)
      for i in range(n_config):
          cut, profit = [int(x) for x in stdin.readline().strip().split()]
          config[cut] = profit
      queries = [ int(x) for x in stdin.readline().strip().split()]
      for q in queries:
          print(cutRod_mem(q, config, M))
      print('=====================Mem State===========')
      print(printPrettyDict(M))
      line = stdin.readline().strip()

main()