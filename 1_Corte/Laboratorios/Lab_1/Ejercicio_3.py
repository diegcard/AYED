from sys import stdin
def palindromo(pal):
    if len(pal) == 1:
        return "True"
    elif len(pal) == 2:
        if pal[:1] == pal[-1]:
            return "True"
        else:
            return "False"
    else:
        if pal[:1] == pal[-1]:
            return palindromo(pal[1:-1])
        else:
            return "False"

def main():
    pal = stdin.readline().strip()
    while pal:
        rest = palindromo(pal)
        print(rest)
        pal = stdin.readline().strip()
        
if __name__ == '__main__':
    main()