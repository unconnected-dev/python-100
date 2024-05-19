#Reverse Linked List
#https://leetcode.com/problems/reverse-linked-list/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
if False:
    class Solution:
        def __init__(self) -> None:
            self.head = None
        
        def reverseList(self, head):
            curr = head
            prev = None
            next = None
            
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr            
                
                curr = next
                
            return prev
        
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
            
        def reverseList(self, head):
            curr = head
            prev = None
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            self.head = prev
            return prev
        
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")
    
caseHead_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
caseHead_2 = ListNode(1, ListNode(2))
caseHead_3 = ListNode()

solution = Solution()
solution.reverseList(caseHead_1)
solution.print_list()

solution.reverseList(caseHead_2)
solution.print_list()

solution.reverseList(caseHead_3)
solution.print_list()