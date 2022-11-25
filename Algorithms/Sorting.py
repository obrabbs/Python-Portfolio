def Bubble_sort(L):
    '''
    Function to sort a list using the bubble sort method

    Parameters:
    L = unordered 1D list/array

    Returns:
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

def Insertion_sort(L):
    '''
    Function to sort a list using the insertion sort method

    Parameters:
    L = unordered 1D list/array

    Return:
    L = ordered 1D list/array
    '''
    for i in range(1, len(L)):
        #Current number taken out
        num = L[i]

        #Loop to move elements greater than num ahead one position
        j = i - 1
        while j >= 0 and num < L[j]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = num
    return L

#Exercise 1(a): Bubble Sort
#Test lists for bubble sort function
list1 = [4, 3, 2, 1]
print(f"Unordered list: {list1} \nOrdered List: {Bubble_sort(list1)}")
list2 = [10, 4, 55, 82, 93, 8]
print(f"Unordered list: {list2} \nOrdered List: {Bubble_sort(list2)}")
list3 = [1, 5, 22, 302, 10001]
print(f"Unordered list: {list3} \nOrdered List: {Bubble_sort(list3)}")

#Exercise 1(b): Insertion sort
#Test lists for insertion sort function
list1 = [10, 3, 8, 2, 5]
print(f"\nUnsorted list: {list1} \nInsertion sorted list: {Insertion_sort(list1)}")
list2 = [5, 4, 2, 3, 8, 201, 3021, 4, 30, 408, 790]
print(f"Unsorted list: {list2} \nInsertion sorted list: {Insertion_sort(list2)}")
list3 = [1, 3, 5, 7, 10]
print(f"Unsorted list: {list3} \nInsertion sorted list: {Insertion_sort(list3)}")
