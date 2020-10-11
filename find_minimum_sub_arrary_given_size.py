import sys

def find_minimum_sub_array_given_size(arr, k):

    minval = sys.maxsize
    maxval = float('-inf')
    sum = 0
    last = 0
    for i in range(len(arr)):

        sum += arr[i]
        if(i+1 >= k):
            
            if(sum < minval):
                minval = sum
                last = i
            maxval = max(sum, maxval)
            sum -= arr[i+1-k]
    print("Minimum sub array", arr[last-k+1:last+1])
    print ("Max value", maxval)



if __name__ == "__main__":
    #arr = [10, 4, 2, 5, 6, 3, 8, 1]
    arr = [1,2,4,5,3]
    k = 3
    find_minimum_sub_array_given_size(arr, k)   