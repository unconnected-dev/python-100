#Maximum Depth Of A Binary Tree
#https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if True:
    class Solution:
            def __init__(self) -> None:
                self.root = None
            
            def get_root(self):
                return self.root

            def set_root(self, root):
                self.root = root

            def insert(self, val):
                if val is None:
                    return 
                
                if self.root is None:
                    self.root = TreeNode(val)
                else:
                    self.insert_recursive(self.root, val)
            
            def insert_recursive(self, node, val):
                if val is None:
                    return 
                
                if val < node.val:
                    if node.left is None:
                        node.left = TreeNode(val)
                    else:
                        self.insert_recursive(node.left, val)
                        
                else:
                    if node.right is None:
                        node.right = TreeNode(val)
                    else:
                        self.insert_recursive(node.right, val)
                            
            def maxDepth(self, root: Optional[TreeNode]) -> int:

                if root is None:
                    return 0
                    
                l = self.maxDepth(root.left) if root.left is not None else 0
                r = self.maxDepth(root.right) if root.right is not None else 0 

                self.depth = 0 + max(l, r)

                if root is not None:
                    return self.depth + 1
                    
            def print_tree(self, node, level=0, prefix="Root: "):
                if node is not None:
                    print(" " * (level * 4) + prefix + str(node.val))
                    if node.left is not None or node.right is not None:
                        if node.left:
                            self.print_tree(node.left, level + 1, "L--- ")
                        else:
                            print(" " * ((level + 1) * 4) + "L--- None")
                        if node.right:
                            self.print_tree(node.right, level + 1, "R--- ")
                        else:
                            print(" " * ((level + 1) * 4) + "R--- None")

            def delete_tree(self):
                self.delete_tree_recursive(self.root)
                self.root = None

            def delete_tree_recursive(self, node):
                if node is not None:
                    self.delete_tree_recursive(node.left)
                    self.delete_tree_recursive(node.right)

                    node.left = None
                    node.right = None
                    node.val = None


#I think my insert function is incorrect as it is creating a different tree to leetcodes
#in the first case but the solution is still working

tree = Solution()

elements = [3,9,20,None,None,15,7]
for el in elements:
    tree.insert(el)

tree.print_tree(tree.get_root())
print(f"{tree.maxDepth(tree.get_root())}")
tree.delete_tree()


print()
print("******************************")
elements = [1,None,2]
for el in elements:
    tree.insert(el)

tree.print_tree(tree.get_root())
print(f"{tree.maxDepth(tree.get_root())}")
tree.delete_tree()


print()
print("******************************")
elements = []
for el in elements:
    tree.insert(el)

tree.print_tree(tree.get_root())
print(f"{tree.maxDepth(tree.get_root())}")
tree.delete_tree()
