#Trees
#A tree is a hierarchical data structure consisting of nodes, where each node has a value 
#and references to childnodes

#The top node is called the root, nodes with no children are called leaves
#Trees can be classified into various types, such as binary trees, binary search trees, AVL 
#trees, etc

#Node: each element in the tree
#Root: the top node of the tree
#Edge: the link between two nodes
#Leaf: a node with no children
#Subtree: a tree formed by a node and its decendants


#Key vs Val
#Key indicates the uniqueness of the 
#Val indicates general data being stored in the data structure


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_recursive(self.root, val)
    
    def insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.insert_recursive(node.left, val)
                
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self.insert_recursive(node.right, val)
    
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.val, end=' ')
            self.inorder_traversal(node.right)
    
    def preorder_traversal(self, node):
        if node is not None:
            print(node.val, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.val, end=' ')


tree = BinaryTree()

elements = [10, 5, 15, 3, 7, 12, 18]
for el in elements:
    tree.insert(el)

print()
print("Inorder traversal:")
tree.inorder_traversal(tree.root)
print()
print("\nPreorder traversal:")
tree.preorder_traversal(tree.root)
print()
print("\nPostorder traversal:")
tree.postorder_traversal(tree.root)    


#Methods of traversal


#Inorder traversal
#Left -> Root -> Right

#Traverse the left subtree, visit the root node, traverse the right subtree
#Recursively perform an inorder traversal of the left subtree
#Process the root node
#Recursively perform an inorder traversal of the right subtree

#     10
#    /  \
#   5    15
#  / \   / \
# 3   7 12 18

#The inorder traversal would be: 3, 5, 7, 10, 12, 15, 18


#Preorder traversal
#Root -> Left -> right

#Visit the root node, traverse the left subtree, traverse the right subtree
#Process the root node
#Recursively perform a preorder traversal of the left subtree
#Recursively perform a preorder traversal of the right subtree

#     10
#    /  \
#   5    15
#  / \   / \
# 3   7 12 18

#The preorder traversal would be: 10, 5, 3, 7, 15, 12, 18


#Postorder traversal
#Left -> Right -> Root

#Traverse the left subtree, traverse the right subtree, visit the root node
#Recursively perform a postorder traversal of the left subtree
#Recursively perform a postorder traversal of the right subtree
#Process the root node

#     10
#    /  \
#   5    15
#  / \   / \
# 3   7 12 18

#The postorder traversal would be: 3, 7, 5, 12, 18, 15, 10