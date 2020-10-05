import queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None
    
    def get(self):
        return self.data
    
    def set(self, data = None):
        self.data = data
    
    def get_children(self):
        children = []
        if(self.left is not None):
            children.append(self.left)
        if self.right != None:
            children.append(self.right)
    
class BST(object):
    def __init__(self):
        self.root = None
    
    def set_root(self, data):
        self.root = Node(data)
    
    def insert_node(self, cur_node, data):
        if data < cur_node.data:
            if cur_node.left:
                self.insert_node(cur_node.left,data)
            else:
                cur_node.left = Node(data)
        elif data > cur_node.data:
            if cur_node.right:
                self.insert_node(cur_node.right, data)
            else:
                cur_node.right = Node(data)
    
    def insert(self, data):
        if self.root is None:
            self.set_root(data)
        else:
            self.insert_node(self.root, data)
        
#util function
#print inorder
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

#print inorder
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

#print inorder
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

#print level order
def level_order(root):
    if root:
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            cur_node = q.get()
            print(cur_node.data, end=" ")
            
            if cur_node.left:
                q.put(cur_node.left)
            if cur_node.right:
                q.put(cur_node.right)

def Inorder_Iterative(root):

    if root:
        S = []
        cur_node = root
        while True:
            if cur_node:
                S.append(cur_node)
                cur_node = cur_node.left
            elif cur_node is None and len(S) > 0:
                temp = S[-1]
                S.pop()
                print(temp.data, end=" ")
                cur_node = temp.right
            else:
                break

def Preorder_Iterative(root):
    cur_node = root
    S = []
    S.append(cur_node)
    while len(S) > 0:
        temp = S[-1]
        S.pop()
        print(temp.data, end=" ")
        if(temp.right):
            S.append(temp.right)
        if(temp.left):
            S.append(temp.left)

def delete(root, data):
    if root is None:
        return root
    
    if data < root.left:
       root.left = delete(root.left ,data)
    elif data > root.right:
        root.right = delete(root.right, data)
    
    else:
        #No left node
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else: #root has both left and right
            #get smallest from right - > assign to root 
            # delete the smallest right
            temp = get_min_value(root.right)
            root.data = temp
            root.right = delete(root.right, temp)

def find_node(root, val):
    if root is None or root.data == val:
        return root
    
    if root.data < val:
        return find_node(root.right, val)
    elif root.data > val:
        return find_node(root.left, val)

def get_min_value(root):
    if root is None:
        return 0
    cur_node = root
    while cur_node.left:
        cur_node = cur_node.left
    return cur_node.data

def get_max_value(root):
    if root is None:
        return 0
    cur_node = root
    while cur_node.right:
        cur_node = cur_node.right
    return cur_node.data

def size(root):
    if root is None:
        return 0
    return size(root.left) + 1 + size(root.right)

def height(root):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)
    h = 1 + max(left_height, right_height)
    return h

def bst_from_sorted_array(arr):
    if arr is None or len(arr) == 0:
        return None
    
    mid = len(arr)//2
    root = Node(arr[mid])

    root.left = bst_from_sorted_array(arr[:mid])
    root.right = bst_from_sorted_array(arr[mid+1:])

    return root

def get_inorder_successor(root, val):

    node = find_node(root, val)
    if node.right is not None:
        print("\nInorder successor is ", get_min_value(node.right))
    else:
        successor = None
        ancestor = root
        while node != ancestor:
            if node.data < ancestor.data:
               successor = ancestor
               ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        
        if successor is not None:
            print("In order successor is ", successor.data)

def get_inorder_predecessor(root, val):

    node = find_node(root, val)
    if node.left is not None:
        print("\nInorder predecessor is ", get_max_value(node.left))
    else:
        predecessor = None
        ancestor = root
        while node != ancestor:
            if node.data > ancestor.data:
               predecessor = ancestor
               ancestor = ancestor.left
            else:
                ancestor = ancestor.left
        
        if predecessor is not None:
            print("\nIn order predecessor is ", predecessor.data)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    bs = bst_from_sorted_array(arr)
    level_order(bs)
    get_inorder_successor(bs,3 )
    get_inorder_predecessor(bs,3 )

    print("\nLeft, right, tree height", height(bs))

    bst = BST()
    bst.insert(50)
    bst.insert(20)
    bst.insert(70)
    bst.insert(10)
    bst.insert(100)
    bst.insert(30)
    

    print("\nlevel order")
    level_order(bst.root)
    print("\nmin and max value and size ", get_min_value(bst.root),",", get_max_value(bst.root),",", size(bst.root))
    print("\nPre order")
    preorder(bst.root)
    print("\nPre order1")
    Preorder_Iterative(bst.root)
    
    print("\nIn order")
    inorder(bst.root)
    print("\nIn order")
    Inorder_Iterative(bst.root)


