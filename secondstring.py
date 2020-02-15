#This program takes a user inputed string and 
# outputs every second letter in reverse order

sentence = str(input("Please enter a sentence: ", ))

#Take every second character starting at the 2nd character
x = sentence[1::2]

#Reverse the first step
y = x[-1::-1]

print("Here is every second character in reverse order:", y)