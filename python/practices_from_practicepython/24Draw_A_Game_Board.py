#!/usr/bin/python3


def drawboard():
    x = int(input("Please input size of Tic Tac Toe game board: "))
    for i in range(x):
        for j in range(x):
            print(" ---", end="")
        print(" ")
        for m in range(x):
            print("|   ", end="")
        print("|")
    for p in range(x):
        print(" ---", end="")
    print(" ")


if __name__ == '__main__':
    drawboard()
