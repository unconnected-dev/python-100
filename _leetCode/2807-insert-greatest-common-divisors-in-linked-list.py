#Insert Greatest Common Divisors In Linked List
#https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

caseHead_1 = [18,6,10,3]
caseHead_2 = [7]

if True:
    def insertGreatestCommonDivisors(head):
        curr = head

        while curr.next:
           curr.next, curr = ListNode(gcd(curr.val, curr.next.val), curr.next), curr.next

        return head

