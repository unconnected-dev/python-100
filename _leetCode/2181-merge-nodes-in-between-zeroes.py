#Merge Nodes In Between Zeros
#https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

caseHead_1 = [0,3,1,0,4,5,2,0]
caseHead_2 = [0,1,0,3,0,2,2,0]

if True:
    def mergeNodes(head):
        current = head.next
        last_zero = head
        while current:
            if current.val != 0:
                last_zero.val += current.val
            else:
                last_zero.next = current
                last_zero = current

            current = current.next

        current = head
        while current:
            if current.next.val == 0:
                current.next = None

            current = current.next

        return head