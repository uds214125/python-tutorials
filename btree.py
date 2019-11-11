class BTree:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,left,right):
        self.left = left
        self.right = right
    

obj = BTree(1)
# obj.insert(2,3)
obj.left = 2
obj.right = 3
print(obj.left)  