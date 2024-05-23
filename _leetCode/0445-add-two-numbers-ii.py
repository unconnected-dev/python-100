#Add Two Numbers II
#https://leetcode.com/problems/add-two-numbers-ii/description/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None
        
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            current = l1
            n1 = ""
            while current:
                n1 += str(current.val)
                current = current.next

            current = l2
            n2 = ""
            while current:
                n2 += str(current.val)
                current = current.next
            
            n3 = [*str(int(n1) + int(n2))]
            dumm = ListNode()
            prev = dumm
            for n in n3:
                new_node = ListNode()
                new_node.val = int(n)
                prev.next = new_node
                prev = new_node
            
            self.print_list(dumm.next)
            return dumm.next
         
        def generate_from_list(self, l):
            a_node = ListNode(l[0])
            head = a_node
            prev = a_node
            for i in range(1, len(l)):
                new_node = ListNode(l[i])
                prev.next = new_node
                prev = new_node  
            
            return head
        
        def print_list(self, l):
            current_node = l
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")
            
solution = Solution()

casel1_1 = solution.generate_from_list([7,2,4,3])
casel2_1 = solution.generate_from_list([5,6,4])
solution.addTwoNumbers(casel1_1, casel2_1)

casel1_2 = solution.generate_from_list([2,4,3])
casel2_2 = solution.generate_from_list([5,6,4])
solution.addTwoNumbers(casel1_2, casel2_2)

