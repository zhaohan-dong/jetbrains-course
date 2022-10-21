file = open('salary.txt', 'r')
new_file = open('salary_year.txt', 'w+')
for line in file:
    line.replace('\n', '')
    new_file.write(str(int(line) * 12) + '\n')
file.close()
new_file.close()
