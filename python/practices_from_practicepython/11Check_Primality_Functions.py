#!/usr/bin/python3


def main():
    x = int(input("Give me a number: "))
    p = True
    for i in range(2, x-1):
        if x % i == 0:
            p = False
            break
    if p and x > 1:
        print("{} is a prime".format(x))
    else:
        print("{} is not a prime".format(x))


if __name__ == '__main__':
    main()
