#Merge Two Sorted Lists
#https://leetcode.com/problems/merge-two-sorted-lists/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if False:
    class Solution:
        def __init__(self) -> None:
            self.head = None

        def mergeTwoLists(self, list1, list2):
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

        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")    

if True:

    class Solution:
        def __init__(self) -> None:
            self.head = None

        def setHead(self, head):
            self.head = head

        def mergeTwoLists(self, list1, list2):
            if list1 is None:
                return list2
                
            if list2 is None:
                return list1
            
            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
    
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")    


caseList1_1 = ListNode(1, ListNode(2, ListNode(4)))
caseList2_1 = ListNode(1, ListNode(3, ListNode(4)))

caseList1_2 = ListNode()
caseList2_2 = ListNode()

caseList1_3 = ListNode()
caseList2_3 = ListNode(0)


solution = Solution()

solution.setHead(solution.mergeTwoLists(caseList1_1, caseList2_1))
solution.print_list()

solution.setHead(solution.mergeTwoLists(caseList1_2, caseList2_2))
solution.print_list()

solution.setHead(solution.mergeTwoLists(caseList1_3, caseList2_3))
solution.print_list()