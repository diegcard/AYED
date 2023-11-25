from sys import stdin
def balanced(cadena):
    Diccionary = ["(", "["]
    comp_a = {"(": "A",
              "[": "B"}
    comp_b = {")": "A",
              "]": "B"}
    sequence = []
    for i in range(len(cadena)):
        if cadena[i] in Diccionary:
            sequence.insert(0, comp_a[cadena[i]])
        elif len(sequence) == 0:
            return False
        else:
            if comp_b[cadena[i]] == sequence[0]:
                sequence.pop(0)
            else:
                return False
    if len(sequence) == 0:
        return True
    return False

def main():
    n = int(stdin.readline().strip())
    for _ in range(n):
        cadena = stdin.readline().strip()
        print("Yes") if balanced(cadena) else print("No")
main()
