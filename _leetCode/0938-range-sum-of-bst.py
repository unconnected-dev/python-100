#Range Sum Of BST
#https://leetcode.com/problems/range-sum-of-bst/description/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
        def __init__(self) -> None:
            self.root = None
            self.low = None
            self.high = None
        
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

        def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
            
            if root == None:
                return 0

            if root.val < low:
                return self.rangeSumBST(root.right, low, high)

            if root.val > high:
                return self.rangeSumBST(root.left, low, high)

            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

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

elements = [10,5,15,3,7,None,18]
for el in elements:
    tree.insert(el)

caseLow_1 = 7
caseHigh_1 = 15

tree.print_tree(tree.get_root())
print(f"{tree.rangeSumBST(tree.get_root(), caseLow_1, caseHigh_1)}")
tree.delete_tree()