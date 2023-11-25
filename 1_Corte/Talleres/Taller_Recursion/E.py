def binari(n, bi):
    if n // 2 != 0:
        return binari(n//2, str(n%2) + str(bi))
    return str((n%2)) + str(bi)

def main():
    n = 16
    text = ""
    print(binari(n,text))
main()