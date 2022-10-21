#!/usr/bin/python3


def main():
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    playing = 0 in game[0] or 0 in game[1] or 0 in game[2]
    while playing:
        while playing:
            p1 = input("Player 1, Please input move coordinate in 'row' 'column': ")
            p1 = p1.split(" ")
            if len(p1) == 2 and 0 < int(p1[0]) < 4 and 0 < int(p1[1]) < 4:
                if game[int(p1[0])-1][int(p1[1])-1] == 0:
                    game[int(p1[0])-1][int(p1[1])-1] = "X"
                else:
                    print("It has been taken")
                    continue
                print(game)
            else:
                print("Wrong Input!")
                continue
            playing = 0 in game[0] or 0 in game[1] or 0 in game[2]
            break
        while playing:
            p2 = input("Player 2, Please input move coordinate in 'row' 'column': ")
            p2 = p2.split(" ")
            if len(p2) == 2 and 0 < int(p2[0]) < 4 and 0 < int(p2[1]) < 4:
                if game[int(p2[0]) - 1][int(p2[1]) - 1] == 0:
                    game[int(p2[0]) - 1][int(p2[1]) - 1] = "O"
                else:
                    print("It has been taken")
                    continue
                print(game)
            else:
                print("Wrong Input!")
                continue
            playing = 0 in game[0] or 0 in game[1] or 0 in game[2]
            break


if __name__ == '__main__':
    main()