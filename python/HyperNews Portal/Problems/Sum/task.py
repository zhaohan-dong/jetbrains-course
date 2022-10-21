# read sums.txt
file = open('sums.txt', 'r')
for line in file:
    number = [int(elem) for elem in line.split(" ")]
    print(number[0]+number[1])
file.close()