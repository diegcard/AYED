from sys import stdin
def primo(n):
    if n == 1: return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
def main():
    x = []
    n,i = int(stdin.readline().strip()),1
    while len(x) != n:
        if primo(i):
            x.append(i)
        i+=1
    print(f'Los {n} numeros primos son:')
    print(", ".join(map(str,x))+".")
main()