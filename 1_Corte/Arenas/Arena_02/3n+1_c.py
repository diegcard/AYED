from sys import stdin
def prom(num, i=1):
    if num == 1:
        return i
    else:
        if num % 2 == 0:
            return prom(num//2, i+1)
        else:
            return prom( num*3 +1, i+1)

def maxci(i,j,may=0):
    i, j = min(i, j), max(i, j)
    if i == j:
        return may
    else:
        if prom(i) > may:
            return maxci(i+1, j, prom(i))
        else:
            return maxci(i+1, j, may)
def main():
    line = stdin.readline().strip().split()
    while line:
        print("{} {} {}".format(str(line[0]), str(line[1]),maxci(int(line[0]), int(line[1]))))
        line = stdin.readline().strip().split()
main()