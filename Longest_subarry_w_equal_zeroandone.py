
#Contiguous array 
#find the count of all contiguous array will equal number of zeroes and 
#If consider 0 to -1 then sum of the sub array always 0 
#Use dictionary -> key = sum , value = index
def longest_sub_with_zeroandone(arr):
    n = len(arr)
    max_len = 0
    sum = 0
    h = {}
    for i in range(n):
        if(arr[i] == 0):
            arr[i] = -1
        
        sum += arr[i]
        
        if(sum == 0):
            max_len = max(max_len, i+1)
        elif sum not in h.keys():
            h[sum] = i
        else:
            max_len = max(max_len, i-h[sum])
        
    print("Max length ", max_len)


if __name__ == "__main__":
    arr = [ 0, 0, 1, 1, 1, 0, 0]
    longest_sub_with_zeroandone(arr)