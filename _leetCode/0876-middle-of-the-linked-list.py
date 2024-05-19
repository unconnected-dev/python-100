#Middle Of The Linked List
#https://leetcode.com/problems/middle-of-the-linked-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
if False:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            last = head
            middle = head

            while last and last.next:
                middle = middle.next
                last = last.next.next
            
            return middle

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
            self.middle = None
            
        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            self.head = head
            fast = head
            slow = head

            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
            
            self.middle = slow
            return slow

        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")
        
        def get_middle(self):
            return self.middle.val
        
caseHead_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
caseHead_2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

solution = Solution()

solution.middleNode(caseHead_1)
solution.print_list()
print(f"{solution.get_middle()}")

solution.middleNode(caseHead_2)
solution.print_list()
print(f"{solution.get_middle()}")