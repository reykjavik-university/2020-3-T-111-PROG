# Advanced
secs_str = input("Input seconds: ")
secs_int = int(secs_str)
hours = secs_int//3600
remainder = secs_int%3600
minutes = remainder//60
seconds = remainder%60
print(hours,":",minutes,":",seconds)