#Convert Binary Number In A Linked List To Integer
#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def getDecimalValue(self, head: ListNode) -> int:
            self.head = head
            res = ''
            current = head
            while current:
                res += str(current.val)
                current = current.next
            
            return int(res, 2)
        
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")

caseHead_1 = ListNode(1, ListNode(0, ListNode(1)))
caseHead_2 = ListNode(7)

solution = Solution()

solution.getDecimalValue(caseHead_1)
print(f"{solution.print_list()}")

solution.getDecimalValue(caseHead_2)
print(f"{solution.print_list()}")