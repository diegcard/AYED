from sys import stdin
from random import randint
from time import time
SEQ = 1
MAX = 255
SIZE = 1e6

def sortElement(A, element, dir = True):
    index, criteria = 0, A[0] < element if dir else A[0] > element
    while index < len(A) and criteria:
       index += 1
       if(index < len(A)):
           criteria = A[index] < element if dir else A[index] > element
    return A[:index] + [element] + A[index:]

def insertionSort(seq, dir=True):
    A = seq
    for el in range(1,len(A)):
        A = sortElement(A[:el], A[el], dir) + A[el+1:]
    return A
"""
Merge Sort
"""
def merge(sq, sq2):
    i, j, result = 0, 0, []
    while i < len(sq) and j < len(sq2):
        if sq[i] <= sq2[j]:
            result.append(sq[i])
            i+=1
        else:
            result.append(sq2[j])
            j+=1
    if i < len(sq):
        result += sq[i:]
    else:
        result += sq2[j:]
    return result

def mergeSort(sq):
    if len(sq) <= 1:
        return sq[:]
    half = len(sq) // 2
    left = mergeSort(sq[:half])
    right = mergeSort(sq[half:])
    return merge(left, right)


def main():
    for i in range(int(SEQ)):
        sq = [ randint(-MAX, MAX) for i in range(int(SIZE))]
        print(sq)
        print("Case", i+1, ":")
        #print("Unsorted sq", sq)
        #t_0 = time()
        #insertionSort(sq)
        #print("sorted sq")
        #t_1 = time()
        #print(t_1 - t_0)
        t_0 = time()
        ms_sq = mergeSort(sq)
        #print("ms(sq): ", ms_sq)
        t_1 = time()
        print(t_1 - t_0)
main()
#print(merge([1,5,7,9,15], [6,10,16,25]))