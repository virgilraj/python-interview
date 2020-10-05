
def find_index_replace_with_one_get_max_ones(arr):
    max_count = 0     # stores maximum number of 1's (including 0)
    max_index = -1    # stores index of 0 to be replaced

    prv_zero_index = -1  # stores index of previous zero
    count = 0            # store current count of zeros

    n = len(arr)

    for i in range(n):
        if(arr[i] == 1):
            count +=1
        else:
            # if current element is 0
			# reset count to 1 + no. of ones to the left of current 0
            count = i - prv_zero_index
            # update prev_zero_index to current index
            prv_zero_index = i
            
        if count > max_count:
            max_count = count
            max_index = prv_zero_index
    
    if max_index != -1:
        print("Index to be replaced is", max_index, max_count)
    else:
        print("Invalid input")

if __name__ == "__main__":
    A = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
    find_index_replace_with_one_get_max_ones(A)
