#!/usr/bin/python3


def main():
    import string
    import secrets
    poolpre = string.ascii_letters + string.digits + string.punctuation
    pool = poolpre.replace("|", "")  # delete | from string
    length = int(input("Password Length? "))
    while True:
        password = "".join(secrets.choice(pool) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
    with open("file.txt", "w+") as file_op:
        file_op.write(password)
        file_op.close()
    print("password saved in file.txt")


if __name__ == '__main__':
    main()
