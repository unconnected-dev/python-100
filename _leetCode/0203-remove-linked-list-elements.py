#Remove Linked List Elements
#https://leetcode.com/problems/remove-linked-list-elements/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if True:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        prev = None
        current = head
        while current:
            if current.val == val:
                if prev:
                    prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        
        return head