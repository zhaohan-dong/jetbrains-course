#
# Example file for working with date information
#

from datetime import date
from datetime import time
from datetime import datetime


def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class

  today = date.today()
  print(today)

  # print out the date's individual components

  print(today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)

  print(today.weekday())
  days = ["a", "b","c", "d", "e", "f", "g"]
  print(days[today.weekday()])

  ## DATETIME OBJECTS
  # Get today's date and time from the datetime class

  today = datetime.now()
  print (today)

  # Get the current time
  t = datetime.time(datetime.now())
  print (t)

  
if __name__ == "__main__":
  main();
  