#exercise 06
time =  int(input("Enter the amount of seconds:"))
d = time // 86400
h = time // 3600
m= time // 60
time = time % (24*3600)
time %= 3600
time %= 60
s = time
print(f" d:h:m:s -> {d:}:{h:}:{m:}:{s}") 



