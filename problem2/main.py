
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
Tim Sort
params : ary - Input Array
         k - Insertion sort crossover point
'''
def TimSort(ary, k):
    if len(ary) <= 1:
        return ary

    if len(ary) <= k:
        return InsertionSort(ary , len(ary))

    med = len(ary) // 2
    ary1 = ary[:med]
    ary2 = ary[med:]

    ary1 = TimSort(ary1, k)
    ary2 = TimSort(ary2, k)

    return merge(ary, ary1, ary2)



if __name__ == "__main__":
    pass