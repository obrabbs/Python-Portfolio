## Exercise 1: Using Matplotlib for 2D data visualisation

Adapting the code from Exercise 10, visualise $P(t)$ and $K(t)$ on the same graph, along with the total energy $E = P+K$. 
Set the x-axis from $t=0$ to $t=2v0/g$. 

- Use an arbitrary choice of $v_0$ and $m$
- Limit the y-axis to 1.3 times the maximum $y$-data
- Visualise with a suitable legend, labels and line styles 

## Exercise 2: Using Matplotlib for 3D data visualisation

The quantum wave function for a particle in a 2D box of side $L$ is:
$$
\psi_{n_xn_y}(x,y) = {2 \over L}\sin\left({n_x\pi x \over L}\right)
\sin\left({n_y\pi y \over L}\right)
$$

For the state where $n_{x} =1$ and $n_y = 2$:

1. Visualise $\psi_{n_xn_y}$ as:

    - a 3d plot 
    
    - a 2d contour plot
    
    - set $L=1$ and $x,y$ to range from $0\rightarrow1$ inclusive
    
2. Repeat this for the probability of the wave function $\psi_{n_xn_y}^2 $   

3. Visualise 1D cross section (i.e. a line-out) on the same graph:

    - along $x=0.5$ of the wavefunction    
    
    - along $x=0.5$ of the probability function
    
4. Label and format all graphs accordingly
5. Save the graphs as pdfs and minimise the white space around the graphs.

## Exercise 3: Using Scipy for data analysis

Using the curve_fit function from Scipy, perform a linear regression analysis of the thermal expansion i.e. length as a function of temperature:

- use a chi-squared $\chi^2$ method including the error on the mean fall time
    - determine the linear expansion coefficient 
- visualise measurements and analysis results on a 2d plot
    - time error bars is the error on the mean length
- Label, format and save the graph accordingly
    - for example ensure $\chi^2$ is stated in the analysis legend
    - Add minor ticks to this graph

## Exercise 4 
(a) Generate a 1D array of 10 random integers from 1-20 inclusive. Prompt the user to guess an integer from within this list. Now check if they guessed correctly and print so to screen with the message "Are you lucky? =" with a result *True* or *False*. 

(b) Iterate through this 1D array using a for-loop. For each number in the array, check if it is odd or even and print this to screen.

## Exercise 5: Heaviside function
(a) 
The following "step" function is known as the Heaviside function 
$$
H(x)= 
\begin{cases}
    0,& x < 0\\
    1,& x \ge 0
\end{cases}
$$
and is widely used in mathematics.

Implement $H(x)$ as a Python function *heavy(x)* using a if-else loop.

Test your implementation for $x = -\frac{1}{2}, 0, 10$.

(b)
It is in many numerical applications advantageous to work with
a smooth version of the Heaviside function where the function itself
and its first derivative are continuous. One such smoothed Heaviside function is
$$
    H_\epsilon(x)= 
\begin{cases}
    0,& x < -\epsilon\\
    \frac{1}{2}+  \frac{x}{2\epsilon} +  \frac{1}{2\pi}\sin(\frac{\pi x}{\epsilon}), & -\epsilon \le x \le \epsilon \\
    1,& x > \epsilon
\end{cases}
$$
Where $\epsilon\approx 0$. Implement this function as a Python fucntion *heavysmooth(x)*.

Test your implementation for $x = -1, -0.001, 0.001, 1$ using $\epsilon=0.1$

(c) Use a for-loop to calculate both functions for 200 values of $x$ in the range $-1\le x \ge 1$ . Visualise both functions using this data. Include minor ticks/label and save the plot as appropiate.

## Exercise 6: Free fall with drag
(a) As per the [video lecture](https://www.youtube.com/watch?v=qRP_yxmnddA&list=PLdy_4e1GvNG0MMc86Y7cWRb8kjS2SUhpY&index=11&t=1415s), add a drag component to our numerical free fall model. The sky driver here has mass $m=75$kg, height 1.85m and width 0.3m with a drag coefficient $c_d=1$. The starting altitude is $y_0=5500$m and the air density is $\rho = 1.225$ kg/m$^2$. Set the time step $dt = 0.1$s.

- Implement this using a while-loop
- Visualise the sky-diver's:
    - absolute velocity as a function of time
    - height as a function of time
        - on a double y plot
- Print to screen, rounded to 1 decimal place:
    - the terminal velocity
    - the fall time (i.e how long did it take to reach the ground)

(b) Investigate the dependence of the terminal velocity with mass. 

- Vary mass from 1g to 100kg
- Keep all other parameters fixed as before
- Implement this using a nested for-loop (i.e. not a while loop)
- Visualise the results. Set minor ticks and font size=14.