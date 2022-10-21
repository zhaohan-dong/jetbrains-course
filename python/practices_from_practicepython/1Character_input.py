#!/usr/bin/python3

from datetime import datetime
import datetime


def main():
    thisyear = datetime.date.today()
    thisyear = int(thisyear.strftime("%Y"))
    age = input("Enter your age: ")
    age = int(age)
    year = thisyear - age + 100
    print("This year is {}" .format(thisyear))
    print("In {} you will be 100 years old." .format(year))




if __name__ == '__main__':
    main()
