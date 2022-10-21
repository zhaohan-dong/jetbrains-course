#!/usr/bin/python3
import math


def tanfov(focal_length, diag):
    # calculation in rad, input focal length in mm
    return math.tan(2 * math.atan(diag / (2 * focal_length)))


def main():
    c = float(input("Circle of Confusion in mm: "))
    hn = float(input("Height of near object in mm: "))
    hf = float(input("Height of far object in mm: "))
    f = float(input("Focal length in mm: "))
    d = float(input("Diagonal of frame in mm: "))
    N = (f * f * (hf - hn)) / \
        (c * ((2 * hf * hn) / tanfov(f, d) - f * (hf + hn)))
    print("The required F-stop is: {}".format(N))


if __name__ == '__main__':
    main()
