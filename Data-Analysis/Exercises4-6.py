#Exercise 4
import numpy as np

#(a): Guess number in list

def IsItemInList(List, Num):
    if(Num in List):
        return True
    else:
        return False

randNums = np.random.randint(1, 21, 10)
guess = int(input("What is your guess? "))
print(f"Are you lucky? {IsItemInList(randNums, guess)}")

#(b): Iteration of a List

def OddOrEven(List):
    for i in List:
        if(i%2 == 0):
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

OddOrEven(randNums)

#Exercise 5
import numpy as np
#(a): Heaviside Function

def Heavy(x):
    if(x < 0):
        return 0
    else:
        return 1

print(f"x=-0.5: H(x)={Heavy(-0.5)}")
print(f"x=0: H(x)={Heavy(0)}")
print(f"x=10: H(x)={Heavy(10)}")

#(b): Smoothed Heaviside Function

def HeavySmooth(x):
    e = 0.1
    if(x < -e):
        return 0
    elif(x > e):
        return 1
    else:
        return 0.5 + x/(2*e) + (1/(2*np.pi))*np.sin((np.pi*x)/e)

print(f"x=-1: H(x)={HeavySmooth(-1)}")
print(f"x=-0.001: H(x)={HeavySmooth(-.001)}")
print(f"x=0.001: H(x)={HeavySmooth(0.001)}")
print(f"x=1: H(x)={HeavySmooth(1)}")

#(c): Visualise both functions for -1<x<1
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 200, dtype=float)
H = []
HSmoothed = [] 

for i in x:
    H.append(Heavy(i))
    HSmoothed.append(HeavySmooth(i))

plt.plot(x, H, label="Heaviside Function")
plt.plot(x, HSmoothed, label="Smoothed Heaviside Function")
plt.xlabel("x")
plt.ylabel("H(x)")
plt.title("Heaviside Function for -1<x<1")
plt.legend()
plt.minorticks_on()
plt.show()
plt.savefig("HeavisideFunction.pdf")

#Exercise 6
#(a): Free fall with Drag

#Libraries and Functions
import numpy as np
import matplotlib.pyplot as plt

def Acceleration(m, v):
    g = 9.81
    #Area from height*width = 1.85*0.3 =
    A = 0.555
    rho = 1.225
    #Note that drag coeff cd = 1
    Fd = (v**2 * A * rho) / 2
    F = m * g - Fd
    return F/m


#Initial Conditions:
m = 75
y = [5500]
a = [9.81]
v = [0]
t = [0]
dt = 0.1

#Data:
i = 0
while min(y) > 0.0:
    t.append(t[i] + dt)
    a.append(Acceleration(m, v[i]))
    v.append(v[i] + a[i] * dt)
    y.append(y[i] - v[i] * dt)
    i += 1

#Terminal Velocity and Time of Flight:
vTerminal = max(v)
ToF = max(t)
print(f"Terminal velocity: {round(vTerminal, 1)},\nTime of flight: {round(ToF, 1)}.")

#Plot:
fig, ax1 = plt.subplots()
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Height [m]", color='blue')
plot_1 = ax1.plot(t, y, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.set_ylabel('Velocity [$ms^{-1}$]', color='red')
plot_2 = ax2.plot(t, v, color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title("Freefall with Drag")
plt.show()
plt.savefig("Freefall-with-drag.pdf")

#(b): Dependence of the terminal velocity with mass
#Libraries and Functions
import numpy as np
import matplotlib.pyplot as plt

#Functions
def Acceleration(m, v):
    g = 9.81
    #Area from height*width = 1.85*0.3 =
    A = 0.555
    rho = 1.225
    #Note that drag coeff cd = 1
    Fd = (v**2 * A * rho) / 2
    F = m * g - Fd
    return F/m

#Data:
#array m contains varying mass elements from 0.001-100kg
m = (np.linspace(1, 100000, 1000))/1000
#empty list for terminal velocities
vTerminal = []

for i in m:
    y = [5500]
    a = [9.81]
    v = [0]
    t = [0]
    dt = 0.1
    z = 0
    for j in v:
        t.append(t[z] + dt)
        if(max(t)<=ToF):
            a.append(Acceleration(i, j))
            v.append(j + a[z] * dt)
            z += 1

    vTerminal.append(max(v))

#Plot:
fnt = 14
plt.plot(m, vTerminal)
plt.title("Terminal Velocity against Mass \nvarying from 1g to 100kg with N=1000 data points", fontsize=fnt)
plt.xlabel("Mass [kg]", fontsize=fnt)
plt.ylabel("Terminal Velocity [m$s^{-1}$]", fontsize=fnt)
plt.minorticks_on()
plt.tick_params(labelsize=fnt)
plt.savefig("Terminal-velocity-with-varying-mass.pdf")