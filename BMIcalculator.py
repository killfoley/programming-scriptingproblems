#This program will calculate the user's BMI
#based on their input height (cm) and weight (kg)

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

#convert height to meters
height = height / 100

#BMI alculation is weight divide height squared.
BMI = weight / (height**2)

#Round BMI to 1 decimal place
BMI = round(BMI, 1)

#print("Your BMI is", BMI)

#If loop to return BMI information to user

if BMI < 18.5:
    print("Your BMI is", BMI, "You are under weight")

elif BMI > 18.5 and BMI <= 24.9:
    print("Your BMI is", BMI, "You are a healthy weight")

elif BMI > 25 and BMI <= 29.9:
    print("Your BMI is", BMI, "You are overweight")

elif BMI > 30 and BMI <= 39.9:
    print("Your BMI is", BMI, "You are obese")

elif BMI > 40:
    print("Your BMI is", BMI, "You are morbidly obese")