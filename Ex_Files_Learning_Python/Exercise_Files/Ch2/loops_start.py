#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x < 5):
    print (x)
    x = x+1

  # define a for loop, range sets 'x' to 0 and goes up right before 10
  for x in range(0, 10): #range is exclusive of second parameter
    print (x)

  # use a for loop over a collection
  # days=["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
  # for d in days:
  #   print (d)
    
 
  # use the break and continue statements
  for x in range(5, 10):
    if (x == 7): break
    print (x)

  for x in range(5, 10):
    if (x % 2 == 0): continue
    print (x)

  #using the enumerate() function to get index 
  days=["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
  for i,d in enumerate(days):
    print (i, d) #print out index counter and the actual value

if __name__ == "__main__":
  main()
