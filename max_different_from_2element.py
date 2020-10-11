def max_difference(arr):
    n = len(arr)
    diff = 0

    for i in range(n-1):
        for j in range(i+1, n):
            diff = max(diff, abs(arr[j]-arr[i]))
    
    print("Max differenc" , diff)

def max_difference_kadence(arr):
    diff = 0 
    minval = float('inf')
    max_so_far = float('-inf')
    maxval = float('-inf')
    n = len(arr)

    #for i in reversed(range(n-1)):
    for i in range(n):
        # update max if current element is greater than the maximum element
        if(arr[i] > max_so_far):
            max_so_far = arr[i]
        # if the current element is less than the maximum element,
		# then update the difference if required
            print(i, max_so_far)
        else:
            diff = max(diff, abs(max_so_far - arr[i]))

        
        minval = min(minval, arr[i])
        maxval = max(maxval, arr[i])


    print("Diff", diff, maxval - minval)

        

if __name__ == "__main__":
    A = [2, 7, 9, 5, 1, 3, 5, 12]
    max_difference(A)
    max_difference_kadence(A)