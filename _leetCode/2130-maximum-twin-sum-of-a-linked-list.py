#Maximum Twin Sum Of A Linked List
#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

caseHead_1 = [5,4,2,1]
caseHead_2 = [4,2,2,3]
caseHead_3 = [1,100000]

if False:
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

if True:
    def pairSum(head):

        vals = []
        current = head

        while current:
            vals.append(current.val)
            current = current.next

        res = 0
        mid = len(vals)//2
        i, j = 0, len(vals) - 1
        while i <= mid:
            res = max(res, vals[i] + vals[j])
            i += 1
            j -=1
        
        return res
        