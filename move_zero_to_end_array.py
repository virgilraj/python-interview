#Move all zeros present in an array to the end
#Simple approach O(nlogn)
#Move all non zero to right then all end elements to zero

def move_zero_to_end_array(arr):
    n = len(arr)
    k = 0
    for i in range(n):
        if arr[i] != 0:
            arr[k] = arr[i]
            k +=1
    for i in range(k,n):
        arr[i] = 0
    
    print(arr)

#Sliding window
#Right and left pointer
#Right pointer move first
#if non zero element found the swap with left
#Increment left and right
#if zero found - increment right
def move_zero_to_end_array_sliding(arr):
    n = len(arr)
    left = 0
    right = 0
    while(right < n):
        if(arr[right] != 0):
            arr[right],arr[left] = arr[left], arr[right]
            print(arr)
            left +=1
        right +=1
    print(arr)

if __name__ == "__main__":
    arr = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    #move_zero_to_end_array(arr)
    move_zero_to_end_array_sliding(arr)