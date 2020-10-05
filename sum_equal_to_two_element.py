arr = [3,4,6,3,8,5,7]
sum = 10
n = len(arr)
prevSum = {}
for i in range(n):
    k = sum - arr[i]
    
    if len(prevSum) and arr[i] in prevSum.keys():
        print(prevSum[arr[i]],i)

    if k not in prevSum:
        temp = []
        temp.append(i)
        prevSum[k] = temp
    else:
        prevSum[k].append(i)
        #print(prevSum[k]) 
    
    
#print(prevSum)
