import random

global board, player, cpu, GameOver

def showBoard():
    print(board[0], '|', board[1], '|', board[2])
    print('-' * 9)
    print(board[3], '|', board[4], '|', board[5])
    print('-' * 9)
    print(board[6], '|', board[7], '|', board[8])

def cpuMove():
    while True:
        cpu_pos = random.randint(0, 8)
        if board[cpu_pos] == ' ':
            board[cpu_pos] = 'o'
            cpu.add(cpu_pos)
            break;

def isValid(val):
    if val > 3 or val < 1 :
        print("\nInvalid Input\nEnter Values Between 1 & 3\nTry Again\n\n")
        return False
    return True

def playerMove():
    row = int(input("Enter Row: "))
    if not isValid(row):
        return playerMove()
    col = int(input("Enter Column: "))
    if not isValid(col):
        return playerMove()
    player_pos = (row - 1) * 3 + (col - 1)
    if board[player_pos] == ' ':
        board[player_pos] = 'x'
    else:
        print("\nPosition Already Taken\n")
        return playerMove()
    player.add((row - 1) * 3 + (col - 1))

win = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {6, 4, 2}, {0, 4, 8})

play = 'Y'
print("Enter Values Between 1 & 3\n")

while play == 'Y':
    board = [' '] * 9
    player = set()
    cpu = set()
    GameOver = False

    showBoard()

    while GameOver == False:
        playerMove()
        if ' ' not in board:
            print("\n\nGame Tied\n\n")
            break
        cpuMove()
        showBoard()
        for case in win:
            if case.issubset(player):
                print("\n\nYou Won\n\n")
                GameOver = True
                break
            elif case.issubset(cpu):
                print("\n\nCPU Won\n\n")
                GameOver = True
                break
    
    while True:
        play = input("Play Again(Y/N)? ").upper()
        if play == 'Y' or play == 'N':
            break
        else:
            continue

print("\nExiting Game...\n\n")
