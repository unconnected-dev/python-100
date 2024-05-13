#Intersection Of Two Linked Lists
#https://leetcode.com/problems/intersection-of-two-linked-lists/description/

if True:
    def getIntersectionNode(headA, headB):
        my_set = set()
        current = headA
        while current:
            my_set.add(current)
            current = current.next

        current = headB
        while current:
            if current in my_set:
                break

            current = current.next
        
        if current:
            return current
        else:
            return None
