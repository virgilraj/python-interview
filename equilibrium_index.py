
def equilibrium_index(arr):

    n= len(arr)
    left = [0] * n
    left[0] = 0
    right = 0

    # left[i] stores sum of elements of sub-list A[0..i-1]
    for i in range(1,n):
        left[i] = left[i-1] + arr[i-1]
    
    # traverse list from right to left
    for i in reversed(range(n)):

        """ if sum of elements of sub-list A[0..i-1] is equal to:
			the sum of elements of sub-list A[i+1..n) i.e.
			(A[0] + .. + A[i-1]) = (A[i+1] + A[i+2] + .. + A[n-1]) """

        if(left[i] == right):
            print("equilibrium_index", i)
        right +=arr[i]

def equilibrium_index_approach(arr):
    n = len(arr)
    for i in range(1, n):
        left = 0
        right = 0
        l = i - 1
        r = i + 1
        while(l >= 0):
            left +=arr[l]
            l -=1
        while(r < n):
            right += arr[r]
            r +=1
        if(left == right):
            print("equilibrium ", i)


if __name__ == "__main__":
    A = [0, -3, 5, -4, -2, 3, 1, 0]
    #A = [1, 2, 6, 4, 0, -1 ]
    equilibrium_index(A)
    equilibrium_index_approach(A)