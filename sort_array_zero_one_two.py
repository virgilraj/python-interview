
#maintain 3 pointers 
#left, right, middle
#move the middle
#if 0 then swap with middle and increase left and middle
#if 1 increase middle
#if 2 swap with right and increment middle and decreement right
def longest_sub_with_zeroandone(arr, pivot):
    n = len(arr)
    low = 0
    medium = 0
    high = n-1
    #pivot = 1
    while(medium <= high):
        if(arr[medium] < pivot):
            arr[low], arr[medium] = arr[medium], arr[low]
            low = low + 1
            medium = medium + 1
        elif(arr[medium] > pivot):
            arr[high], arr[medium] = arr[medium], arr[high]
            high = high - 1
        else:
            medium = medium + 1

    print("Sorted Array ", arr)

if __name__ == "__main__":
    arr = [ 0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0 ]
    arr = [ 0,10,-2,4,-6,7,-3,0 ]
    pivot = 0
    longest_sub_with_zeroandone(arr,pivot)