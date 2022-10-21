#!/usr/bin/python3

def main():
    x = int(input("Input number"))
    for i in range(1,x+1):
        if x % i == 0:
            print(i)

if __name__=="__main__":
    main()
