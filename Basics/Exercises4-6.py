#Exercise 4
def Hello(name):
    print(f"Hello {name}")

#User input formatted as a string
name = str(input("What is your name? "))
Hello(name)

#Exercise 5
#Libraries and functions
import numpy as np

def Cooking_time(EggType, T0):
    '''
    Function which returns the cooking time for an egg. See Exercise 5 in Exercises.md for equations

    Parameters:
    EggType = small or large
    T0 = Initial temperature of the egg
    '''
    Tw = 100
    Ty = 70
    p = 1.038
    c = 3.7
    K = 0.0054

    if(EggType == "small"):
        M = 47
    elif(EggType == "large"):
        M = 67

    t = np.log(0.76*(T0 - Tw)/(Ty - Tw))*((M**(2/3)*c *p**(1/3))/(K * (np.pi)**2 * (4*np.pi / 3)**(2/3)))
    return t/60

#Note that an egg from fridge has T0 = 4 and an egg at room temperature has T0 = 20
#Printing the time taken for the given scenarios
time1 = Cooking_time("large", 4)
print(f"Large egg from fridge takes {time1} mins\n")

time2 = Cooking_time("large", 20)
print(f"Large egg at room temperature takes {time2} mins\n")

time3 = Cooking_time("small", 4)
print(f"Small egg from fridge takes {time3} mins\n")

time4 = Cooking_time("small", 20)
print(f"Small egg at room temperature takes {time4} mins\n")

#Printing the difference between cooking times for large and small eggs, both from a fride and from room temp
print(f"Difference between small and large egg from a fridge: {time1 - time3}")
print(f"Difference between small and large egg from room temperature: {time2 - time4}")

#Exercise 6
#Local library
import energy_functions as ef

#KE and GPE for a body of mass 20kg moving with velocity 5m/s at height 30m
m, v, h = 20, 5, 30
print(f"KE = {ef.KE(m, v)}J, for m = {m} and v = {v}")
print(f"GPE = {ef.GPE(m, h)}J, for m = {m} and h = {h}")