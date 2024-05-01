#Merge Two Sorted Lists
#https://leetcode.com/problems/merge-two-sorted-lists/description/

caseList1_1 = [1,2,4]
caseList2_1 = [1,3,4]

caseList1_2 = []
caseList2_2 = []

caseList1_3 = []
caseList2_3 = [0]

if True:
    def mergeTwoLists(list1, list2):
        dumm = ListNode()
        tail = dumm
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            tail = tail.next 
            
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dumm.next
