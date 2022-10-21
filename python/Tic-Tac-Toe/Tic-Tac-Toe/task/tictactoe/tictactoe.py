#!/usr/bin/python3
error = 0
game = [["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]]


def print_table():
    if error == 0:
        print("---------")
        print("|", game[0][0], game[0][1], game[0][2], "|")
        print("|", game[1][0], game[1][1], game[1][2], "|")
        print("|", game[2][0], game[2][1], game[2][2], "|")
        print("---------")


def askinput():
    global coord
    coord = input("Enter the coordinates: ")
    coord.split(" ")
    coord = list(coord)
    coord.pop(1)


def checkinput(turn):
    for i in range(len(coord)):
        if coord[i] not in ["0", "1", "2",
                            "3", "4", "5",
                            "6", "7", "8",
                            "9"]:
            print("You should enter numbers!")
            return False
        elif int(coord[i]) > 3 or int(coord[i]) < 1:
            print("Coordinates should be from 1 to 3!")
            return False
        else:
            coord[i] = int(coord[i])
    j = coord[0] - 1
    i = 3 - coord[1]
    if turn % 2 == 1 and game[i][j] == "_":
        game[i][j] = "X"
        return True
    elif turn % 2 == 0 and game[i][j] == "_":
        game[i][j] = "O"
        return True
    else:
        print("This cell is occupied! Choose another one!")
        return False


def checkwin():
    global win
    win = False
    winner = "_"
    impossible = False
    xcount = 0
    ocount = 0

    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] != "_":
            if winner == "_":
                win = True
                winner = game[i][0]
            else:
                impossible = True

    for j in range(3):
        if game[0][j] == game[1][j] == game[2][j] != "_":
            if winner == "_":
                win = True
                winner = game[0][j]
            else:
                impossible = True

    if game[0][0] == game[1][1] == game[2][2] != "_":
        if winner == "_":
            win = True
            winner = game[1][1]
        else:
            impossible = True

    if game[0][2] == game[1][1] == game[2][0] != "_":
        if winner == "_":
            win = True
            winner = game[1][1]
        else:
            impossible = True

    for sub in game:
        for elem in sub:
            if elem == "X":
                xcount += 1
            elif elem == "O":
                ocount += 1

    if abs(xcount - ocount) > 1:
        impossible = True

    if impossible:
        print("Impossible")
        return True
    elif win:
        print("{} wins".format(winner))
        return True
    elif "_" in game[0] or "_" in game[1] or "_" in game[2]:
        return False
    else:
        print("Draw")
        return True


def main():
    turn = 1
    win = False
    print_table()
    while win is False:
        correctinput = False
        while correctinput is False:
            askinput()
            correctinput = checkinput(turn)
        print_table()
        win = checkwin()
        turn += 1


if __name__ == '__main__':
    main()
