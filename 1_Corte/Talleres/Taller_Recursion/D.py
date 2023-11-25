def mdc(a,b):
    if a == 0:
        return b
    elif a != 0 and b != 0:
        return mdc(b, a%b)
    return a

def main():
    x,y= 8,2
    print(mdc(x,y))
main()