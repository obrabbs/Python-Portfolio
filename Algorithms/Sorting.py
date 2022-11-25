#Exercise 1(a): Bubble Sort

def Bubble_sort(L):
    '''
    Function to sort a list using the bubble sort method

    Parameters:
    L = unordered 1D list/array

    Return:
    L = ordered 1D list/array
    '''
    for i in range(len(L)):
        swap = 0
        for j in range(len(L) - 1 - i):
            if(L[j] > L[j+1]):
                L[j], L[j+1] = L[j+1], L[j]
                swap = 1
        if(swap == 0): break
    return L

#Test lists for bubble sort function
list1 = [4, 3, 2, 1]
print(f"Unordered list: {list1} \nOrdered List: {Bubble_sort(list1)}")
list2 = [10, 4, 55, 82, 93, 8]
print(f"Unordered list: {list2} \nOrdered List: {Bubble_sort(list2)}")
list3 = [1, 5, 22, 302, 10001]
print(f"Unordered list: {list3} \nOrdered List: {Bubble_sort(list3)}")
    
