
def equilibrium_index(arr):
    n = len(arr)
    lefsum = 0
    sum = 0
    for i in range(n):
        sum += arr[i]

    for i in range(n):
        #total sum - current sum == right sum
        sum -=arr[i] #right sum
        
        if(sum == lefsum):
            print("equilibrium_index", i)
        lefsum +=arr[i]

def equilibrium_index_approach(arr):
    n = len(arr)
    for i in range(1, n):
        left = 0
        right = 0
        l = i - 1
        r = i + 1
        while(l >= 0):
            left +=arr[l]
            l -=1
        while(r < n):
            right += arr[r]
            r +=1
        if(left == right):
            print("equilibrium ", i)


if __name__ == "__main__":
    #A = [0, -3, 5, -4, -2, 3, 1]
    A = [1, 2, 6, 4, 0, -1]
    #A = [1, 2, 6, 4, 0, -1 ]
    equilibrium_index(A)
    equilibrium_index_approach(A)