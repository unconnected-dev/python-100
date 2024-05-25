#Invert Binary Tree
#https://leetcode.com/problems/invert-binary-tree/description/

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
            if self.root is None:
                self.root = TreeNode(val)
            else:
                self.insert_recursive(self.root, val)
        
        def insert_recursive(self, node, val):
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

        def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
            if not root:
                return root

            self.invertTree(root.left)
            self.invertTree(root.right)

            root.left, root.right = root.right, root.left

            return root
        
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


tree = Solution()

elements = [4,2,7,1,3,6,9]
for el in elements:
    tree.insert(el)

tree.print_tree(tree.get_root())
tree.invertTree(tree.get_root())
tree.print_tree(tree.get_root())
tree.delete_tree()

print()
print("******************************")
elements = [2,1,3]
for el in elements:
    tree.insert(el)

tree.print_tree(tree.get_root())
tree.invertTree(tree.get_root())
tree.print_tree(tree.get_root())
tree.delete_tree()

print()
print("******************************")
elements = []
for el in elements:
    tree.insert(el)

tree.print_tree(tree.get_root())
tree.invertTree(tree.get_root())
tree.print_tree(tree.get_root())
