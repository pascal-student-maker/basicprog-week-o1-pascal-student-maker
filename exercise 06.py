#exercise 06
import math
def calculate_time(seconds):
    
    days = seconds // 86400
    hours = math.ceil(seconds % 86400/ 3600)
    minutes = math.ceil((seconds % 86400 ) % 3600/ 60 )
    seconds = seconds % 60
    
    return days ,hours , minutes,seconds
seconds = int(input(" Enter the amount of seconds:"))
days,hours,minutes,seconds = calculate_time(seconds)
print(f" d:h:m:s -> {days}:{hours}:{minutes}:{seconds}")




