import sys

#Find the max 2 elements
#Find Min 2 elements
#Find the max (multiple of max , multiple of min)

def find_max_product_of_two_integer(arr):
    maxel1 = 0
    maxel2 = (-1)* sys.maxsize
    minel1 = 0
    minel2 =  sys.maxsize
    n = len(arr)

    for i in range(n):
        if(arr[i] > maxel1):
            maxel2 = maxel1
            maxel1 = arr[i]
        if(arr[i] < maxel1 and arr[i] > maxel2):
            maxel2 = arr[i]
        
        if(arr[i] < minel1):
            minel2 = minel1
            minel1 = arr[i]
        if(arr[i] > minel1 and arr[i] < minel2):
            minel2 = arr[i]
        
    print(maxel1, maxel2, minel1, minel2)
    print("Max product", max(maxel1*maxel2, minel1*minel2))


if __name__ == "__main__":
    A = [-10, -3, 5, 6, -2]
    find_max_product_of_two_integer(A)