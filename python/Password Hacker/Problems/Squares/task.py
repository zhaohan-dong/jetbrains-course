n = int(input())


def squares():
    i = 1
    while i > 0:
        yield pow(i, 2)
        i += 1


# Don't forget to print out the first n numbers one by one here
func = squares()
for i in range(n):
    print(next(func))
