def max_heapify(arr, n, i):
    largest = i

    left = 2 * i + 1
    right = 2 * i + 2

    #if left child larger than root
    if(left < n and arr[left] > arr[largest]):
        largest = left
    
    #if right child larger than root
    if(right < n and arr[right] > arr[largest]):
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def min_heapify(A, n, i):
    # get left and right child of node at index i
    left = 2 * i + 1
    right = 2 * i + 2

    smallest = i

    # compare A[i] with its left and right child
    # and find smallest value
    if left < n and A[left] < A[smallest]:
        smallest = left

    if right < n and A[right] < A[smallest]:
        smallest = right

    # swap with child having lesser value and
    # call heapify-down on the child
    if smallest != i:
        #swap(A, i, smallest)
        A[i],A[smallest] = A[smallest], A[i]
        min_heapify(A, n,smallest)

def min_heap_sort(arr):
    n = len(arr)
    for i in reversed(range(len(arr))):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp

        min_heapify(arr, i, 0)
    print(arr)

def max_heap_sort(arr):
    n = len(arr)
    for i in reversed(range(len(arr))):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp

        max_heapify(arr, i, 0)
    print(arr)

def kth_max(arr, k):
    n = len(arr)
    for i in reversed(range(len(arr))):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        if(i== (n-k)):
            print("Kth max is", temp, arr[i])
            break
        max_heapify(arr, i, 0)

def kth_min(arr, k):
    n = len(arr)
    for i in reversed(range(len(arr))):
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp
        if(i== (n-k)):
            print("Kth min is", temp)
            break
        min_heapify(arr, i, 0)

# Function to convert max heap to min heap
def convert(A):

    # Build-Heap: Call heapify starting from last internal
    # node all the way upto the root node
    i = (len(A) - 2) // 2
    while i >= 0:
        #print(i)
        min_heapify(A, len(A), i )
        i = i - 1

def is_min_heap(arr):
    # check for all internal nodes that their left child and
	# right child (if present) holds min-heap property or not
    n = (len(arr)-2)//2 +1
    for i in range(n):
        if arr[i] > arr[i*2 + 1] or (2*i +2 != len(arr) and arr[i] > arr[i*2 + 2]):
            return False
    return True

def is_max_heap(arr):
    # check for all internal nodes that their left child and
	# right child (if present) holds min-heap property or not
    n = (len(arr)-2)//2 +1
    for i in range(n):
        if arr[i] < arr[i*2 + 1] or (2*i +2 != len(arr) and arr[i] < arr[i*2 + 2]):
            return False
    return True
    

if __name__ == "__main__":
    arr = [-2,1,5,9,4,6,7]
    #arr = [9, 4, 7, 1, -2, 6, 5]
    #n =len(arr)
    print("Is min heap ", is_min_heap(arr))
    i = (len(arr) - 2) // 2
    while i >= 0:
        #print(i)
        max_heapify(arr, len(arr), i )
        i = i - 1
    
    kth_max(arr, 3)

    print(arr)

    max_heap_sort(arr)
    
    A = [9, 4, 7, 1, -2, 6, 5]
    print("Is max heap ", is_max_heap(A))
	# build a min heap by initializing it by given list
    convert(A)
    
    print(A)
    min_heap_sort(A)
    #kth_min(A, 3)
    
