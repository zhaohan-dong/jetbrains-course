x = input()
li = [int(digit) for digit in x]
result = 0.0
for i in range(len(li)):
    result += li[i]
result = result / len(li)
print(result)
