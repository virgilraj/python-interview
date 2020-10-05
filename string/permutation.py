
def permute(data, i, length): 
    if i==length: 
        print(''.join(data) )
    else: 
        for j in range(i,length): 
            #swap
            data[i], data[j] = data[j], data[i] 
            permute(data, i+1, length) 
            data[i], data[j] = data[j], data[i] 


if __name__ == "__main__":
    string = "ABC"
    n = len(string) 
    data = list(string) 
    # Time complexities O(n*n!)
    permute(data, 0, n)