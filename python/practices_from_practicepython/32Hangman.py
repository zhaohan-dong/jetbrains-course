#!/usr/bin/python3


import random


def printguessed(guessed):
    for i in range(len(guessed)):
        print(guessed[i] + " ", end="")
    print("")


def chooseword():
    with open('sowpods.txt', "r") as wordbank:
        read = wordbank.read()
        read = read.splitlines()
        word = random.choice(read)
    return word


def main():
    print("Welcome to Hangman!")
    loop = "y"
    while loop == "y":
        word = chooseword()  # input guess word
        guessed = []  # guessed word, for output
        for i in range(len(word)):  # initialize guessed to _s
            guessed.append("_")
        printguessed(guessed)
        guesses = 0  # how many guesses
        remaining = 6
        used_list = []
        while "_" in set(guessed) and remaining > 0:
            letter = input("Guess your letter: ").upper()
            # check if each letter in word if it matches input
            if letter in set(used_list):
                print("Already guessed")
            elif letter not in set(word):
                used_list.append(letter)
                print("Incorrect")
                guesses += 1
                remaining -= 1
            else:
                for i in range(len(word)):
                    if letter == word[i]:
                        guessed[i] = letter
                used_list.append(letter)
                printguessed(guessed)
                guesses += 1
            print("Remaining guesses: {}".format(remaining))
        if "_" in set(guessed):
            print("You lose")
            print("Correct word: {}".format(word))
        else:
            print("You win")
            print("Total guesses: {}".format(guesses))
        loop = input("Continue?(y/n) ")


if __name__ == '__main__':
    main()
