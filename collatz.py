#This program takes a user input of any positive integer 
# and outputs the successive values of the following calculation
#If it is even, it is divided by 2
#if it is odd it is multiplied by 3 and adds 1.
#Program ends when current value is 1

number = int(input("Please enter a positive integer: "))

print(number)

while number != 1:
    if number % 2 == 0:
#// operator discards remainer. Returns int
        number = number // 2 
        print("{}".format(number))

    elif number % 2 != 0:
        number = number * 3 + 1
        print("{}".format(number))