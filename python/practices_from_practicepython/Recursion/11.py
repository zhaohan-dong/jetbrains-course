#!/usr/bin/python3

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        if a > b:
            return gcd(a % b, b)
        elif a < b:
            return gcd(a, b % a)
        else:
            return a


print(gcd(250, 125))