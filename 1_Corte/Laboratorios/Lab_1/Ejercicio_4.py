from sys import stdin
def mcd(x, y):
    while y:
        x, y = y, x % y
    return x

def main():
    n = 0
    while n == 0:
        val = stdin.readline().strip()
        if len(val) > 1:
            val = val.split(" ")
            print(mcd(int(val[0]), int(val[1])))
        else:
            n += 1
if __name__ == '__main__':
    main()