cond = input("Enter cells: ")
game = [[cond[0], cond[1], cond[2]],
        [cond[3], cond[4], cond[5]],
        [cond[6], cond[7], cond[8]]]
error = 0
win = False
winner = "_"
impossible = False
xcount = 0
ocount = 0

for elem in cond[0: len(cond)-1]:
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


if error == 0:
    print("---------")
    print("|", game[0][0], game[0][1], game[0][2], "|")
    print("|", game[1][0], game[1][1], game[1][2], "|")
    print("|", game[2][0], game[2][1], game[2][2], "|")
    print("---------")

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
elif win == False:
    if "_" in cond:
        print("Game not finished")
    else:
        print("Draw")
elif win == True:
    print("{} wins".format(winner))
