#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


# construct a basic timedelta and print it
print (timedelta(days=356, hours=5, minutes=1))

# print today's date
now = datetime.now()
print ("today is: " + str(now))

# print today's date one year from now
print ("one year from now it will be: " + str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print ("in two days and 3 weeks from now it will be: " + str(now + timedelta(days=2, weeks=3)))

# calculate the date 1 week ago, formatted as a string
t = now - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print (s)

### How many days until April Fools' Day?
today = date.today()
a = date(today.year, 4, 1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if (a < today):
    print ("april fools already went by %d days ago" % ((today-a).days))
    a = a.replace(year=today.year+1)

# Now calculate the amount of time until April Fool's Day  
time_to_a = a-today

print ("It's just ", time_to_a.days, "days until april fools")

p = timedelta(minutes=9, seconds=35)
p = p + timedelta(minutes=5, seconds=2)
p = p + timedelta(minutes=7, seconds=32)
p = p + timedelta(minutes=8, seconds=16)
p = p + timedelta(minutes=2, seconds=54)
p = p +timedelta(minutes=10, seconds=20)
p = p + timedelta(minutes=10, seconds=57)
p = p + timedelta(minutes=5, seconds=36)

totsec = p.total_seconds()
h = totsec//3600
m = (totsec%3600) // 60
sec = p.seconds % 60

print ("%d:%d:%d" %(h, m, sec))