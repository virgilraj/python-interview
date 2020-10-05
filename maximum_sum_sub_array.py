import sys

def maximum_sum_sub_array(arr):
    n = len(arr)
    max_so_far = (-1) * sys.maxsize
    max_here = 0

    for i in range(n):
        max_here += arr[i]
        if(arr[i] > max_here):
             max_here = arr[i]
        if(max_here > max_so_far):
            max_so_far = max_here
    
    print(max_so_far)


if __name__ == "__main__":
    arr = [ -2, -1, -3,  4, -1, 2,1, -5, 4]
    maximum_sum_sub_array(arr)