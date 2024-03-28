#Middle Of The Linked List
#https://leetcode.com/problems/middle-of-the-linked-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    if False:
        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            last = head
            middle = head

            while last and last.next:
                middle = middle.next
                last = last.next.next
            
            return middle

    if True:
        def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            fast = head
            slow = head

            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
            
            return slow

caseHead_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
caseHead_2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))

solution = Solution()

print(f"{solution.middleNode(caseHead_1).val}")
print(f"{solution.middleNode(caseHead_2).val}")