def getcellstoCenter(x,y,n):
    center = n-1
    return max(abs(x-center),abs(y-center)) + 1

def printSquare(mat):
    for line in mat:
        print(' '.join(map(str, line)))

def generateWonderSquare(n):
    size = 2*n-1
    mat = [[ getcellstoCenter(i,j,n) for j in range(size)] for i in range(size)]
    return mat
printSquare(generateWonderSquare(5))