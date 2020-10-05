#Step 1 : Traverse left -> right , keep the maximium so far
#step 2 : if max so far less than current ele then note that Right index
#Step 3 : Traverse right --> left, keep minmimum so_far
#Step 4: if min so far greater than current then note the lefer Index 

def largest_sublist_make_sorted(arr):
    rightIndex, leftIndex = 0,0
    max_so_far = float('-inf')
    min_so_far = float('inf')

    for i in range(len(arr)):
        if arr[i] > max_so_far:
            max_so_far = arr[i]
        if arr[i] < max_so_far:
            rightIndex = i

    for i in reversed(range(len(arr))):    
        if arr[i] < min_so_far:
            min_so_far = arr[i]
        
        if arr[i] > min_so_far:
            leftIndex = i

    print("Sort list from index ", leftIndex, " to ", rightIndex)

if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5, 6, 4, 8]
    largest_sublist_make_sorted(arr)