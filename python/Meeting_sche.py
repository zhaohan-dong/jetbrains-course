#!/usr/bin/env python3

# calculate which dates to meet on till a given time with given schedule

import calendar
import datetime

def main(sy="",sm="",sd="",ey="",em="",ed=""):
    sy=int(input("Please Input Start Year"))
    sm=int(input("Start Month"))
    sd=int(input("Start Date"))
    start = datetime.date(sy, sm, sd)       #define start date
    ey=int(input("Please Input End Year"))
    em=int(input("End Month"))
    ed=int(input("End Date"))
    end=datetime.date(ey,em,ed)     #define end date
    meetday = input("Please Input Meeting Days separated by space").split() #input meeting day number 1-7
    for n in range(len(meetday)):
        meetday[n]=int(meetday[n])-1        #transfer to weekday number 0-6
    y=sy        #set loop start year
    m=sm        #set loop start month
    d=sd      #set loop start date
    while(y<ey):        # loop when year is less than end year
        print(y)        # print year
        while(m<13):        # loop when month is less than 13
            c=calendar.monthcalendar(y,m)       #calendar starting at y, m
            x=len(c)        # x weeks in month m
            print(calendar.month_name[m], end=' ')      #print month name
            for i in range(0,x):
                week=c[i]         # "week" is the "i" item of the month "m"
                for md in meetday:
                        #convert meetday number(1-7) into dayname string
                    if week[md]>=d:
                        print(week[md]," ", end='')       #print only if the date is after start date/1
            d=1             #reset minimum date to 1 after first month loop
            m+=1
            print("\n")
        m=1
        y+=1
        print("\n")
    if(y==ey):      #when year is end year
        print(y)
        while(m<em):
            c = calendar.monthcalendar(y, m)  # calendar starting at y, m
            x = len(c)  # x weeks in month m
            print(calendar.month_name[m], end=' ')  # print month name
            for i in range(0, x):
                week = c[i]  # "week" is the "i" item of the month "m"
                for md in meetday:
                      # convert meetday number(1-7) into dayname string
                    if week[md] >= d:
                        print(week[md], " ", end='')  # print only if the date is after start date/1
            d = 1  # reset minimum date to 1 after first month loop
            print("\n")
            m += 1
        if(m==em):
            c = calendar.monthcalendar(y, m)  # calendar starting at y, m
            x = len(c)  # x weeks in month m
            print(calendar.month_name[m], end=' ')  # print month name
            for i in range(0, x):
                week = c[i]  # "week" is the "i" item of the month "m"
                for md in meetday:
                      # convert meetday number(1-7) into dayname string
                    if week[md] >= d and week[md]<= ed:
                        print(week[md], " ", end='')  # print only if the date is after start date and before end date
            return 0
        if (m>em):
            print("Error Start Month")
            return 0
    if(y>ey):
        print("Error Start Year")
        return 0

if __name__== "__main__":
    main()