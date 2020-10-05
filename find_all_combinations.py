#arr[] ---> Input Array 
#data[] ---> Temporary array to store current combination 
#start & end ---> Staring and Ending indexes in arr[] 
#index ---> Current index in data[] 
#r ---> Size of a combination to be printed 

def combination_util(arr, data, start, end, index, r):
    #Current combination is ready to be printed, print it 
    if(index == r):
        print(data)
        return
    
    # replace index with all possible elements. 
    # The condition "end-i >= r-index" 
    # makes sure that including one element 
    # at index will make a combination with 
    # remaining elements at remaining positions
    #i = start
    for i in range(start,end):
        print(end - i, r-index)
        if(end-i >= r- index):
            data[index] = arr[i]
            combination_util(arr, data, i+1, end, index+1, r)     

if __name__ == "__main__":
    arr = [ 1, 2, 3, 4, 5 ]
    r = 3
    data =  [0] * r
    #print(data)
    combination_util(arr, data, 0, len(arr), 0, r)