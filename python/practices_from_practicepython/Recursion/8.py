#!/usr/bin/python3


def harmo_sum(num):
    if num == 1:
        return 1
    else:
        return 1 / num + harmo_sum(num - 1)


print(harmo_sum(12))
