import itertools
from string import ascii_lowercase

password_char = tuple(ascii_lowercase + '0123456789')
i = 1
count = 0
while True:
    password_iter = itertools.product(password_char, repeat=i)
    for j in range(pow(36, i)):
        password = next(password_iter)
        password = ''.join(password)
        print(password, i)
        count += 1

        if count == 1000000:
            print('Too many attempts')
            break
    i += 1
    if count == 1000000:
        break
