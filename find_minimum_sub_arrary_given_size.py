import sys

def find_minimum_sub_array_given_size(arr, k):

    minval = sys.maxsize
    sum = 0
    last = 0
    for i in range(len(arr)):

        sum += arr[i]

        if(i+1 > k):
            
            if(sum < minval):
                minval = sum
                last = i
            sum -= arr[i+1-k]
    print("Minimum sub array", arr[last-k+1:last+1])



if __name__ == "__main__":
    arr = [10, 4, 2, 5, 6, 3, 8, 1]
    k = 3
    find_minimum_sub_array_given_size(arr, k)   