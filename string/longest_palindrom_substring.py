
def longestPalSubstr(str):
    n = len(str)
    maxlength = 0
    index = ()
    for i in range(n):
        for j in range(i,n):
            if(checkPalnidrom(str[i:j+1]) == True):
                if (maxlength < j-i+1):
                    maxlength = j-i+1
                    index = i, j+1
    
    print("Longest palindrom ", maxlength, index, str[index[0]:index[1] ])

def checkPalnidrom(str):
    n = len(str)
    mid = n //2
    for i in range(mid):
        if str[i] != str[n-i-1]:
            return False
    return True

def longest_palindrom_dp(str):
    n = len(str)

    #create dp table with nXn
    
    table = [[0 for x in range(n)] for y in range(n) ]
    
    #diagonal element is always palindrom
    maxlength = 1
    i = 0
    while i < n:
        table[i][i] =True
        i = i +1
    
    #2 element sub string
    #previous element and current is same then mark true
    start = 0
    i = 0
    while i < n -1:
        if str[i] == str[i+1]:
            table[i][i+1] = True
            start = i
            maxlength = 2
        i = i +1

    # Check for lengths greater than 2.  
    # k is length of substring 
    #1. start and end element should be same
    #2. middle string should be palindrom

    k = 3
    while k <=n:
        #reset staring index
        i =0
        while i < (n - k + 1):
            # Get the ending index of  substring from starting  
            # index i and length k 
            j = i + k -1
            print(i, j, k)
            if str[i] == str[j] and table[i+1][j-1]:
                table[i][j] =True

                if k > maxlength:
                    maxlength = k
                    start = i
            i = i +1
        k = k +1

    print("Longest pal sub str is", str[start:start+maxlength], maxlength )
'''
The idea is very simple and effective. 
For each character in the given string, we consider it as mid point of a palindrome 
and expand in both directions to find maximum length palindrome. 
For even length palindrome, we consider every adjacent pair of characters as mid point.
'''

def expand(S, low, high):
    length = len(S)

    #expand in both direction
    while low >=0 and high < length and S[low] == S[high]:
        low = low - 1
        high = high + 1
    
    return S[low+1:high]


def longest_palindrom_simple(S):
    max_str = ""
    max_length = 0

    length = len(S)
    
    for i in range(length):
        # find a longest odd length palindrome with str[i] as mid point
        # OOD length
        cur_str = expand(S, i, i)
        cur_length = len(cur_str)

        if cur_length > max_length:
            max_length = cur_length
            max_str = cur_str

        # find a longest even length palindrome with str[i] and str[i+1] as mid points
		# Note that a even length palindrome has two mid points
        # EVEN length
        cur_str = expand(S, i, i+1)
        cur_length = len(cur_str)

        if cur_length > max_length:
            max_length = cur_length
            max_str = cur_str

    print(max_str, max_length)
if __name__ == "__main__":
    #print(checkPalnidrom("virgil"))
    longestPalSubstr("abac")
    longest_palindrom_dp("abac")
    longest_palindrom_simple("abac")