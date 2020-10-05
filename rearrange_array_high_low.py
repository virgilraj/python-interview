#Rearrange an array with alternate high and low elements
#Approach 1 = Move 2 element at a time
#Check left element greater than current then swap 
#Check right element less than current then swap

def rearrange(arr):
    n = len(arr)
    for i in range(1, n, 2):
        if(arr[i] < arr[i-1]):
            arr[i],arr[i-1] = arr[i-1],arr[i]
        if(arr[i] < arr[i+1]):
            arr[i],arr[i+1] = arr[i+1],arr[i]
    
    print(arr)

if __name__ == "__main__":
    arr = [9, 6, 8, 3, 7]
    rearrange(arr)
    