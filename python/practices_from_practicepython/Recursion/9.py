#!/usr/bin/python3


def geosum(num):
    if num == 1:
        return 1
    else:
        return 1/num + geosum(num-1)


print(geosum(11))