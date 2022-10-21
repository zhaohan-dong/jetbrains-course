#!/usr/bin/python3


def sumdigit(num):
    str_num = str(num)
    if len(str_num) == 1:
        return num
    else:
        res = int(str_num[0]) + sumdigit(int(str_num[1:]))
        return res

print(sumdigit(1206397120968216))