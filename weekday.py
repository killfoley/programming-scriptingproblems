#this program will output if today is a weekday
#or weekend day

import datetime

now = datetime.datetime.now()

if now.weekday() >= 0 and now.weekday() <= 4:
    print("Yes, unfortunately today is a weekday.")

if now.weekday() == 5 or now.weekday() == 6:
    print("It is the weekend, yay!")