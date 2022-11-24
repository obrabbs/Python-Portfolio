#Exercise 1(a)

print("Hello World")

#Exercise 1(b)

#a)
print(5**2)
print(25**(0.5))

#b)

print((5 + (5**2 -4 * 8 * 3))/(2*8))

#c)

def quadratic_solver(a, b, c):  #function to solve quadratic equations (i.e. ax^2 + bx +c)
    x_plus = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
    x_minus = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
    return x_plus, x_minus

print(quadratic_solver(47.2, -148.1, 72.6))
print(quadratic_solver(-19, 67, 82))

#Exercise 2
name = input("Name: ")
age = int(input("Age: "))
height = float(input("Height (cm): "))
weight = float(input("Weight (kg): "))

print(f"Hi {name}, you are {age} years old. You are {height}cm tall and have a weight of {weight}kg." )

if(age < 40):
    print(f"Your age is {40.5-age} years off the UK median of 40.5.")
else:
    print(f"Your age is {age-40.5} years off the UK median of 40.5.")

#Exercise 3
import numpy as np


x = float(input("Value of x (degrees): "))
x = x * (np.pi / 180)
cosx = np.cos(x)
acosx = 1 - (x**2)/2 + (x**4)/(4*3*2) - (x**6)/(6*5*4*3*2) #acosx = approximate value of cosx

print(f"cosx = {cosx} and from the series expansion cosx = {acosx}.")

if(cosx > acosx):
    absDiff = cosx - acosx
    perDiff = (absDiff * 100)/acosx
else:
    absDiff = acosx - cosx
    perDiff = (absDiff * 100)/cosx
print(f"Absolute difference = {absDiff}, \nand Percentage difference = {perDiff} %.")