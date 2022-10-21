#!/usr/bin/python3


import random


def main():
    with open('sowpods.txt', "r") as wordbank:
        read = wordbank.read()
        read = read.splitlines()
        word = random.choice(read)
        print(word)

if __name__ == '__main__':
    main()
