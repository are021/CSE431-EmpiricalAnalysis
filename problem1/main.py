import numpy as np
import random
import timeit

'''
Generate A Random Array of Size n
'''
def GenerateRandomArray(n):
    return random.sample(range(100), n)


'''
Generate Nearly Sorted Array
'''
def GenerateNearlySorted(n):
    res = GenerateRandomArray(n)
    res.sort()
    #Randomize one of the values
    rand_index = random.randint(0, n - 1)
    res[rand_index] = res[rand_index] + random.randint(21, 100)

    return res

'''
Generate a Reverse Order Array
'''
def GenerateReverseArray(n):
    res = GenerateRandomArray(n)
    res.sort(reverse=True)
    return res

'''
Insertion Sort
Reference : https://www.geeksforgeeks.org/insertion-sort/
'''
def InsertionSort(ary, n):
    
    for i in range(1, n):
        curr = ary[i]
        j = i - 1

        while j >= 0 and curr < ary[j]:
            ary[j + 1] = ary[j]
            j -= 1
        
        ary[j + 1] = curr

'''
Merge Function
'''
def merge(res,left, right):
    i,j,k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res[k] = left[i]
            i += 1
        else:
            res[k] = right[j]
            j += 1
        
        k += 1
    
    #Add in Remaining Elements
    while i < len(left):
        res[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        res[k] = right[j]
        j += 1
        k += 1
    
    return res




'''
Merge Sort
Reference : 
'''
def MergeSort(ary):
    if len(ary) <= 1:
        return ary

    med = len(ary) // 2
    ary1 = ary[:med]
    ary2 = ary[med:]

    ary1 = MergeSort(ary1)
    ary2 = MergeSort(ary2)

    return merge(ary, ary1, ary2)





if __name__ == "__main__":
    pass
    print(timeit.repeat(
        
    ))




