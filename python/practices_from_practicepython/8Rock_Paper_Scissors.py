#!/usr/bin/python3


def main():
    loop = 1
    while loop == 1:
        i = input("Player 1 \nRock, Paper, Scissors")
        j = input("Player 2 \nRock, Paper, Scissors")
        if i not in ["Rock", "Paper", "Scissors"] or j not in ["Rock", "Paper", "Scissors"]:
            print("Error Input")
            continue
        if i == j:
            print(i, j, "\nDraw")
        elif i == "Rock":
            if j == "Paper":
                print(i, j, "Player 2 Wins")
            else:
                print(i, j, "Player 1 Wins")
        elif i == "Scissors":
            if j == "Rock":
                print(i, j, "Player 2 Wins")
            else:
                print(i, j, "Player 1 Wins")
        if input("Again?(Yes)") == "Yes":
            continue
        else:
            break

if __name__ == '__main__':
    main()
