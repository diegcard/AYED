from sys import stdin
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def solve():
    n = int(stdin.readline())
    stdin.readline()
    for _ in range(n):
        m = int(stdin.readline().strip())
        parent = [i for i in range(m+1)]
        rank = [0] * (m+1)
        success = 0
        unsuccess = 0
        while True:
            try:
                line = input()
                if not line:
                    break
                op, a, b = line.split()
                a, b = int(a), int(b)
                if op == 'c':
                    union(parent, rank, a, b)
                else:
                    if find(parent, a) == find(parent, b):
                        success += 1
                    else:
                        unsuccess += 1
            except EOFError:
                break
        print(f'{success},{unsuccess}')
        if _ != n-1:
            print()

solve()
