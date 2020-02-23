#this program will output if today is a weekday
#or weekend day

import datetime

now = datetime.datetime.now()

#now.weekday returns day or the week as integer between 0 and 6
#reference https://docs.python.org/2/library/datetime.html
if now.weekday() >= 0 and now.weekday() <= 4:
    print("Yes, unfortunately today is a weekday.")

if now.weekday() == 5 or now.weekday() == 6:
    print("It is the weekend, yay!")