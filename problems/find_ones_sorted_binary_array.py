
def find_ones_from_binary_array(arr, left, right):
    if arr[right] == 0:
        return 0
    
    if arr[left] == 1:
        return right -left +1
    
    mid = (left + right )//2

    return find_ones_from_binary_array(arr, left , mid) + find_ones_from_binary_array(arr, mid+1, right)

if __name__ == "__main__":
    A = [0, 0, 1, 1, 1, 1, 1]
    print("Total number of 1's present are", find_ones_from_binary_array(A, 0, len(A) - 1))
