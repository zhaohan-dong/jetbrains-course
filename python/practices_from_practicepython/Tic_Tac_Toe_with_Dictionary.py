#!/usr/bin/python3


def drawboard(game):
    for i in range(3):
        for j in range(3):
            print(" ---", end="")
        print(" ")
        for m in range(3):
            print("|", game[i][m], "",  end="")
        print("|")
    for p in range(3):
        print(" ---", end="")
    print(" ")


# check(game) returns a list in [<win>, <display win message>]
def check(game):
    win = False
    winline = ""
    diagl = game[0][0] == game[1][1] == game[2][2] != " "
    diagr = game[0][2] == game[1][1] == game[2][0] != " "
    if diagl or diagr:
        win = True
        if game[1][1] == "X":
            winline = "Player 1 Wins"
        else:
            winline = "Player 2 Wins"
    if not win:
        for i in range(3):
            row = game[i][0] == game[i][1] == game[i][2] != " "
            if row:
                win = True
                if game[i][1] == "X":
                    winline = "Player 1 Wins"
                else:
                    winline = "Player 2 Wins"
                break
    if not win:
        for j in range(3):
            column = game[0][j] == game[1][j] == game[2][j] != " "
            if column:
                win = True
                if game[1][j] == "X":
                    winline = "Player 1 Wins"
                else:
                    winline = "Player 2 Wins"
                break
    return win, winline


def main():
    game = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]
    drawboard(game)
    print("done")
    playing = " " in game[0] or " " in game[1] or " " in game[2]
    # loop for the whole game
    while playing and check(game)[0] is not True:

        # loop for player 1 till correct input given
        while playing and check(game)[0] is not True:
            p1 = input("Player 1, Please input move coordinate in 'row' 'column': ")
            p1 = p1.split(" ")

            # detect if input is valid
            if len(p1) == 2 and 0 < int(p1[0]) < 4 and 0 < int(p1[1]) < 4:

                # replace if the spot is not taken
                if game[int(p1[0]) - 1][int(p1[1]) - 1] == " ":
                    game[int(p1[0]) - 1][int(p1[1]) - 1] = "X"
                else:
                    print("It has been taken")
                    continue
                drawboard(game)

            else:
                print("Wrong Input!")
                continue
            playing = " " in game[0] or " " in game[1] or " " in game[2]
            break   # break for player 1 on correct move

        # loop for player 2 till correct input given
        while playing and check(game)[0] is not True:
            p2 = input("Player 2, Please input move coordinate in 'row' 'column': ")
            p2 = p2.split(" ")

            # detect if input is valid
            if len(p2) == 2 and 0 < int(p2[0]) < 4 and 0 < int(p2[1]) < 4:

                # replace if the spot is not taken
                if game[int(p2[0]) - 1][int(p2[1]) - 1] == " ":
                    game[int(p2[0]) - 1][int(p2[1]) - 1] = "O"
                else:
                    print("It has been taken")
                    continue
                drawboard(game)

            else:
                print("Wrong Input!")
                continue
            playing = " " in game[0] or " " in game[1] or " " in game[2]
            break   # break for player 2 on correct move
    print(check(game)[1])


if __name__ == '__main__':
    main()
