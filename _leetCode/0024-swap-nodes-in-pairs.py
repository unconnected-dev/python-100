#Swap Nodes In Pairs
#https://leetcode.com/problems/swap-nodes-in-pairs/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def swapPairs(self, head):
            
            if not head:
                return head
            
            prev, current, start = None, head, head.next              
            while current and current.next:
                goto = current.next
                if prev:
                    prev.next = goto
                
                current.next, goto.next = goto.next, current
                prev, current = current, current.next
        
            self.head = start or head
            return start or head
        
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")
            
caseHead_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

caseHead_2 = ListNode()
caseHead_3 = ListNode(1)

solution = Solution()

solution.swapPairs(caseHead_1)
solution.print_list()

solution.swapPairs(caseHead_2)
solution.print_list()

solution.swapPairs(caseHead_3)
solution.print_list()