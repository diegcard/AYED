from sys import stdin

def camp(campos,x1,x2,y1,y2,count):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if campos[i][j] == 1:
                continue
            elif campos[i][j] == 0:
                campos[i][j] = 1
                count += 1
    return count

def main():
    w, h, n = list(map(int,stdin.readline().strip().split()))
    while w != 0 and h != 0 and n != 0:
        campos = [[0 for j in range(h)] for i in range(w)]
        count = 0
        while n > 0:
            x1, y1, x2, y2 = list(map(int, stdin.readline().strip().split()))
            x1-=1
            y1-=1
            x2-=1
            y2-=1
            x1, x2 = min(x1, x2), max(x1, x2)
            y1, y2 = min(y1, y2), max(y1, y2)
            count = camp(campos, x1, x2, y1, y2,count)
            n -= 1
        rest = (w*h)-count
        if rest == 0:
            print("There is no empty spots.")
        elif rest == 1:
            print("There is one empty spot.")
        else:
            print("There are {} empty spots.".format(rest))
        input()
        w, h, n = list(map(int, stdin.readline().strip().split()))
    input()

main()