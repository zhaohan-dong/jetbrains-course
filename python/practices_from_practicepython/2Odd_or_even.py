#!/usr/bin/python3

def main():
    x = int(input("Enter a number "))
    if x % 4 == 0:
        print("A different message")
    elif x % 2 == 0:
        print("Even")
    else:
        print("Odd")

if __name__=="__main__":
    main()