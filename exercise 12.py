#exercise 12
from math import sqrt
a = int(input("Enter the length of side a:"))
b = int(input("Enter the length of side b:"))
c = int(input("Enter the length of side c:"))

s = (a +b+c)*0.5

heron_formula = sqrt(s*(s-a) *(s-b) *(s-c))

print(f" The  surface   area  is:  %.2f" % heron_formula ,"cm²")



