import sys

def minimum_sum_sub_array(arr):
    n = len(arr)
    min_so_far =  sys.maxsize
    min_here = 0

    for i in range(n):
        min_here += arr[i]
        if(arr[i] < min_here):
             min_here = arr[i]
        if(min_here < min_so_far):
            min_so_far = min_here
    
    print(min_so_far)


if __name__ == "__main__":
    arr = [ -2, -1, -13,  4, -1, 2,1, -5, 4]
    minimum_sum_sub_array(arr)