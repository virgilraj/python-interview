
def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start

    for i in range(start,end):
        if(arr[i] <= pivot):
            #swap(arr, i, pIndex)
            arr[i],arr[pIndex] = arr[pIndex],arr[i]
            pIndex = pIndex +1
    
    #swap(arr,pIndex, end)
    arr[end],arr[pIndex] = arr[pIndex],arr[end]
    return pIndex

def swap(arr,start, end ):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

def QuickSort_Recursive(arr, start, end):
    
    if(start < end):
        pindex = partition(arr, start, end)
        #left side
        QuickSort_Recursive(arr, start, pindex-1)
        #right side
        QuickSort_Recursive(arr, pindex+1, end)

if __name__ == "__main__":
    arr = [3,4,6,3,8,5,7]
    QuickSort_Recursive(arr, 0, len(arr)-1)

    print(arr)
