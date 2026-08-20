'''
Josiah Cleveland
Homework 1.1
BSSD 3410 (Applied Algorithms & Architecture)
19 August 2026

We want to compare the two search algorithms by adding a counter
for each number of operations and a timer to calculate how long
each search takes

Generate an array of 200 random integers instead of the hardcoded
arr and rerun your program. You probably want to remove the print
statements for the number of operations. You can use random.sample
as described at the link below or use a for loop and random.randint
as described at the same link.
'''

#Step 3.1 of the comparison is to import timeit library
import timeit

#Step 4.1: import random
import random

#===============================================================
#Step 1.1 is to add python3 code to linearly search x in arr[]
#if x is present, then return its location, otherwise returns -1
def search(arr, n, x):

    #Step 2: add operation counters throughout
    #here is a variable for an operations counter:
    # operations = 0
    for i in range(0, n):
        #adds one to operations variable
        # operations += 1
        if (arr[i] == x):
            # print("linear ops:", operations)
            return i
    # print("LINEAR OPS:", operations)
    return -1

#===============================================================
#Step 1.2 is to add python3 code to implement iterative binary
#search, and it returns location of x in given array arr if
#present, otherwise returns -1
def binarySearch(arr, l, r, x):

    #Step 2: add operation counters throughout
    #here is a variable for an operations counter:
    # operations = 0
    while l <= r:
        #adds one to operations variable
        # operations += 1
        mid = l + (r - l) // 2
        #check if x is present at mid
        if arr[mid] == x:
            # print("binary ops:", operations)
            return mid

        #if x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        #if x is smaller, ignore right half
        else:
            r = mid - 1

    #if we reach here, then the element was not present
    # print("BINARY OPS:", operations)
    return -1


#===============================================================
#Step 3.2: give main an explicit __name__ check
if __name__ == "__main__":

#Step 1.3 is to add driver code
    #Step 4.2 is to use random.sample
    arr = random.sample(range(1000), k=200)
    x = 10
    n = len(arr)
    print("random array:", arr, "\narray length: ", n)

#Step 3.3: add new implementation of timeit library
    iter = 10
    ltime = timeit.timeit(lambda:search(arr, n, x),\
                          setup="from __main__ import search",\
                          number=iter)
    btime = timeit.timeit(lambda:binarySearch(arr, 0, len(arr)-1, x),\
                          setup="from __main__ import binarySearch",\
                          number=iter)
    print("Linear search took:", ltime)
    print("Binary search took:", btime)

'''
    #using Linear Search:
    result = search(arr, n, x)
    if (result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

    #using Iterative Binary Search:
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
'''
