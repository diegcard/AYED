def inver(arr):
    if len(arr) == 0:
        return arr
    return [arr[-1]] +inver(arr[:-1])

def main():
    arr = [1,2,3,4,5,6,7,8,9]
    print(inver(arr))
main()