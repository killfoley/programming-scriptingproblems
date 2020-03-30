#this program will output an approximation for 
# the square root of a given input number

a = float(input("enter a positive number: "))

def sqrt(a, TOL=0.0001):
    #calcluate the first approximation
    x = 0.5 * a
    y = 0.5 * (x + a / x)
    #exectue while loop until new result of calculation does not become more accurate than previous
    for i in range(20):
        x = y
        y = 0.5 * (x + a / x)
        if y - x**2 < TOL:
            return x

#print result rounding to 1 decimal    
print("The square root of", a, "is approx.", round(sqrt(a), 1))


