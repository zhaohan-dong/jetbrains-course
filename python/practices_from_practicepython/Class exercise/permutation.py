#!/usr/bin/python3


def permutation(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            xc = lst[:i] + lst[i+1:]
            for elem in permutation(xc):
                l.append([x]+elem)
        return l

print(permutation(["a","b","c","d"]))