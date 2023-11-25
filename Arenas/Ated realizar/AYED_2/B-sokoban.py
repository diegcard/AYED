from sys import stdin
Map = []
worker = []
targets = 0
B = 0
def board_configuration(rows,columns):
    global Map
    global targets
    global B
    global worker
    targets = 0
    B = 0
    Map = [[0 for j in range(columns)] for i in range(rows)]
    for R in range(rows):
        line = stdin.readline().strip()
        for C in range(columns):
            Map[R][C] = line[C]
            if (line[C] == 'w' or line[C] == 'W'): 
                worker = [R, C]
            if (line[C] == '+' or line[C] == 'B' or line[C] == 'W'): 
                targets += 1
            if (line[C] == 'B'): 
                B += 1
def win():
    if(B == targets):
        return True
    else:
        return False
def movements(vertical, horizontal):
    global Map
    global B
    global worker
    #A donde me quiero mover ahí un target o un espacio en blanco
    if ((Map[worker[0] + vertical][worker[1] + horizontal] == '.') or (Map[worker[0] + vertical][worker[1] + horizontal] == '+')):
        Map[worker[0] + vertical][worker[1] + horizontal] = 'w' if (Map[worker[0] + vertical][worker[1] + horizontal] == '.') else 'W'
        Map[worker[0]][worker[1]] = '.' if (Map[worker[0]][worker[1]] == 'w') else '+'
        worker[0] += vertical
        worker[1] += horizontal
    elif((Map[worker[0] + vertical][worker[1] + horizontal] == 'b') or (Map[worker[0] + vertical][worker[1] + horizontal] == 'B')):
        if not ((Map[worker[0] + vertical * 2][worker[1] + horizontal * 2] == '#') or (Map[worker[0] + vertical * 2][worker[1] + horizontal * 2] == 'b') or (Map[worker[0] + vertical * 2][worker[1] + horizontal * 2] == 'B')):
            Map[worker[0]][worker[1]] = '.' if (Map[worker[0]][worker[1]] == 'w') else '+'
            worker[0] += vertical
            worker[1] += horizontal
            Map[worker[0]][worker[1]] = 'w' if (Map[worker[0]][worker[1]] == 'b') else 'W'
            Map[worker[0] + vertical][worker[1] + horizontal] = 'b' if (Map[worker[0] + vertical][worker[1] + horizontal] == '.') else 'B'
            if((Map[worker[0]][worker[1]] == 'W') and (Map[worker[0] + vertical][worker[1] + horizontal] == 'b')): B -= 1
            if((Map[worker[0] + vertical][worker[1] + horizontal] == 'B') and (Map[worker[0]][worker[1]] == 'w')): B += 1
def keystrokes():
    win()
    num_kt = 0
    line = stdin.readline().strip()
    while((win() is False) and (num_kt < len(line))):
        if (line[num_kt] == 'U' or line[num_kt] == 'D'):
            vertical = -1 if (line[num_kt] == 'U') else 1
            horizontal = 0
        else:
            horizontal = 1 if (line[num_kt] == 'R') else -1
            vertical = 0
        num_kt += 1
        movements(vertical, horizontal)
def final_board(game):
    if(win() is True):
        print(f"Game {game}: complete")
    else:
        print(f"Game {game}: incomplete")
    for row in Map:
        print(''.join(row))
def main():
    games = 1
    line = stdin.readline().strip()
    while(line != '0 0'):
        data = list(map(int, line.split(' ')))
        board_configuration(data[0],data[1])
        keystrokes()
        final_board(games)
        games += 1
        line = stdin.readline().strip()
main()

