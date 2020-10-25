def brute_force(arr, sum):
    n = len(arr)
    max_len =0
    for i in range(n):
        newsum = 0
        for j in range(i,n):
            newsum += arr[j]
            if(newsum == sum ):
                print("brute_force Sum found at index ", i, j )
                max_len = max(max_len, j-i)

    print("max length ", max_len)

#Dictionary approach

def findSum(arr, sum):
    so_far_sum = {}
    n = len(arr)
    so_far = 0
    so_far_sum[0]=[0]
    max_len = 0
    min_len = float('inf')
    for i in range(n):
        so_far += arr[i]

        if (so_far - sum) in so_far_sum.keys():
            print(" Sum found at index ", so_far_sum[so_far - sum], i )
            temp = so_far_sum[so_far - sum]
            for j in temp:
                max_len = max(max_len, i-j)
                min_len = min(min_len, i-j)

        if so_far not in so_far_sum:
            temp = []
            temp.append(i+1)
            so_far_sum[so_far] = temp
        else:
            so_far_sum[so_far].append(i+1)

    print("Max length", max_len)
    print("Min length", min_len)

#other approach -- not 
def other_approach(A, sum):
    # maintains sum of current window
	windowSum = 0

	# maintain a window [low, high-1]
	(low, high) = (0, 0)

	# consider every sublist starting from low index
	for low in range(len(A)):

		# if current window's sum is less than the given sum,
		# then add elements to current window from right
		while windowSum < sum and high < len(A):
			windowSum += A[high]
			high = high + 1

		# if current window's sum is equal to the given sum
		if windowSum == sum:
			print("Sublist found", (low, high - 1))
			#return

		# At this point the current window's sum is more than the given sum
		# remove current element (leftmost element) from the window
		windowSum -= A[low]

if __name__ == "__main__":
    #arr = [ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 ]
    arr = [ 3, 4, 7, 2,  5, -3 ]
    #brute_force(arr, 4)
    findSum(arr,7)
    other_approach(arr,7)
    