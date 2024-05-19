#Remove Duplicates From Sorted List
#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
if False:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def deleteDuplicates(self, head):
            self.head = head
            curr = head
            
            while curr:
                while curr.next and curr.next.val == curr.val:
                    curr.next = curr.next.next 
                
                curr = curr.next
                
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
            
        def deleteDuplicates(self, head):
            self.head = head
            curr = head
            
            while curr and curr.next:
                if curr.next.val == curr.val:
                    curr.next = curr.next.next
                else:
                    curr = curr.next
            
            return head
    
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")
    
caseHead_1 = ListNode(1, ListNode(1, ListNode(2)))
caseHead_2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

solution = Solution()

solution.deleteDuplicates(caseHead_1)
solution.print_list()

solution.deleteDuplicates(caseHead_2)
solution.print_list()