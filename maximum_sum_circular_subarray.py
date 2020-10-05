#1. Find minimum sum of sub array
#2. Find sum of all elements
#minus 2 - 1
#edge case if all minus value then get the max value

def find_sum_of_circular_array(arr):
    n = len(arr)
    min_here = 0
    min_so_far = float('inf')
    max_value = float('-inf')
    sum = 0

    for i in range(n):
        sum += arr[i]

        min_here += arr[i]
        if arr[i] < min_here:
            min_here = arr[i]
        if min_here < min_so_far:
            min_so_far = min_here
        
        max_value = max(max_value, arr[i])
    
    print("Sum, min sub array, sum of circular subarray", sum, min_so_far, sum - (min_so_far))
    print("Max value", max_value)

if __name__ == "__main__":
    #arr = [5,3,2,4,1]
    arr = [5,-3,-2,6,-1,4]
    #arr = [-5,-3,-2,-6,-1,-4]
    find_sum_of_circular_array(arr)