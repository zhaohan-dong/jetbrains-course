#!/usr/bin/python3

def printguessed(guessed):
    for i in range(len(guessed)):
        print(guessed[i] + " ", end="")
    print("")

def main():
    print("Welcome to Hangman!")
    word = "EVAPORATE"  # input guess word
    guessed = []    # guessed word, for output
    for i in range(len(word)):      # initialize guessed to _s
        guessed.append("_")
    printguessed(guessed)
    guesses = 0     # how many guesses
    while "_" in set(guessed):
        letter = input("Guess your letter: ")
        # check if each letter in word if it matches input
        if letter in set(guessed):
            print("Already guessed")
        elif letter not in set(word):
            print("Incorrect")
            guesses += 1
        else:
            for i in range(len(word)):
                if letter == word[i]:
                    guessed[i] = letter
            printguessed(guessed)
            guesses +=1
    print("Total guesses: {}" .format(guesses))





if __name__ == '__main__':
    main()