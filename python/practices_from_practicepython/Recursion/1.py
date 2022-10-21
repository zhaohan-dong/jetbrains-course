#!/usr/bin/python3
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php


def sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        res = lst[0] + sum(lst[1:])
        return res

print(sum([1, 2, 3, 4, 5]))