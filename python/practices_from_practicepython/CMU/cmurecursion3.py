#!/usr/bin/python3


def digits(n):
    if n < 10:
        return 1
    else:
        return digits(n//10) + 1


def main():
    print(digits(15))
    print(digits(105))
    print(digits(15105))


if __name__ == '__main__':
    main()
