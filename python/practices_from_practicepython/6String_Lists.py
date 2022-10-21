#!/usr/bin/python3

def main():
    word = input("Is this a palindrome")
    # string reversal using [start_index:end_index:step(default=1)] step -1 makes it reverse
    rev = word[::-1]
    print(rev)
    if rev == word:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()