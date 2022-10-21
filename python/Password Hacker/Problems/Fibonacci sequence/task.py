from math import sqrt


def fibonacci(n):
    phi = (sqrt(5) + 1) / 2
    for i in range(n):
        yield pow(phi, i) - (pow(-1, n) / pow(phi, n)) / sqrt(5)
