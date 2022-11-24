#Exercise 4
def Hello(name):
    print(f"Hello {name}")

name = str(input("What is your name? "))

#Exercise 5

import numpy as np

def Cooking_time(EggType, T0):
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

time1 = Cooking_time("large", 4)
print(f"Large egg from fridge takes {time1} mins\n")
time2 = Cooking_time("large", 20)
print(f"Large egg at room temperature takes {time2} mins\n")
time3 = Cooking_time("small", 4)
print(f"Small egg from fridge takes {time3} mins\n")
time4 = Cooking_time("small", 20)
print(f"Small egg at room temperature takes {time4} mins\n")

print(f"Difference between small and large egg from a fridge: {time1 - time3}")
print(f"Difference between small and large egg from room temperature: {time2 - time4}")

#Exercise 6

import energy_functions

m, v = 20, 5
print(f"KE = {energy_functions.kinetic_energy(m, v)}J, for m = {m} and v = {v}")
h = 30
print(f"GPE = {energy_functions.gravitational_potential_energy(m, h)}J, for m = {m} and h = {h}")

