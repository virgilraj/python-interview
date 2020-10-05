# Function to find maximum sum path in two given lists
# Below code is similar to merge routine of mergesort algorithm

def maxSum(X, Y):
    sum = sum_x = sum_y = 0

    m = len(X)
    n = len(Y)

    # i and j denotes current not index of X and Y respectively
    i = j = 0

    # loop till X and Y are empty
    while i < m and j < n:

        # to handle duplicate elements in X
        while i < m-1 and X[i] == X[i+1]:
            sum_x += X[i]
            i = i + 1

        # to handle duplicate elements in Y
        while j < n-1 and Y[j] == Y[j+1]:
            sum_y += Y[j]
            j = j + 1

        # if current element of Y is less than current element of X
        if Y[j] < X[i]:
            sum_y += Y[j]
            j = j + 1

        # if current element of X is less than current element of Y
        elif X[i] < Y[j]:
            sum_x += X[i]
            i = i + 1

        else: # if X[i] == Y[j]:
            # consider maximum sum and include value of current cell
            sum += max(sum_x, sum_y) + X[i]

            # move both indices by 1 position
            i = i + 1
            j = j + 1

            # reset both sums
            sum_x = 0
            sum_y = 0

    # process remaining elements of X (if any)
    while i < m:
        sum_x += X[i]
        i = i + 1

    # process remaining elements of Y (if any)
    while j < n:
        sum_y += Y[j]
        j = j + 1

    sum += max(sum_x, sum_y)


    print("Maximum sum is ", sum )

if __name__ == "__main__":
    X = [3, 6, 7, 8, 10, 12, 15, 18, 100]
    Y = [1, 2, 3, 5, 7, 9, 10, 11, 15, 16, 18, 25, 50]
    maxSum(X,Y)