#!/usr/bin/python3


def check():
    game = [[1, 2, 1],
            [2, 1, 1],
            [2, 1, 0]]
    Win = False
    diagl = game[0][0] == game[1][1] == game[2][2] != 0
    diagr = game[0][2] == game[1][1] == game[2][0] != 0
    if diagl or diagr:
        Win = True
        print("Player {} Wins" .format(game[1][1]))
    if not Win:
        for i in range(3):
            row = game[i][0] == game[i][1] == game[i][2] != 0
            if row:
                Win = True
                print("Player {} Wins".format(game[i][0]))
                break
    if not Win:
        for j in range(3):
            column = game[0][j] == game[1][j] == game[2][j] != 0
            if column:
                Win = True
                print("Player {} Wins".format(game[0][j]))
                break


if __name__ == '__main__':
    check()
