#!/usr/bin/python3



def subset(lst, low, high):
    if low > high:
        return [[]]
    else:
        rem = subset(lst, low + 1, high)
        sub = []
        for elem in rem:
            sub += [[lst[low]] + elem]
        rem += sub
        return rem

print(subset([4, 5, 6], 0, 2))
