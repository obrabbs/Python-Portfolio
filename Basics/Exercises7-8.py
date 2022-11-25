#Exercise 7

import numpy as np

#a (integers 0-10)
print("(a)")
IntList = [*range(0, 11, 1)]
print(IntList)

#b (floats 0-10)
print("(b)")
FloatArr = np.linspace(0.0, 10.0, num = 20, dtype = float)
print(FloatArr)

#c (append function)
print("(c)")
IntList.append(11)
print(IntList)

#can't use the append function for a numpy array, since arrays are immutable

#d (final value of list and array to 12)
print("(d)")
IntList[11] = 12
print(IntList)
FloatArr[19] = 12
print(FloatArr)

#e (operations on arrays and list)
print("(e)")
def myFunction(a):
    print(a**2)

myFunction(FloatArr)

#can't perform operations on lists

#f (conversion between list and array)
print("(f)")
FloatList = list(FloatArr)
print(FloatList)
IntArr = np.asarray(IntList)
print(IntArr)

#g (2D Array of Floats - 2x3)
print("(g)")
A2 = np.asarray([[2.1, 3.6, 7.4],[11.5, 10.2, 18.6]])
print(A2)

#h (middle column of 2x3 array)
print("(h)")
c = A2[:,1]
print(c)

#i

#mutable list
print("(i): list")
foo = [1, 2, 3, 4, 5]
print(f"original foo id {id(foo)}")
bar = foo
print(f"original bar id {id(bar)}")
bar += [6, 7]
print(f"foo = {foo} with id {id(foo)}")
print(f"bar = {bar} with id {id(bar)}")

print("Both foo and bar add 6 and 7 to the end. The ID is the same for both foo and bar")

#immutable tuple
print("(i): tuple")
foo = (1, 2, 3, 4, 5)
print(f"original foo id {id(foo)}")
bar = foo
print(f"original bar id {id(bar)}")
bar += (6, 7)
print(f"foo = {foo} with id {id(foo)}")
print(f"bar = {bar} with id {id(bar)}")

print("The ID for bar is changed and appends 6 and 7 to the list. Elements in foo remain unchanged with the same ID")

#Exercise 8
#Libraries
import numpy as np
#energy_functions is a local library
import energy_functions as ef

#Constants:
g = 9.81

#User inputs:
v0 = float(input("Initial velocity: "))
m = float(input("Mass: "))

#Functions:
def Time(g, v0):
    '''
    Function to return an array of time values in the range 0<t<(2*v0)/g

    Parameters:
    g = acceleration due to gravity
    v0 = initial velocity
    '''
    tMax = (2 * v0)/g
    t = np.linspace(0, tMax, num = 50, dtype = float) #returns an array of time values: 0<t<(2*v0)/g
    return t
def yFunction(v0, g, t):
    '''
    Function to return an array of values for the altitude y

    Parameters:
    v0 = initial velocity
    g = acceleartion due to gravity
    t = array of time values
    '''
    y = v0*t + 0.5*g*t**2
    return y
def vFunction(v0, g, t):
    '''
    Function to return an array of values for the velocity v
        
    Parameters:
    v0 = initial velocity
    g = acceleartion due to gravity
    t = array of time values

    '''
    v= v0 + g*t
    return v

#Data
t = Time(g, v0)
y = yFunction(v0, g, t)

#Calculating required energies
P = ef.GPE(m, y)
v = vFunction(v0, g, t)
K = ef.KE(m, v)
Total = P + K

#Array manipulation to output the first row and second column
data = np.array([t, y, v, P, K])
print(f"First row: {data[:,0]}")
print(f"Second column: {data[1,:]}")