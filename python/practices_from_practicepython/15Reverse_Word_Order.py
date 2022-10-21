#!/usr/bin/python3


def main():
    string = input("Input a sentence: ")
    string = string.split(" ")
    reverse = string[::-1]
    reverse = " ".join(reverse)
    print(reverse)


if __name__ == '__main__':
    main()