#This program takes a user input of any positive integer 
# and outputs the successive values of the following calculation

x = int(input("Please enter a positive integer: "))

print(x)

while x != 1:
    if x % 2 == 0:
        x = x // 2
        print(x)

    elif x % 2 != 0:
        x = x * 3 + 1
        print(x)