# in-place merge two sorted lists X and Y
# invariant: X and Y are sorted at any point
def merge_two_sorted_array(X, Y):
    m = len(X)
    n = len(Y)

    # consider each element X[i] of list X and ignore the element
	# if it is already in correct order else swap it with next smaller
	# element which happens to be first element of Y

    for i in range(m):
        if(X[i] > Y[0]):
            #Swap
            X[i], Y[0] =  Y[0], X[i]

            first = Y[0]

            # move Y[0] to its correct position to maintain sorted
			# order of Y. Note: Y[1..n-1] is already sorted
            k = 1
            while(k < n and Y[k] < first):
                Y[k-1] = Y[k]
                k = k +1
            Y[k-1] = first




if __name__ == "__main__":
    X = [1, 4, 7, 8, 10]
    Y = [2, 3, 9 ]
    merge_two_sorted_array(X,Y)
    print("X:", X)
    print("Y:", Y)