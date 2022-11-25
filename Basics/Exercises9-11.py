#Exercise 9

#Libraries and Functions
import numpy as np
import pandas as pd

def Acceleration(m, v):
    '''
    Function to return the acceleration of a body in freefall with drag

    Parameters:
    m = mass
    v = velocity
    '''
    g = 9.81
    #Area, A, from height*width = 1.85*0.3
    A = 0.555
    rho = 1.225
    #Note that drag coeff cd = 1
    Fd = (v**2 * A * rho) / 2
    F = m * g - Fd
    return F/m


#Initial Conditions:
m = 75
a = [9.81]
y = [5500]
v = [0]
t = [0]
dt = 1

#Data:
for i in range(0,10):
    t.append(t[i] + dt)
    v.append(v[i] + a[i] * dt)
    y.append(y[i] - v[i] * dt)
    a.append(Acceleration(m, v[i + 1]))


#Part a:
#Create lists
t1 = ['%.1f' % elem for elem in t]
a = ['%.2f' % elem for elem in a]

dict = {'t [s]' : t1,
        '  a [m/s^2]' : a}
df = pd.DataFrame(dict)
print(df)

#Part b:
t2 = ['%.2f' % elem for elem in t]

dict = {'t [s]' : t2,
        'a [m/s^2]' : a}
df = pd.DataFrame(dict)
df.to_csv('Basics/Created-files/Freefall-with-drag.csv', index = False)

#Exercise 10

def Convert_list_to_string(s):
    '''
    Function to convert a list 's' of characters to a string
    '''
    new = ""
    for i in s:
        new += i
    return new

#Driver code:
file = open('Basics/Exercise-files/Mixed.txt')

rows = []
#Iteration to get all of the rows as lists of strings
for line in file.readlines():
    rows.append(line.split(' '))

nums = []
#Iteration to append all integers to nums
for item in rows:
    for j in item:
        j = Convert_list_to_string(j)
        if(j.isnumeric() == True):
            nums.append(int(j))

#Unsorted and Sorted Lists:
print(f"Unsorted list: \n{nums}")
sortedNums = sorted(nums)
print(f"Sorted List: \n{sortedNums}")

sortedList = []

#Save to .txt file with 5 characters:
file = open('Basics/Created-files/Sorted-numbers.txt', 'w')
for i in sortedNums:
    i = str(i)
    file.write("%5s\n" %i)
file.close()

#Exercise 11
#Libraries and Files:
import numpy as np

#Load .txt with arrays for each column
h, t1, t2, t3, t4, t5 = np.loadtxt('Basics/Exercise-files/FreefallData.txt', unpack='True')
tmean = np.zeros(len(h))
tstd = np.zeros(len(h))

#Mean and Standard Deviations for Repeat Time Measurements:
for i in range(len(h)):
    temp = [t1[i], t2[i], t3[i], t4[i], t5[i]]
    tmean[i] = np.mean(temp)
    tstd[i] = np.std(temp)

#Part a
#Saving all data using np.savetxt() with 3dp precision and headers for columns
np.savetxt('Basics/Created-files/Freefall_V2.txt', np.c_[h, t1, t2, t3, t4, t5, tmean, tstd], fmt='%.3f', delimiter = ', ', header = 'h, t1, t2, t3, t4, t5, mean time, std dev on fall time')

#Part b
#Saving subset of data [h, tmean, tstd] with 3dp precision and headers for columns
np.savetxt('Basics/Created-files/Freefall_V3.txt', np.c_[h, tmean, tstd], fmt='%.3f', delimiter=', ', header='h, mean fall time, std dev on fall time')