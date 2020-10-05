from heapq import heapify, heappop, heappush

class Node(object):
    def __init__(self, value, number, index):
        self.value = value
        self.number = number
        self.index = index
    
    def get_value(self):
        return self.value
    
    def get_list_number(self):
        return self.number
    
    def get_index(self):
        return self.index
    def set_value(self, value):
        self.value = value
    
    def set_list_number(self, number):
        self.number = number
    
    def set_index(self, index):
        self.index = index
    
def merge(arr):
    n = len(arr)
    h = []
    heapify(h)
    index = 0
    for i in range(n):
        if(index < len(arr[i]) ):
            n = Node(arr[i][index], i, index)
            heappush(h,n.value)
    
    for i in h: 
        print(i, end = ' ') 
    print("\n") 


if __name__ == "__main__":
    A = []
    A.append([10, 20, 30, 40])
    A.append([15, 25, 35])
    A.append([27, 29, 37, 48, 93])
    A.append([32, 33])
    merge(A)


    

