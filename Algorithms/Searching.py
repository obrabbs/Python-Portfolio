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

#Test for a number in list
list1 = [0, 1, 4, 2, 3, 8, 10]
Linear_search(list1, 4)
#Test for a number not in list
list2 = [6, 20, 53, 10, 9, 23, 87]
Linear_search(list1, 5)

