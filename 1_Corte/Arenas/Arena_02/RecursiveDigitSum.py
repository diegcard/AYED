from sys import stdin

def superDig(n):
    rest = 0
    while n !=0:
        rest+=n%10
        n = n//10
    if rest > 10:
        return superDig(rest)
    return rest

def main():
    x = stdin.readline().strip()
    while x:
        x = x.split(" ")
        n = str(x[0])*int(x[1])
        print(superDig(int(n)))
        x = stdin.readline().strip()
main()