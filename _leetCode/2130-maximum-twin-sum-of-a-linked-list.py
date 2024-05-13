#Maximum Twin Sum Of A Linked List
#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

caseHead_1 = [5,4,2,1]
caseHead_2 = [4,2,2,3]
caseHead_3 = [1,100000]

if True:
    def pairSum(head):
        current = head
        prev = None

        reverse = ListNode()
        while current:
            prev = current
            current = current.next

            reverse_ = ListNode()
            reverse_.val = prev.val
            reverse_.next = reverse
            reverse = reverse_

        res = 0
        current = head
        while current and reverse:
            res = max(res, current.val + reverse.val)
            current = current.next
            reverse = reverse.next
        
        return res