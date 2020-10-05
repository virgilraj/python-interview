#Circular array
def find_ele_sorted_array(arr, X):
    left, right = 0, len(arr)-1

    while(left <= right):
        mid = (left + right)//2

        if arr[mid] == X:
            return mid
        
        #Right half
        if arr[mid] <= arr[right]:
            if arr[mid] < X <= arr[right]:
                left  = mid +1
            else:
                right = mid -1
        else:
            if arr[mid] > X >= arr[left]:
                right = mid -1
            else:
                left = mid +1
    return -1

def 

if __name__ == "__main__":
    A = [9, 10, 2, 5, 6, 8]
    key = 10
    print(find_ele_sorted_array(A, key))