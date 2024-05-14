#Palindrome Linked List
#https://leetcode.com/problems/palindrome-linked-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if False:
    class Solution:
        def getMiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            last = head
            middle = head

            while last and last.next:
                middle = middle.next
                last = last.next.next

            return middle

        def reversedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head

            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            return prev

        def isPalindrome(self, head: Optional[ListNode]) -> bool:
            middleNode = self.getMiddleNode(head)
            fromStart = head
            fromEnd = self.reversedList(middleNode)

            while fromEnd != None:
                if fromStart.val != fromEnd.val:
                    return False

                fromEnd = fromEnd.next
                fromStart = fromStart.next
            
            return True

if True:
    class Solution:
        def isPalindrome(self, head: Optional[ListNode]) -> bool:
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            prev = None
            while slow:
                t = slow.next
                slow.next = prev
                prev = slow
                slow = t
            
            while head and prev:
                if head.val != prev.val:
                    return False

                head = head.next
                prev = prev.next

caseHead_1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
caseHead_2 = ListNode(1, ListNode(2))

solution = Solution()

print(f"{solution.isPalindrome(caseHead_1)}")
print(f"{solution.isPalindrome(caseHead_2)}")