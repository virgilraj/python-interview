
def partition(arr,start, end):
    pIndex = start
    # each time we find a negative number, pIndex is incremented
	# and that element would be placed before the pivot
    for i in range(start,end):
        if arr[i] < 0:
            arr[i],arr[pIndex] = arr[pIndex],arr[i]
            pIndex +=1
    
    print(arr)

if __name__ == "__main__":
    a = [9, -3, 5, -2, -8, -6, 1, 3,0]
    partition(a, 0, len(a)-1)