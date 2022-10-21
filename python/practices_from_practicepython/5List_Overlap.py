#!/usr/bin/python3

import random


def main():
    a = random.sample(range(1, 50), random.randint(1, 20))
    b = random.sample(range(1, 50), random.randint(1, 20))
    common = []
    print("a = {} \nb = {}" .format(sorted(a), sorted(b)))
    for i in a:
        if i in b:
            if i not in common:
                common.append(i)
    common.sort()
    print(common)





if __name__ == "__main__":
    main()
