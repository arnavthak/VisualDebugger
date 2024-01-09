
class BST:
    def __init__(self):
        ''' Initialize BST '''
        self.root = None
    
    def put(self, key):
        ''' Put a new BST Node with value key in the BST '''
        if self.root:
            self.root.put(key)
        else:
            self.root = BSTNode(key)

class BSTNode:
    def __init__(self, val, left=None, right=None):
        ''' Initialize BST Node '''
        self.val = val
        self.left = left
        self.right = right
    
    def put(self, key):
        ''' Put a new BST Node with value key in the BST '''
        if key < self.val:
            if self.left:
                self.left.put(key)
            else:
                self.left = BSTNode(key)
        elif key > self.val:
            if self.right:
                self.right.put(key)
            else:
                self.right = BSTNode(key)
    

    