#exercise 12
from math import sqrt
a = int(input("Enter the length of the side a:"))
b = int(input("Enter the length of the side b:"))
c = int(input("Enter the length of the side c:"))
s = (a+b+c)*0.5
heron_formula = sqrt(s*(s-a) * (s-b) * (s-c))
print(f" the surface area is : %.2f" % heron_formula)

