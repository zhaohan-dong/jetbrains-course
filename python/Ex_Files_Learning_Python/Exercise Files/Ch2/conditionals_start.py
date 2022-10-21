#
# Example file for working with conditional statements
#

def main():
    x, y= 10, 100

  # conditional flow uses if, elif, else
    if (0<=x<10):
      print("x has one figure")
    elif (x<100):
      print("x has two figures")
    elif (x<1000):
     print("x has three figures")
    else :
      print("error")

  # conditional statements let you use "a if C else b"
  

if __name__ == "__main__":
  main()
