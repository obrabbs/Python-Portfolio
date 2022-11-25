#Exercise 1 (2D plots)
#Libraries
import numpy as np
import matplotlib.pyplot as plt
import energy_functions as ef

#Constants
g = 9.81 #acceleration due to gravity+
v0 = 10 #initial velocity = 10m/s
m = 5 #mass = 5kg

#Functions:
def Time(g, v0):
    tMax = (2 * v0)/g
    t = np.linspace(0, tMax, num = 50, dtype = float) #returns an array of time values: 0<t<(2*v0)/g
    return t
def yFunction(v0, g, t):
    y = v0*t - 0.5*g*t**2
    return y
def vFunction(v0, g, t):
    v= v0 - g*t
    return v

#Data Inputs:
t = Time(g, v0)
y = yFunction(v0, g, t)
P = ef.GPE(m, y)
v = vFunction(v0, g, t)
K = ef.KE(m, v)
E = P + K

data = [t, P, K, E]

#Plotting:
plt.plot(t, P, 'red', label="Potential Energy")
plt.plot(t, K, 'blue', label="Kinetic Energy")
plt.plot(t, E, 'magenta' ,label="Total Energy")
plt.ylim([0, 1.3*max(E)])
plt.legend(loc='upper left')
plt.show()

#Exercise 2 (3D Data)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#1 (Wavefunction):
def Psi(x, y):
    L, nx, ny = 1, 1, 2 #constants
    psi = (2/L)*np.sin((nx*np.pi*x)/L)*np.sin((ny*np.pi*y)/L)
    return psi

x = np.linspace(0, 1, num = 51, dtype = float)
y = np.linspace(0, 1, num = 51, dtype = float)
X, Y = np.meshgrid(x, y)
wf = Psi(X, Y) #wf = wavefunction

 #3D Plot:
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, wf)
plt.title("3D plot of the wavefunction for a particle in a box")
plt.xlabel("x")
plt.ylabel("y")
ax.set_zlabel("\u03A8(x, y)")
plt.show()
plt.savefig("3D_wavefunction.pdf")

 #Contour Map:
fig,ax = plt.subplots(1,1)
cp = ax.contourf(X, Y, wf)
fig.colorbar(cp)
plt.title('Contour plot representing the wavefunction for a particle in a box')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.savefig("Contour_wavefunction.pdf")

#2 (Probability of the Wavefunction)
def Probability(Z):
    return Z**2

Prob = Probability(wf) #Prob = probability of wavefunction

 #3D Plot:
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Prob)
plt.title("3D plot representing the probability of the wavefunction for a particle in a box")
plt.xlabel("x")
plt.ylabel("y")
ax.set_zlabel("\u03A8(x, y)")
plt.show()
plt.savefig("3D_prob_wavefunction.pdf")

 #Contour Map:
fig,ax = plt.subplots(1,1)
cp = ax.contourf(X, Y, Prob)
fig.colorbar(cp)
plt.title('Contour plot representing the probability of the wavefunction for a particle in a box')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
plt.savefig("Contour_prob_wavefunction.pdf")

#3 (1D Cross-Section)
#X[25] = 0.5

plt.plot(Y[:,25], wf[:,25], label = "Wavefunction")
plt.plot(Y[:,25], Prob[:,25], label = "Probability of the wavefunction")
plt.legend()
plt.title("1D cross-section at x=0.5 for the wavefunction and its probability")
plt.xlabel('y')
plt.ylabel('z')
plt.show()
plt.savefig("Wavefunction_x-0.5.pdf")

#Exercise 3 (Scipy: curve_fit function)
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Data:
T = np.array([0.0, 25.0, 50.0, 75.0, 100.0, 125.0, 150.0, 175.0, 200.0, 225.0, 250.0])
L = np.array([1.1155, 1.1164, 1.117, 1.1172, 1.118, 1.119, 1.1199, 1.121, 1.1213, 1.1223, 1.1223])
yerr = np.array([0.0003, 0.0003, 0.0003, 0.0003, 0.0003, 0.0003, 0.0003, 0.0015, 0.0012, 0.0011, 0.0011])

#Functions:
def Linear_fit(T, m, c): #linear fit function to use for the curve_fit function
    return m*T + c
def Expansion_coeff(m, L):
    return (1/L)*slope

popt, pcov = curve_fit(Linear_fit, T, L, p0=(1,0), sigma = yerr)
fiterr = np.sqrt(np.diag(pcov))
slope = popt[0]
errslope = fiterr[0]
intercept = popt[1]
errintercept = fiterr[1]

exp_coeff = Expansion_coeff(slope, intercept)
print(f"Linear Expansion Coefficient: {exp_coeff}")

#To visualise this data set, we can plot it
LFit = Linear_fit(T, slope, intercept) #This will generate our length data with fitted values for slope and intercept

plt.errorbar(T, L, yerr=np.array(yerr), fmt='ro', label="Data")
plt.plot(T, LFit, 'b-', label="chi-squared fit")
plt.legend(loc='upper left')
plt.xlabel("Temperature [\u2103]")
plt.ylabel("Length [m]")
plt.title("Linear Thermal Expansion using a chi-squared fit")
plt.minorticks_on()
plt.show()
plt.savefig("Curve_fit-thermal_expansion.pdf")