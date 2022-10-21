def range_sum(numbers, a, b):
    result = 0
    for elem in numbers:
        if a <= elem <= b:
            result += elem
    return result


numbers = [int(elem) for elem in input().split(' ')]
a, b = [int(elem) for elem in input().split(' ')]
print(range_sum(numbers, a, b))
