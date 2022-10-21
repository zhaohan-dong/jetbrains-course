n = int(input())


def even():
    for i in range(n):
        yield i * 2


# Don't forget to print out the first n numbers one by one here
generator = even()
for i in range(n):
    print(next(generator))
