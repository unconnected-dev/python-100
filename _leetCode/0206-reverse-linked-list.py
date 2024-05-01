#Reverse Linked List
#https://leetcode.com/problems/reverse-linked-list/description/

caseHead_1 = [1,2,3,4,5]
caseHead_2 = [1,2]
caseHead_3 = []

if False:
    def reverseList(head):
        curr = head
        prev = None
        next = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr            
            
            curr = next
            
        return prev
    
if True:
    def reverseList(head):
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev