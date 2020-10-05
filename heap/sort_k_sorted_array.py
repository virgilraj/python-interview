from heapq import heapify, heappop, heappush

def sort_k_sorted_array(arr, k):
    h = []
    heapify(h)
    for i in range(k+1):
        heappush(h, arr[i])

    index = 0
    for i in range(k+1, len(arr)):
        arr[index] = heappop(h)
        heappush(h, arr[i])
        index = index +1

    while len(h) > 0:
        arr[index] = heappop(h)
        index = index +1
    
    print(arr)

if __name__ == "__main__":
    arr = [4,2,1,3,5]
    h = []
    heapify(h)
    for i in range(len(arr)):
        heappush(h, arr[i])
    for i in h: 
        print(i, end = ' ') 
    print("\n") 

    A = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    sort_k_sorted_array(A, 2)