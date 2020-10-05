
#rodcut(n) = max { price[i – 1] + rodCut(n – i) } where 1 <= i <= n

def rodCut(price, length):
    if length == 0:
        return 0
    
    maxValue = float('-inf')

    # one by one partition the given rod of length n into two parts of length
	# (1, n-1), (2, n-2), (3, n-3), .... (n-1 , 1), (n, 0) and take maximum

    for i in range(1, length + 1):
        cost = price[i-1] + rodCut(price, length - i)

        if cost > maxValue:
            maxValue = cost
            
    return maxValue


#rod cut dynamic programing
def rodCut_DP(price, length):
    # T[i] stores maximum profit achieved from rod of length i
    T = [0] *(length + 1)

    #consider rod of length i

    for i in range(1, length+1):
        # divide the rod of length i into two rods of length j
        # and i-j each and take maximum
        for j in range(1, i+1):
            print(i,j)
            
            print(T[i], price[j-1], T[i - j])
            T[i] = max(T[i], price[j-1] + T[i-j] )
            print(T)
    
    print("Maximum profit ", T[length])

if __name__ == "__main__":
    # length = [ 1, 2, 3, 4, 5, 6, 7, 8 ]
    price = [1, 5, 8, 9, 10, 17, 17, 20]

    rodlength = 4
    print("Maximum profit ", rodCut(price, rodlength))
    rodCut_DP(price, rodlength)
