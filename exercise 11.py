# exercise 11


import math
print(dir(math))


#module sys

import sys
a= print(sys.version)
print(f"The used  python version is: {a}  ")


#datetime
from datetime import datetime
c= datetime.now()
current_time = c.strftime('%H%M:%S')
print(' The Current date and time is:',c)

#area of a circle
a = float(input("Enter the radius of the circle:"))
b = a*a
c = float(b * 3.14)
print(f"The area of the circle with radius {a} is {c:.2f}")

# volume of a sphere
r = float(input("Radius of the sphere:"))
a =  r*r*r
V = float((4/3) * 3.14 *a)
print(f"The volume of the sphere with radius {r} is {V:.2f}")

#calender
import calendar
yy = 2018
mm = 8
print(calendar.month(yy,mm))

#print cpu
import multiprocessing
cpu_count = multiprocessing.cpu_count()
print(cpu_count)

