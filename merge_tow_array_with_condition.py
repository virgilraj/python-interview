#Merge two arrays by satisfying given constraints
#Step 1 . curPos and J =0 
#2. X[curPos] is zero and next element of X greater than Y element then replace zero with y element
#3. curPos++ and j++
#4. curpos element is zero and next element greater than zero and next element less than Y
#5. Swap curpos to next element and curPos++
#6. curpos element > 0 then curPos++
#7. replace last zero with Y array 

def merge_two_sorted_array_replaces_zero(X,Y):
    j = 0
    curPos = 0
    m = len(X)
    n = len(Y)
    for i in range(m-1):
        if(X[curPos] == 0 and X[i+1] > Y[j]):
            X[curPos] = Y[i]
            curPos +=1
            j +=1
        elif(X[curPos] == 0 and X[i+1] >0 and X[i+1] < Y[j]):
            X[curPos],X[i+1] = X[i+1],X[curPos]
            curPos +=1
        elif(X[curPos] > 0):
            curPos +=1

    #Replace Last zero elements
    while(curPos < m and j < n):
        X[curPos] = Y[j]
        curPos +=1
        j +=1

if __name__ == "__main__":
    X = [0, 2, 0, 3, 0, 5, 6, 0, 0]
    Y = [1, 8, 9, 10, 15]
    merge_two_sorted_array_replaces_zero(X,Y)
    print(X)
