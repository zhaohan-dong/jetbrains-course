#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import tzinfo

def main():

    # construct a basic timedelta and print it

    print(timedelta(days=365, hours=5, minutes=1))

    # print today's date

    now = datetime.now()
    print("today is:" + str(now))

    # print today's date one year from now

    print("one year from now it will be:" + str(now+timedelta(days=365)) )


    # create a timedelta that uses more than one argument

    print("In 2 days and 3 weeks, it will be:" + str(now+timedelta(days=2, weeks=3)))

    # calculate the date 1 week ago, formatted as a string
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d %Y")
    print( "One week ago it was: " + s)

### How many days until April Fools' Day?

    t= date.today()
    afd=date(t.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year

    if afd<t:
        print ("April Fool's day already went by by %d days ago" % (t-afd).days)
        afd = afd.replace(year= today.year+1)


# Now calculate the amount of time until April Fool's Day  

    time_to_afd = afd-t
    print("It's just %d day until April Fool's day" % time_to_afd.days )

# days from a given day

    givenday = datetime(2020, 3, 6, 20, 30, 50)
    print("Time 1 week 2 days 1 minute and 20 seconds from 2020-03-06 20:30:50 is "
          + str(givenday+timedelta(days=2,weeks=1,minutes=1,seconds=20)))


if __name__ == "__main__":
    main()