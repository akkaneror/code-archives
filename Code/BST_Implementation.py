# Author: OMKAR PATHAK

# This program illustrates an example of Binary Search Tree using Python
# Binary Search Tree, is a node-based binary tree data structure which has the following properties:
#
# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# The left and right subtree each must also be a binary search tree.
# There must be no duplicate nodes.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.size = 1

    def update_stats(self):
        self.size = (0 if self.leftChild is None else self.leftChild.size) \
                    + \
                    (0 if self.rightChild is None else self.rightChild.size)

    def insert(self, k):
        ''' For inserting the data in the Tree '''
        self.size += 1
        if self.data == k:
            return False        # As BST cannot contain duplicate data

        elif k < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild: #is not None
                return self.leftChild.insert(k)
            else: #is None
                self.leftChild = Node(k)
                return self.leftChild #return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(k)
            else:
                self.rightChild = Node(k)
                return self.rightChild #return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def delete(self, k):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if k < self.data:
            self.leftChild = self.leftChild.delete(k)
        elif k > self.data:
            self.rightChild = self.rightChild.delete(k)
        else:
            # deleting node with one child
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data)

        return self

    def find(self, k):
        ''' This function checks whether the specified data is in tree or not '''
        if(k == self.data):
            return True
        elif(k < self.data):
            if self.leftChild: # is not None
                return self.leftChild.find(k)
            else:
                return False
        else:
            if self.rightChild: # is not None
                return self.rightChild.find(k)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild: #is not None
                self.leftChild.preorder()
            if self.rightChild: #is not None
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild: #is not None
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild: #is not None
                self.rightChild.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild: #is not None
                self.leftChild.postorder()
            if self.rightChild: #is not None
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

    def rank(self, k):
        """ Return the number of data <= k in the subtree rooted at this node."""
        left_size = 0 if self.leftChild is None else self.leftChild.size
        if k == self.data:
            return left_size + 1
        elif k < self.data:
            if self.leftChild: #is not None
                return self.leftChild.rank(k)
            else: #is None
                return 0
        else:
            if self.rightChild: #is not None
                return self.rightChild.rank(k) + left_size + 1
            else:
                return left_size + 1

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is not None:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()

    def rank(self, k):
        """The number of data <= k in the tree"""
        if self.root is not None:
            return self.root.rank(k)
        else:
            return 0


if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree.find(1))
    print(tree.find(12))
    ''' Following tree is getting created:
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    '''

    tree.preorder()
    tree.inorder()
    tree.postorder()
    print('\nRank:', tree.rank(10))
    print('\nRank:', tree.rank(12))
    print('\n\nAfter deleting 20')
    tree.delete(20)
    tree.inorder()
    tree.preorder()
    print('\n\nAfter deleting 10')
    tree.delete(10)
    tree.inorder()
    tree.preorder()
    print('\nRank:', tree.rank(12))
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

        # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

        # Key is smaller than root's key
    return search(root.left, key)
