def is_rotated_palindrome(S):
    for i in range(len(S)):
        # in-place rotate the string by 1 unit
        S = S[1:] + S[0]
        if(checkPalnidrom(S) == True):
            return True
    
    return False

def checkPalnidrom(S):
    n = len(S)
    mid = n //2
    for i in range(mid):
        if S[i] != S[n-i-1]:
            return False
    return True

if __name__ == "__main__":
    S = "ABCDCBA"
    print("Is Palindrome ", is_rotated_palindrome(S))
    