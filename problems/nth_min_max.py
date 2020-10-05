import sys

def findNthMax(arr, k):
    intMin = -sys.maxsize -1
    nThMax = intMin
    pos = 0
    maxele = intMin
    finalList = []
    count = 0
    for i in range(k):
        for j in range(len(arr)):
            count +=1
            if arr[j] > nThMax:
                nThMax = arr[j]
                pos = j
        arr[pos] = intMin
        maxele = nThMax
        finalList.append(nThMax)
        nThMax = intMin

    print(k, " th max is ", maxele, count)

def findNthMin(arr,k):
    intMax = sys.maxsize
    nthMin = intMax
    minele = intMax
    pos = 0
    for i in range(k):
        for j in range(len(arr)):
            if arr[j] < nthMin:
                nthMin = arr[j]
                pos = j
        
        arr[pos] = intMax
        minele = nthMin
        nthMin = intMax
    
    print(k, " th min value is ", minele)

if __name__ == "__main__":
    arr = [2,3,1,8,6,7]
    findNthMax(arr, 2)
    arr = [2,3,1,3,5,8,6,7]
    findNthMin(arr, 5)