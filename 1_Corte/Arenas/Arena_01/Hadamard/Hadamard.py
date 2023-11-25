from sys import stdin
import math


def potencia(size):
    if not math.log(size, 2).is_integer():
        return False
    else:
        return True


def una_mat(b_list, size):
    matrix = [[0 for i in range(size)] for j in range(size)]
    index = 0
    for row in range(size):
        for column in range(size):
            if b_list[index] == 'T':
                matrix[row][column] = 1
            else:
                matrix[row][column] = -1
            index += 1
    return Produ(matrix, size)


def Produ(matrix, size):
    estado = True
    product = 0
    for row in range(size-1):
        for column in range(size):
            product = product + matrix[row][column]*matrix[row+1][column]
        if product != 0:
            estado = False
    return estado


def main():
    size = int(stdin.readline().strip())
    if potencia(size):
        val = (stdin.readline().strip()).split()
        if size == 1 and val[0] == 'F':
            print("No Hadamard")
        elif una_mat(val, size):
            print("Hadamard")
        else:
            print("No Hadamard")
    else:
        print("Imposible")

main()

