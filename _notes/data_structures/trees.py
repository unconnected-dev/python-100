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
        self.value = val
        
class BinaryTree:
    def __init__(self) -> None:
        self.roof = None
    
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
            