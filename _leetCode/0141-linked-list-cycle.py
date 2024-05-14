#Linked List Cycle
#https://leetcode.com/problems/linked-list-cycle/description/

caseHead_1 = [3,2,0,-4]
caseHead_2 = [1,2]
caseHead_3 = [1]

if True:
    def hasCycle(head):
        my_set = set()
        current = head
        while current:
            if current in my_set:
                return True
            my_set.add(current)
            current = current.next
        
        return False