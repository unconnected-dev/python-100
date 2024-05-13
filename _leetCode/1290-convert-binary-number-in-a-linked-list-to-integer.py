#Convert Binary Number In A Linked List To Integer
#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

caseHead_1 = [1,0,1]
caseHead_2 = [0]

if True:
    def getDecimalValue(head):
        res = ''
        current = head
        while current:
            res += str(current.val)
            current = current.next

        return int(res,2)