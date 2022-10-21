#!/usr/bin/python3


def main():
    x = int(input())
    y = int(input())
    z = int(input())
    max = 0
    if x > y:
        max = x
    elif x < y:
        max = y
    if max < z:
        max = z
    print(max)

if __name__ == '__main__':
    main()
