def find_longest_bitonic(arr):
    n = len(arr)
    I = [1] * n
    D = [1] * n

    # Add incement index in to I -- left to Right
    I[0] = 1
    for i in range(1,n):
        if(arr[i-1] < arr[i]):
            I[i] = I[i-1] +1

    # Add decrement index in to D -- Right to left
    D[n-1] = 1
    for i in reversed(range(n-1)):
        if(arr[i+1] < arr[i]):
            D[i] = D[i+1] +1
    
    print(I)
    print(D)

    lbs_len = 1
    beg = 0
    end =0
    for i in range(n):
        if(lbs_len < I[i] + D[i] - 1):
            lbs_len = I[i] + D[i] -1
            beg = i - I[i] + 1
            end = i + D[i] - 1

            print(i, lbs_len, beg,end)
    print("Bitonic sub array")
    #print("[%d, %d]", beg,end)
    for i in range(beg, end):
        print(arr[i], end =" ")  

#Approach 2
def findBitonicSublist(arr):
    n = len(arr)
    end_index = 0
    max_len = 0

    i = 0
    while(i+1 < n-1):
        # check for Longest Bitonic Sublist starting at A[i]

		# reset length to 1
        length = 1
        # run till sequence is increasing
        while(i+1 < n and arr[i+1] > arr[i]):
            i += 1
            length += 1
        
        # run till sequence is decreasing
        while(i+1 < n and arr[i+1] < arr[i]):
            i += 1
            length += 1
        
        if(length > max_len):
            max_len = length
            end_index = i
        
    print("The length of longest bitonic sublist is", max_len)

    print("The longest bitonic sublist is", (end_index - max_len) +1 , end_index)
    for i in range((end_index - max_len) +1, end_index):
        print(arr[i], end =" ") 
        

if __name__ == "__main__":
    A = [3, 5, 8, 4, 5, 9, 10, 8, 5, 3, 4]
    find_longest_bitonic(A)
    findBitonicSublist(A)
