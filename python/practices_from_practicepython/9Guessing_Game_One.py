#!/usr/bin/python3

import random


def main():
    r = 0
    while 1 == 1:
        a = random.randint(1, 9)
        n = 0
        guesses = 0
        r += 1
        while 1 == 1:
            print("\nRound: {} Guesses: {}".format(r, guesses))
            n = input("Guess a number between 1 and 9, Enter 'exit' to quit: ")
            if n == "exit":
                break
            elif n < str(a):
                print("Too Low")
            elif n == str(a):
                print("Exactly Right")
                break
            elif n > str(a):
                print("Too High")
            guesses += 1
        if n == "exit":
            break

    print("Round: {} Guesses: {}".format(r - 1, guesses))


if __name__ == '__main__':
    main()
