#!/usr/bin/python3


def main():
    bd_dict = {"Albert Einstein": 1, "Benjamin Franklin": 2, "Ada Lovelace": 3}
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    print("\n".join(bd_dict.keys()))
    key = input("Who's birthday do you want to look up?")
    print("{}'s birthday is {}".format(key, bd_dict.get(key, "DNE")))


if __name__ == '__main__':
    main()
