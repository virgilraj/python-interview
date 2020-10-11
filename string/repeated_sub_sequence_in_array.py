'''
The idea is very simple. 
If we discard all non-repeating elements from the string (having frequency of 1) 
and the resulting string is non-Palindrome, 
then the string contains a repeated subsequence. 
If the resulting string is a palindrome and don’t have any character with frequency 3 or more,
 the string cannot have repeated subsequence.
'''

def repeated_sub_sequence(S):
    # dict to store frequency of each distinct character of given String
    freq = {}
    
    # update dict with frequency
    for c in S:
        # if frequency of any character becomes 3, we have found repeated subsequence
        freq[c] = freq.get(c, 0) + 1
        if freq.get(c) >= 3:
            return True
    # consider all repeated elements (frequency 2 or more)
	# and discard all non-repeating elements (frequency 1)

    repeated = [c for c in S if freq.get(c) >= 2]
    print(repeated)
    print("Has repeated sub sequence", not is_palindrome(repeated))

def is_palindrome(A):
    low, high = 0, len(A) -1
    while low < high:
        if A[low] != A[high]:
            return False
        low = low +1
        high = high - 1
    return True

if __name__ == "__main__":

    #S = "XYBYAXB"
    S = "MADAM"
    S = "XYBABYX"
    repeated_sub_sequence(S)
