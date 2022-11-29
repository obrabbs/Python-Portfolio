def Linear_search(N, num):
    '''
    Linear search procedure

    Parameters:
        N = 1D list or array
        num = number to search for

    Outputs:
        If N contains num, procedure outputs "{num} is at index {i}"
        If N doesn't contain num, procedure outputs "{num} is not in list"
    '''
    for i in range(len(N)):
        if(num == N[i]):
            print(f"{num} is at index {i}")
            break
        elif(i == len(N)-1):
             print(f"{num} is not in list")
        else:
            continue

def Binary_search(N, num, high, low=0):
    '''
    Binary search procedure

    Parameters:
        N = 1D list or array
        num = number to search for
        high = index of higher limit in N
        low = index of lower limit in N (default = 0)

    Outputs:
        If N contains num, the function returns the index of num in N
        If N doesn't contain num, the function returns -1
    '''
    midIndex = (high+low)//2
    if(high >= low):
        if(num == N[midIndex]):
            return midIndex
        elif(num > N[midIndex]):
            return Binary_search(N, num, low=midIndex+1, high=high)
        else:
            return Binary_search(N, num, low=low, high=midIndex-1)
    else:
        return -1

#Exercise 2(a): Linear Search
#Test for a number in list
list1 = [0, 1, 4, 2, 3, 8, 10]
Linear_search(list1, 4)
#Test for a number not in list
list2 = [6, 20, 53, 10, 9, 23, 87]
Linear_search(list2, 5)

#Exercise 2(b): Binary Search
#Test for a number at the middle of list
list1 = [4, 5, 20, 83, 92]
numSearched = 20
result = Binary_search(list1, numSearched, high=len(list1)-1)
if(result == -1):
    print(f"{numSearched} not in list")
else:
    print(f"{numSearched} is at index {result}")
#Test for a number below the middle of list
list2 = [10, 12, 30, 38, 47]
numSearched = 12
result = Binary_search(list2, numSearched, high=len(list2)-1)
if(result == -1):
    print(f"{numSearched} not in list")
else:
    print(f"{numSearched} is at index {result}")
#Test for a number above the middle of list
list3 = [8, 12, 14, 17, 18, 22, 53]
numSearched = 22
result = Binary_search(list3, numSearched, high=len(list3)-1)
if(result == -1):
    print(f"{numSearched} not in list")
else:
    print(f"{numSearched} is at index {result}")
#Test for a number not in list
list4 = [7, 16, 19, 32, 43, 52, 89]
numSearched = 5
result = Binary_search(list4, numSearched, high=len(list4)-1)
if(result == -1):
    print(f"{numSearched} not in list")
else:
    print(f"{numSearched} is at index {result}")