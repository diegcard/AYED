from sys import stdin
def trhee(n,cnt):
    if n== 1:
        return(n,cnt)
    if n%2==0:
        return trhee(n/2,cnt+1)
    return trhee((3*n)+1,cnt+1)
def compare(value1,value2):
    if value1>value2:
        return value1
    return value2
def main():
    n=stdin.readline().strip().split()
    while n:
        n_ints=[int(x) for x in n] 
        t1,t2=trhee(n_ints[0],1),trhee(n_ints[1],1)
        big = compare(t1[1],t2[1])
        print(n_ints[0],n_ints[1],big)
        n=stdin.readline().strip().split()
main()
