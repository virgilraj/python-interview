
def find_interleavings(X, Y, result=set(), cur=""):
    # insert curr into set if we have reached end of both Strings
    if not X and not Y:
        result.add(cur)
        return result
    
    # if X is empty, append its first character not in the
	# result and recur for remaining substring
    if X:
        result = find_interleavings(X[1:], Y, result, cur + X[0])
    if Y:
        result = find_interleavings(X, Y[1:], result, cur + Y[0])
    
    return result

if __name__ == "__main__":
    X = "ABC"
    Y = "ACB"

    # use set to handle duplicates
    result = find_interleavings(X, Y)
    print(result)