def suma_par(n):
    if n < 2:
        return 0
    else:
        return n + suma_par(n-2) if n % 2 == 0 else suma_par(n-1)

def main():
    print(suma_par(4))
main()