def Check_1D(N):
    '''
    Procedure to print the missing numbers in a 1D list/array, which has elements from 1 to the 
    length of the list with 'x' for missing numbers (i.e. [1, 2, 3, 4, 'x'], where x would be 5)
    
    Parameters:
    N = 1D list/array of the form described above

    Output:
    numsMissing = missing numbers in N
    '''
    L = len(N)
    numsMissing = []
    for i in N:
        if(i == 'x'):
            for j in range(1, L+1):
                if(j in N):
                    continue
                else:
                    numsMissing.append(j)
    #Remove duplicates using in-built set() function
    numsMissing = list(set(numsMissing))
    print(f"Missing number(s): {numsMissing}")

def Num_elements(N):
    '''
    Function to compute the number of elements in a 2D list/array
    '''
    L=0
    for row in N:
        L += len(row)
    return L

def Check_2D(N):
    '''
    Procedure to print the missing numbers in a 2D list/array, which has elements from 1 to the 
    length of the list with 'x' for missing numbers (i.e. [1, 2, 3, 4, 'x'], where x would be 5)
    
    Parameters:
    N = 1D list/array of the form described above

    Output:
    numsMissing = missing numbers in N
    '''
    numMax = Num_elements(N) + 1
    numsMissing = []
    for row in N:
        for i in row:
            if(i == 'x'):
                for j in range(1, numMax):
                    if(any(j in k for k in N)):
                        continue
                    else:
                        numsMissing.append(j)
    #Remove duplicates using in-built set() function
    numsMissing = list(set(numsMissing))
    print(f"Missing number(s): {numsMissing}")
        
#Exercise 3(a): Missing number in 1D list/array
#Test for 1 missing number
list1 = [2, 5, 7, 3, 'x', 1, 4, 9, 6]
Check_1D(list1)
#Test for 2 missing numbers
list2 = ['x', 2, 'x', 4, 1]
Check_1D(list2)

#Exercise 3(b): Missing number in 2D list/array
#Test for 2x2 matrix with 2 missing numbers (one in each row)
list1 = [[3, 'x'],['x', 1]]
Check_2D(list1)
#Test for 3x3 matrix with 4 missing numbers
list2 = [[6, 'x', 9],['x', 'x', 1],[5, 3, 'x']]
Check_2D(list2)
#Test for 2x3 matrix with 3 missing numbers
list3 = [[3, 'x', 'x'], ['x', 1, 6]]
Check_2D(list3)