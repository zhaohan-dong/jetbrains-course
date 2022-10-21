#!/usr/bin/python3


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    x = int(input("Input number"))
    for i in a:
        if i < x:
            b.append(i)
        else:
            break
    print(b)


if __name__ == "__main__":
    main()
