
# using binary search we can find it in log(n)
# if value of mid and index of mid is equal
#then mis match lies in the right side of it

def smallest_missing_element(arr, left , right):
    if left > right:
        return left
    
    mid = left + (right - left) // 2

    if arr[mid] == mid:
        return smallest_missing_element(arr,  mid + 1, right)
    else:
        return smallest_missing_element(arr,  left, mid-1)


if __name__ == "__main__":
    A = [0, 1, 2,  4, 5, 6]

    (left, right) = (0, len(A) - 1)

    print("The smallest missing element is", smallest_missing_element(A, left, right))