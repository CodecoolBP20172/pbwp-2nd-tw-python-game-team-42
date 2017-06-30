import random
import os
board = []
legit = True
over = False
steps = 0
score = 0
direction = None


# LISTA KÉSZÍTÉS
def create_board():
    for i in range(4):
        board.append([" "]*4)
    """
    board[0][0] = "2"
    board[0][1] = "4"
    board[0][2] = "8"
    board[0][3] = "16"
    board[1][0] = "32"
    board[1][1] = "64"
    board[1][2] = "128"
    board[1][3] = "256"
    board[2][0] = "512"
    board[2][1] = "1024"
    board[2][2] = "1024"
    """
    user_input()


# GUI
def print_board():
    count = 0
    print("Steps: " + str(steps) + "    Score:" + str(score))
    print("==========================================")
    for i in board:
        print("%1s %4s %4s %4s %4s %4s %4s %4s %4s" % ("||", "", "|", "", "|", "", "|", "", "||"))
        print("%1s %4s %4s %4s %4s %4s %4s %4s %4s" % ("||", i[0], "|", i[1], "|", i[2], "|", i[3], "||"))
        print("%1s %4s %4s %4s %4s %4s %4s %4s %4s" % ("||", "", "|", "", "|", "", "|", "", "||"))
        if count < 3:
            print("||--------------------------------------||")
            count += 1
    print("==========================================")


# BEILLESZT EGY RANDOM HELYRE EGY RANDOM SZÁMOT
def random_number():
    empties = []
    global over
    for i in range(4):
        for j in range(4):
            if board[i][j] == " ":
                empties.append([i, j])
            if board[i][j] == "2048":
                over = True
                return print("YOU WIN!")
    if len(empties) == 0:
        over = True
        return print("GAME OVER")
    ri = random.choice(empties)
    rn = random.choice(["2", "4"])
    board[ri[0]][ri[1]] = rn
    empties = []


def move_horizontal():
    global direction
    for i in range(4):
        if direction == "right" or direction == "d":
            board[i].reverse()
        for j in range(4):
            for k in range(j):
                if board[i][k] == " ":
                    board[i][k] = board[i][j]
                    board[i][j] = " "
        if direction == "right" or direction == "d":
            board[i].reverse()


def melt_horizontal():
    global score
    global direction
    for i in range(4):
        if direction == "right" or direction == "d":
            board[i].reverse()
        for j in range(4):
            if board[i][j] == board[i][j-1] and board[i][j] != " " and j != 0:
                board[i][j] = " "
                board[i][j-1] = str(int(board[i][j-1]) * 2)
                score += int(board[i][j-1])
        if direction == "right" or direction == "d":
            board[i].reverse()


def move_vertical():
    global direction
    for j in range(4):
        if direction == "down" or direction == "s":
            board.reverse()
        for i in range(4):
            for k in range(i):
                if board[k][j] == " ":
                    board[k][j] = board[i][j]
                    board[i][j] = " "
        if direction == "down" or direction == "s":
            board.reverse()


def melt_vertical():
    global score
    global direction
    for j in range(4):
        if direction == "down" or direction == "s":
            board.reverse()
        for i in range(4):
            if board[i][j] == board[i-1][j] and board[i][j] != " " and i != 0:
                board[i][j] = " "
                board[i-1][j] = str(int(board[i-1][j]) * 2)
                score += int(board[i-1][j])
        if direction == "down" or direction == "s":
            board.reverse()


def user_input():
    global steps
    global direction
    os.system("clear")
    random_number()
    print_board()
    while over is False:
        try:
            direction = input("Choose a direction: ")
            if direction == "right" or direction == "left" or direction == "d" or direction == "a":
                move_horizontal()
                melt_horizontal()
                move_horizontal()
                steps += 1
                legit = True
            elif direction == "up" or direction == "down" or direction == "w" or direction == "s":
                move_vertical()
                melt_vertical()
                move_vertical()
                steps += 1
                legit = True
            elif direction == "exit":
                break
            else:
                os.system("clear")
                print_board()
                print("Invalid input")
                legit = False
        except KeyboardInterrupt:
            os.system("clear")
            print_board()
            print("Miki nem")
            legit = False

        if legit is True and over is False:
            os.system("clear")
            random_number()
            print_board()


def main():
    create_board()

main()
