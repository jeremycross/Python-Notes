#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()

  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print(now.strftime("%A, %d %B, %y")) #lower case is abbreviated, upper is full word

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime("Locale date and time: %c"))
  print(now.strftime("Locale time: %X"))
  print(now.strftime("Locale date: %x"))


  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("Current time: %I:%M:%S %p"))
  print(now.strftime("24-hour time: %H:%M:%S"))


if __name__ == "__main__":
  main()