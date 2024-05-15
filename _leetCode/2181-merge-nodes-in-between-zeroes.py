#Merge Nodes In Between Zeros
#https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
if False:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
            self.head = head
            
            current = head.next
            last_zero = head
            while current:
                if current.val != 0:
                    last_zero.val += current.val
                else:
                    last_zero.next = current
                    last_zero = current

                current = current.next

            current = head
            while current:
                if current.next.val == 0:
                    current.next = None

                current = current.next

            return head
    
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")
            
if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
            total = 0
            
            p1, p2 = head, head.next
            
            while p2 is not None:
                if p2.val != 0:
                    total += p2.val
                else:
                    p1 = p1.next
                    p1.val = total
                    total = 0
                
                p2 = p2.next
            
            p1.next = None
            
            self.head = head.next
            return head.next
        
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")
            
caseHead_1 = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
caseHead_2 = ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))

solution = Solution()

solution.mergeNodes(caseHead_1)
print(f"{solution.print_list()}")

solution.mergeNodes(caseHead_2)
print(f"{solution.print_list()}")