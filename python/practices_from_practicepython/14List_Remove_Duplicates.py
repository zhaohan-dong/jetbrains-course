#!/usr/bin/python3


def removedup():
    a = [1, 3, 3, 5, 6, 8, 10, 12, 12, 15, 15, 15]
    b = []
    for i in range(len(a)-1):
        if a[i] not in b:
            b.append(a[i])
    print(b)

def removedup2():
    a = [1, 3, 3, 5, 6, 8, 10, 12, 12, 15, 15, 15]
    b = list(set(a))
    print(b)


if __name__ == '__main__':
    removedup2()
