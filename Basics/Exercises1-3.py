#Exercise 1(a)

print("Hello World")

#Exercise 1(b)

#a)
print(5**2)
print(25**(0.5))

#b)

print((5 + (5**2 -4 * 8 * 3))/(2*8))

#c)

def quadratic_solver(a, b, c):
    '''
    Function to solve quadratics of the form ax^2 + bx +c = 0 returning two roots

    Parameters (all required):
    a = x^2 coefficient
    b = x coefficient 
    c = constant
    '''
    x_plus = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
    x_minus = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
    return x_plus, x_minus

print(quadratic_solver(47.2, -148.1, 72.6))
print(quadratic_solver(-19, 67, 82))

#Exercise 2
#User inputs:
name = input("Name: ")
age = int(input("Age: "))
height = float(input("Height (cm): "))
weight = float(input("Weight (kg): "))

print(f"Hi {name}, you are {age} years old. You are {height}cm tall and have a weight of {weight}kg." )

#Conditional to find how many years away the user's age is from the UK median age
if(age < 40):
    print(f"Your age is {40.5-age} years off the UK median of 40.5.")
else:
    print(f"Your age is {age-40.5} years off the UK median of 40.5.")

#Exercise 3
#Libraries
import numpy as np

#User input of x (in degrees)
x = float(input("Value of x (degrees): "))

#Conversion from degrees to radians
x = x * (np.pi / 180)

#Finding cos(x) and the approximate value of cos(x), acosx, from a series expansion
cosx = np.cos(x)
acosx = 1 - (x**2)/2 + (x**4)/(4*3*2) - (x**6)/(6*5*4*3*2)

print(f"cosx = {cosx} and from the series expansion cosx = {acosx}.")

#Conditional to calculate the absolute and percentage difference between the known and approximated value
if(cosx > acosx):
    absDiff = cosx - acosx
    perDiff = (absDiff * 100)/acosx
else:
    absDiff = acosx - cosx
    perDiff = (absDiff * 100)/cosx
print(f"Absolute difference = {absDiff}, \nand Percentage difference = {perDiff} %.")