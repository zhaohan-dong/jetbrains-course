#!/usr/bin/python3


def main():
    x = int(input("How many Fibonacci numbers to generate: "))
    a = [1, 1]
    if x == 0:
        print("")
    elif x == 1:
        print(1)
    elif x >= 2:
        for i in range (1, x-1):
            a.append(a[i-1] + a[i])
    print(a)

if __name__ == '__main__':
    main()