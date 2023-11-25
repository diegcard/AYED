from sys import stdin

def decoding(texto):
    l = 0
    texto_final = []
    for i in texto.split():
        if len(i) > l:
            texto_final.append(i[l])
            l += 1
    return texto_final

def main():
    cases = int(stdin.readline().strip())
    input()
    for case in range(cases):
        print("Case #{}:".format(str(case+1)))
        texto = stdin.readline().strip()
        while texto:
            print("".join(decoding(texto)))
            texto = stdin.readline().strip()
        print()

if __name__ == '__main__':
    main()
