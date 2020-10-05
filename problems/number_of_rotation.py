
#Linear method
def find_number_of_rotation(arr):

    count = 0
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            count = i
            break
    print("Number of Rotation is", count)

def find_number_of_rotation_bianry_search(A):
    left,right = 0, len(A)-1
    rotation = 0
    # iterate till search space contains at-least one element
    while(left <= right):
        if(arr[left] == arr[right]):
            rotation = left
            break
        mid = (left + right) // 2
        print(mid)
        next = (mid + 1) % len(A)
        prev = (mid - 1 + len(A)) % len(A)

        # if mid element is less than both its next and previous
        # neighbor, then it is the minimum element of the list
        if A[mid] <= A[next] and A[mid] <= A[prev]:
            rotation = mid
            break

        # if A[mid..right] is sorted and mid is not the minimum element,
        # then pivot element canbe present not in A[mid..right] and
        # we can discard A[mid..right] and search in the left half
        elif A[mid] <= A[right]:
            right = mid - 1

        # if A[left..mid] is sorted then pivot element canbe present not in
        # it and we can discard A[left..mid] and search in the right half
        elif A[mid] >= A[left]:
            left = mid + 1
    
    print("Number of Rotation is asd", rotation)

if __name__ == "__main__":
    arr =  [8, 9, 10,11, 1, 2, 3, 4, 5, 6, 7]
    find_number_of_rotation(arr)
    find_number_of_rotation_bianry_search(arr)