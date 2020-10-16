
def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) //2
    left = arr[:mid]
    right = arr[mid:]

    #Recursuivily sort 
    merge_sort(left)
    merge_sort(right)

    k = 0
    l = 0
    r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[k] = left[l]
            l = l + 1
        else:
            arr[k] = right[r]
            r = r +1
        k = k +1
    # Checking if any element was left 

    while l < len(left):
        arr[k] = left[l]
        l = l +1
        k = k +1
    
    while r < len(right):
        arr[k] = right[r]
        r = r +1
        k = k +1



if __name__ == "__main__":
    arr = [6,7,10,23,1,4,9]
    merge_sort(arr)
    print(arr)