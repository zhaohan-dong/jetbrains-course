def multiply(a, b):
    if b == 1:  # base case
        return a
    else:  # recursive case
        return a + multiply(a, b - 1)
