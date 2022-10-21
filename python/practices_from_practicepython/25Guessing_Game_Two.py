#!/usr/bin/python3


import math


def main():
    print("Please have a number in your head(0-100)")
    print("Input 'h' for Too High and 'l' for Too Low, 'c' for correct")
    max_n = 100
    min_n = 0
    guess = 0
    while True:
        num = list(i for i in range(min_n, max_n + 1))
        middle_index = math.ceil(len(num) / 2) - 1
        print(num[middle_index])
        guess += 1
        if len(num) == 1:
            print("It can only be {}".format(num[0]))
            break
        x = input()
        if x == "c":
            print("Correct! {}".format(num[middle_index]))
            break
        elif x == "h":
            max_n = num[middle_index-1]
            print("Too High!")
        elif x == "l":
            min_n = num[middle_index+1]
            print("Too Low!")
        else:
            print("Error Input")
            guess -= 1
    print("Total Guesses: {}".format(guess))


if __name__ == '__main__':
    main()
