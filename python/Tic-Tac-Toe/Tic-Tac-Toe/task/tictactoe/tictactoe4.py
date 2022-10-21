def print_table():
    if error == 0:
        print("---------")
        print("|", game[0][0], game[0][1], game[0][2], "|")
        print("|", game[1][0], game[1][1], game[1][2], "|")
        print("|", game[2][0], game[2][1], game[2][2], "|")
        print("---------")

def checkwin():
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

    for elem in cond:
        if elem == "X":
            xcount += 1
        elif elem == "O":
            ocount += 1

    if abs(xcount - ocount) > 1:
        impossible = True

    if impossible:
        print("Impossible")
    elif not win:
        if "_" in cond:
            print("Game not finished")
        else:
            print("Draw")
    elif win:
        print("{} wins".format(winner))

def askinput():
    global coord
    coord = input("Enter the coordinates: ")
    coord.split(" ")
    coord = list(coord)
    coord.pop(1)

def checkinput():
    for i in range(len(coord)):
        if coord[i] not in ["0", "1", "2",
                            "3", "4", "5",
                            "6", "7", "8",
                            "9"]:
            print("You should enter numbers!")
            return 1
        elif int(coord[i]) > 3 or int(coord[i]) < 1:
            print("Coordinates should be from 1 to 3!")
            return 1
        else:
            coord[i] = int(coord[i])
    j = coord[0] - 1
    i = 3 - coord[1]
    if game[i][j] == "_":
        game[i][j] = "X"
        return 0
    else:
        print("This cell is occupied! Choose another one!")
        return 1

def init():
    error = 0
    cond = input("Enter cells: ")
    game = [[cond[0], cond[1], cond[2]],
        [cond[3], cond[4], cond[5]],
        [cond[6], cond[7], cond[8]]]
    for elem in cond[0: len(cond) - 1]:
        if elem == "X":
            continue
        elif elem == "O":
            continue
        elif elem == "_":
            continue
        else:
            print("Error")
            error = 1
            break

init()
print_table()
askinput()
while checkinput():
    askinput()
print_table()

