# read sample.txt and print the number of lines
count = 0
file = open('sample.txt', 'r')
for line in file:
    count += 1
file.close()
print(count)