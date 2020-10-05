### not good solution
def find_small_sublist_given_sum(arr, k):
    n = len(arr)
    win_sum = 0
    left = 0
    length = 1000
    for right in range(n):
        win_sum += arr[right]

        while win_sum > k and left <= right:
            print(length, right-left+1)
            length = min(length, right-left+1)

            win_sum -= arr[left]
            left +=1
    

    print("Min length", length)




if __name__ == "__main__":
    arr = [ 3, 4, -7, 3, 1, 3, 1, -4, -2, -2 ]
    find_small_sublist_given_sum(arr, 7)