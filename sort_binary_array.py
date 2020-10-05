#Sort binary array in linear time O(n)
#1.Right and left pointer to == 0
#2.Loop right < array length
#2.Right pointer move first
#3.if  zero element found the swap with left
#4.Increment left and right
#5 if non zero found - increment right
def binary_array_sort(arr):
    n = len(arr)
    right = 0 
    left = 0

    while(right < n):
        if(arr[right] == 1):
            right +=1
        else:
            arr[right],arr[left] = arr[left],arr[right] 
            right +=1
            left +=1

if __name__ == "__main__":
    
    arr = [ 1, 0, 0, 0, 1, 0, 1, 1 ]
    binary_array_sort(arr)
    print(arr)
    