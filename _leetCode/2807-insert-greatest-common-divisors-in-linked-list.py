#Insert Greatest Common Divisors In Linked List
#https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

from math import gcd


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def insertGreatestCommonDivisors(self, head):
            self.head = head
            curr = head

            while curr.next:
                curr.next, curr = ListNode(gcd(curr.val, curr.next.val), curr.next), curr.next

            return head
        
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")

caseHead_1 = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
caseHead_2 = ListNode(7)

solution = Solution()

solution.insertGreatestCommonDivisors(caseHead_1)
print(f"{solution.print_list()}")

solution.insertGreatestCommonDivisors(caseHead_2)
print(f"{solution.print_list()}")