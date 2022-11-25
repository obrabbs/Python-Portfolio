## Exercise 1: Sorting algorithms
(a) Sorting algorithms are used to organise numerical data in increasing order. 
Implement a Bubble Sort in Python and test it out on a few different lists of unsorted numbers.

(b) There are many other sorting algorithms, most of which are designed to be faster than Bubble Sort.

Once such alternative is called Insertion Sort. Here each number is taken out and inserted near the beginning in increasing order. 
Implement an Insertion Sort in Python and test it out on a few different lists of unsorted numbers.

## Exercise 2: Searching algorithms
Searching algorithms are used to locate specific elements of data in large data sets. 

(a) The simplest such algorithm is Linear Search. This simply the data set element by element until the search term is found (or not).

- Write a function which implements Linear Search
- Test it our using a few different lists of numbers

(b) For numerical data, a more efficient algorithm is called Binary Search. Here the numerical data is sorted in increasing order before the Binary Search algorithm is used. The algorithm uses a divide and conquer approach. It begins the search in the middle of the data structure. If it is not the middle element, it then infers that the number can only be on one half. If the search term is greater than the middle number, it must be in the second half of the data structure. Otherwise if it is lower than the middle value, then it can only be in the lower half. So one half can be ignored from the subsequent search. 

The algorithm simply repeats this process of comparing with middle value of the remaining half until the search is complete. 

- Write a function which implements binary search
- You may assume that the input list will be already sorted
- Hint: this function is often written recursively where the function calls itself!
- Test out a few different lists of numbers which are sorted by your earlier algorithm in Ex. 1

## Exercise 3: Missing number algorithms
Design and write an algorithm to determine the missing numbers in a 1D list of integers. The list contains integers from 1 to `L` where `L` is the length of the list.

Start with a solvable example:
$$
A = 
\begin{bmatrix}
4 & 3 & ? & 9 & ? & 7 & 2 & 5 & 8
\end{bmatrix}.
$$

Note that there are missing numbers located at `A[2]` and `A[4]`. For our purposes we can denote the missing number by `X` or zero `0`. Since `L=9`, we can deduce that the missing numbers are 1 and 6 in any order.

(a) Plan and write a function, `check1D`, that takes a list such as `A` as it's argument and returns the missing number(s).

(b) Plan and write another function, `check2D` which takes a 2D array as the argument and returns the missing number(s)

$$
B = 
\begin{bmatrix}
4 & 3 & 0 \\
9 & 6 & 7 \\
0 & 5 & 0
\end{bmatrix},
$$

where again a $0$ has replaced a missing element. We can construct 2D arrays using the Numpy module in Python.
