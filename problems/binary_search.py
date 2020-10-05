def binasry_serach(arr, X):
    left, right = 0, len(arr)-1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == X:
            return True
        elif X < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
            
    return False

# Find out if a key x exists in the sorted list A
# or not using binary search algorithm
def binarySearch(A, x):

	# search space is A[left..right]
	(left, right) = (0, len(A) - 1)

	# till search space consists of at-least one element
	while left <= right:

		# we find the mid value in the search space and
		# compares it with key value

		mid = (left + right) // 2

		# overflow can happen. Use:
		# mid = left + (right - left) / 2
		# mid = right - (right - left) // 2

		# key value is found
		if x == A[mid]:
			return mid

		# discard all elements in the right search space
		# including the mid element
		elif x < A[mid]:
			right = mid - 1

		# discard all elements in the left search space
		# including the mid element
		else:
			left = mid + 1

	# x doesn't exist in the list
	return -1

if __name__ == "__main__":
    A = [1,2,2, 5, 6, 8,10]
    key = 101
    print(binasry_serach(A, key))