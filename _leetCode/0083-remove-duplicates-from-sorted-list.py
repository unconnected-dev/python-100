#Remove Duplicates From Sorted List
#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

caseHead_1 = [1,1,2]
caseHead_2 = [1,1,2,3,3]

if False:
    def deleteDuplicates(head):
        curr = head
        
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next 
            
            curr = curr.next
            
        return head
    
if True:
    def deleteDuplicates(head):
        curr = head
        
        while curr and curr.next:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head