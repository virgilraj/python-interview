import sys

#Find largest sub-array formed by consecutive integers
#Condition -- no duplicate elements
#So far O(n2)
#Formaula :: difference between Max and Min value equal to last and first index difference

def longest_consecutve_integer_subarray(arr):
    n = len(arr)
    max_len = 0

    for i in range(n):
        min_ele = arr[i]
        max_ele = arr[i]
        for j in range(i+1, n):
            min_ele = min(min_ele, arr[j])
            max_ele = max(max_ele, arr[j])

            if( (max_ele - min_ele) == (j-i)):
                max_len = max(max_len, max_ele-min_ele+1)
                print("ConsecutiveSub array ", i, j)
            
    print("nLongest Consecutive Sub Array length ", max_len)       

def myapproach(arr):
    n = len(arr)
    max_len = float('-inf')
    s = 0
    e = 0
    ms = 0
    me =0

    for i in range(1,n):
        if abs(arr[i] - arr[i-1]) == 1:
            e = i+1
        else:
            s = i
            e = i
        #print(s,e)
        if max_len < e-s:
            max_len = e-s
            ms = s
            me = e
    print(max_len , arr[ms:me])
if __name__ == "__main__":
    #arr = [ -2, -1, -13,  4, -1, 2,1, -5, 4]
    arr = [ 4, 6, 0, 2, 1, 3, 10, 8, 11 ]
    longest_consecutve_integer_subarray(arr)
    #arr = [4,5,1,2,3,6,7]
    myapproach(arr)