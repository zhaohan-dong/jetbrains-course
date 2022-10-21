#!/usr/bin/python3


def main():
    prime = open("primenumbers.txt", "r")
    happy = open("happynumbers.txt", "r")
    plist = []
    slist = []
    result = []
    for line in prime:
        plist.append(int(line))
    for line in happy:
        slist.append(int(line))
    for i in plist:
        if i in slist:
            result.append(i)
    print(sorted(result))

if __name__ == '__main__':
    main()