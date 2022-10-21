

numbers = [10, 20, 10, 40, 50, 60, 70]
for i in range(len(numbers)):
    for j in range(i, len(numbers)):
        if numbers[i] + numbers[j] == 50:
            print(i, j)