def largest_number(arr):

    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            count +=1
            s1 = str(arr[i]) + str(arr[j])
            s2 = str(arr[j]) + str(arr[i])
            if(int(s2) > int(s1)):
                arr[i],arr[j] = arr[j],arr[i]
    
    print(arr, count)

if __name__ == "__main__":
    largest_number([3,30,34,9])