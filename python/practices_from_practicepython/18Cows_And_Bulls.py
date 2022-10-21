#!/usr/bin/python3
import random


def numgen(length=4):
    return str(random.randint(10 ** (length - 1), 10 ** length - 1))


def numcomp(num, user):
    cowbullcount = [0, 0]
    for i in range(len(num)):
        if num[i] == user[i]:
            cowbullcount[0] += 1
        elif num[i] in user:
            cowbullcount[1] += 1
    return cowbullcount


def main():
    print("Welcome to the Cows and Bulls Game!")
    l = int(input("Please select a level (2-10): "))
    print("Enter a number:")
    gen = numgen(l)
    guesses = 1
    print(gen)
    while True:
        x = input()
        if x == "exit":
            break
        elif len(x) != l:
            print("Wrong input")
            continue
        cowbull = numcomp(gen, x)
        if cowbull[0] == l:
            print("You win! Total guesses: {}".format(guesses))
            break
        else:
            print("{} cows, {} bulls".format(cowbull[0], cowbull[1]))
            print("Try again! Total guesses: {}".format(guesses))
        guesses += 1


if __name__ == '__main__':
    main()
