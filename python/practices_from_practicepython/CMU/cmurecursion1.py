#!/usr/bin/python3


def main():
    print(sum(10))

def sum(x):
    if x > 1:
        return x + sum(x-1)
    elif x == 1:
        return x

if __name__ == '__main__':
    main()