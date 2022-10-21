# write your code here
import socket
import sys
import itertools
from string import ascii_lowercase

password_char = tuple(ascii_lowercase + '0123456789')
args = sys.argv


def main():
    address = (args[1], int(args[2]))
    with socket.socket() as my_socket:
        my_socket.connect(address)
        count = 0
        i = 1

        while True:
            password_iter = itertools.product(password_char, repeat=i)
            for j in range(pow(36, i)):
                password = next(password_iter)
                password = ''.join(password)
                data = password.encode(encoding='utf-8')
                my_socket.send(data)

                response = my_socket.recv(1024)
                response = response.decode(encoding='utf-8')
                count += 1

                if response == 'Connection success!':
                    print(password)
                    break
                if count == 1000000:
                    print('Too many attempts')
                    break
            i += 1
            if response == 'Connection success!':
                break
            if count == 1000000:
                break


if __name__ == '__main__':
    main()
