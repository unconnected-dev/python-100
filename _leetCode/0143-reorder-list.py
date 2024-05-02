#Reorder List
#https://leetcode.com/problems/reorder-list/description/

caseHead_1 = [1,2,3,4]
caseHead_2 = [1,2,3,4,5]

if True:
    def reorderList(head):
        p1, p2 = head, head
        values = []

        while p2:
            values.append(p2.val)
            p2 = p2.next

        left, right = 0, len(values) - 1        
        while left <= right:
            p1.val = values[left]
            p1 = p1.next
            if p1 is not None:
                p1.val = values[right]
                p1 = p1.next

            left += 1
            right -= 1
