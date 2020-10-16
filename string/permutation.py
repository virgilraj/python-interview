
def permute(data, i, length): 
    if i==length: 
        #print(''.join(data) )
        print(data)
    else: 
        for j in range(i,length): 
            #swap
            data[i], data[j] = data[j], data[i] 
            permute(data, i+1, length) 
            data[i], data[j] = data[j], data[i] 


def permute_other(lst):
    n = len(lst)
    if n == 0:
        return []
    elif n == 1:
        return lst
    else:
        l = []
        for i in range(n):
            x = lst[i]
            xs = lst[:i] + lst[i+1:]
            for p in permute_other(xs):
                l.append(str(x) + str(p))
        return l

if __name__ == "__main__":
    string = "ABC"
    n = len(string) 
    #data = list(string) 
    data = [1,2,3,4]
    # Time complexities O(n*n!)
    permute(data, 0, n)
    
    for p in permute_other(data):
        print(p)