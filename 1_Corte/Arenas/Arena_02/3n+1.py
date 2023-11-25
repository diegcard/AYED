def cycle_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def max_cycle_length(i, j):
    if i > j:
        i, j = j, i
    max_length = 0
    for n in range(i, j+1):
        length = cycle_length(n)
        if length > max_length:
            max_length = length
    return max_length

def main():
    while True:
        try:
            i, j = map(int, input().split())
        except EOFError:
            break
        length = max_cycle_length(i, j)
        print(f"{i} {j} {length}")

if __name__ == '__main__':
    main()
