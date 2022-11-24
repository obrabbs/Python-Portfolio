## Exercise 1a: Hello World!
For your traditional first programme, print "Hello World" to the screen.

## Exercise 1b: Simple arithmetic

Besides the basic operators (+, -) you can use $A*B$ for multiplication and $A**B$ for $A^B$.

a) Calculate $5^2$, $\sqrt{25}$ using the $A**B$ syntax

b) Calculate: $ (5 + (5^2 - 4\times8\times3))/ (2 \times 8)$

c) Now write a short Python programme to solve quadratic equations:
$$
ax^2 + bx + c = 0
$$
i.e print the values of x when the equation = 0.

Do you remember the roots of quadratic equation formula? 

Solve for

1. a = 47.2, b = -148.1, c = 72.6
2. a = -19, b = 67, c = 82

## Exercise 2: Create a computer survey

Create a simple computer survey, asking the user at least 4 questions including their *age*.

Your programme should print a single line summarising the answers phrased in a readable sentence.

Also print a statement comparing the participants age with the UK median age of 40.5 years. For example: "Your age is -11.5 years off the UK median of 40.5 years".

## Exercise 3: Calculate a series expansion
The series expansion for cos(x) can be written as:

$$\cos(x) = \large{\large{\sum_{n=0}^{\infty} (-1)^{n} \frac{x^{2n}}{(2n)!}=1-\frac{x^{2}}{2!}+\frac{x^{4}}{4!}-\frac{x^{6}}{6!}+...}}$$

Write a Python programme that compares the value of cos(x) calculated with the first 4 terms of the series expansion above to that returned by `numpy.cos(x)`. 
- Your script should prompt the user for a value of x (in degrees) 
- Print both values of cos(x), their absolute difference and the percentage difference (relative to the value of `numpy.cos(x)`) to the screen

## Exercise 4: Start by creating a simple function to say Hello!
This function should take an string input of a name and print a string 'Hello name'

Prompt the use for their name.

## Exercise 5: Boiling an egg

As an egg cooks, the proteins first denature and then coagulate. When the temperature exceeds a critical point, reactions begin and proceed faster as the temperature increases. In the egg white the proteins start to coagulate for temperatures above 63 C, while in the yolk the proteins start to coagulate for temperatures above 70 C. For a soft boiled egg, the white needs to have been heated long enough to coagulate at a temperature above 63 C, but the yolk should not be heated above 70 C. For a hard boiled egg, the center of the yolk should be allowed to reach 70 C.

The following formula expresses the time $t$ it takes (in seconds) for the center of the yolk to reach the temperature $T_y$ (in Celsius degrees):

$$
t = \frac{M^{2/3}c \rho^{1/3}}{K\pi^2(4\pi/3)^{2/3}}\ln [0.76\frac{T_o - T_w}{T_y - Tw}]
$$

Here, $M$ , $\rho$, $c$, and $K$ are properties of the egg: $M$ is the mass, $ρ$ is the density, $c$ is the specific heat capacity, and $K$ is thermal conductivity. Relevant values are $M$ = 47 g for a small egg and $M$ = 67 g for a large egg, $\rho$ = 1.038 g cm$^{−3}$ , $c$ = 3.7 J g$^{−1}$ K$^{−1}$ , and $K = 5.4\times 10^{-3}$ W cm$^{−1}$ K$^{−1}$ . Furthermore, $T_w$ is the temperature of the boiling water, and $T_o$ is the original temperature of the egg before being put in the water. 


- Write a function to return $t$($M$, $T_0$, $T_y$). Constants should be declared in the function as local variables.

- Set $T_w = 100$ C and $T_y = 70$ C, and compute $t$ in minutes for:
    - a large egg taken from the fridge ($T_o = 4$ C) and from room temperature ($T_o = 20^{\circ}$ C)
    - a small egg taken from the fridge ($T_o = 4$ C) and from room temperature ($T_o = 20^{\circ}$ C)
- compare the differences in cooking time between large and small eggs for otherwise matching initial conditions

## Exercise 6: create and load a module
Create a python script (.py file) and therein create at least 2 functions.

Next create a simple Python programme which imports this new module and calls the functions in some way. 

## Exercise 7: Formatting and Writing Data

(a) Calculate and print to screen a table of data

Calculate data for time, $t$, and acceleration, $a$, for the sky diver in Exercise 14 using $dt=0.01$s.

- Print $t$ and $a$ at 1 second intervals starting at $t=0$ until $t=10$s

- Format the values as floats: 

    - $t$: 1 decimal places of precision and 5 characters in length
    
    - $a$: 2 decimal places of precision and 5 characters in length
    
- Also display a header of t[s] and a[m/s$^2$] above the data, where each is a separate string having 6 and 8 characters of length respectively

## Exercise 8: Reading Data from Files

Load the data from the file: 'Mixed.txt'

- Process this data to select only the numerical data (i.e. integers)

- Sort these numbers in incresing order. Find a built-in Python function for sorting numbers. 

- Save the sorted integer data to a text file. Ensure the individual numbes are saved with the same length e.g. 5 characters long.

## Exercise 9: Saving Data with Numpy

Use the free fall data to test out numpy's *loadtxt* and *savetxt* functions:

- Load the data from "FreefallData.txt"

- Calculate the mean & standard deviations of the repeat time measurements

    - Use an efficient loop for the calculations
    
- Save the new data:

    - Freefall_V2.txt: 
    
        - Save all the data as columns
        
        - Height t1 t2 t3 t4 t5 tmean tstd
        
    - Freefall_V3.txt:
    
        - Save a subset of the data
        
        - 3 columns of height, mean time, standard deviation of fall time
        
    - Save data with 3 decimal places of precision and in base SI units (i.e. [m] and [s])
    
    - Add a useful header to the data files to describe the columns