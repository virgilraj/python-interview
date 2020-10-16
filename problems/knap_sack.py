from collections import deque

# Input:
# Values (stored in list v)
# Weights (stored in list w)
# Number of distinct items (n)
# Knapsack capacity (W)
def kanpsack_binary_DP(v, w, W):
    # T[i][j] stores the maximum value of knapsack having weight less
    # than equal to j with only first i items considered.
    T = [[0 for x in range(W + 1)] for y in range(len(v) + 1)]

    # do for ith item
    for i in range(1, len(v) + 1):

        # consider all weights from 0 to maximum capacity W
        for j in range(W + 1):

            # don't include ith element if j-w[i-1] is negative
            if w[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                # find maximum value we get by excluding or including the ith item
                T[i][j] = max(T[i - 1][j], T[i - 1][j - w[i - 1]] + v[i - 1])
    print(T)
	# return maximum value
    return T[len(v)][W]



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
    lst.sort(key=lambda x: x['ratio'], reverse=True)

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
    #v = [2, 3, 5]
    #w = [1, 2, 3]
    # Knapsack capacity
    #cap = 4
    kanpsack_binary_DP(v, w, cap)
