from collections import deque

def kanpsack_binary(Cap, W, Val, n):
    #base case
    if n == 0 or Cap == 0:
        return 0
    
    if(W[n-1] > Cap):
        return kanpsack_binary(Cap, W, Val, n-1)
    else:
        return max(kanpsack_binary(Cap, W, Val, n-1), 
        Val[n-1] + kanpsack_binary(Cap-W[n-1], W, Val, n-1))

def kanpsack_fraction(Cap, W, Val, n):
    lst = []
    for i in range(len(W)):
        obj = {'weight' : W[i], 'Val': Val[i], 'ratio': Val[i]/W[i] }
        lst.append(obj)
    lst.sort(key=lambda x: x['ratio'])

    curweight = 0
    finalval = 0
    for cur in lst:
        if(curweight + cur['weight'] < Cap):
            finalval += cur['Val']
        else:
            ratio = (Cap-curweight)/cur['weight']
            finalval = finalval + cur['Val']*ratio
    
    print(int(finalval))


if __name__ == "__main__":
    v = [20, 5, 10, 40, 15, 25]
    w = [1, 2, 3, 8, 7, 4]
    # Knapsack capacity
    cap = 10

    print("Knapsack value is", kanpsack_binary(cap, w, v, len(v)))
    kanpsack_fraction(cap, w, v, len(v))
