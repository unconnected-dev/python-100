#Intersection Of Two Linked Lists
#https://leetcode.com/problems/intersection-of-two-linked-lists/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None
        
        def set_head(self, head):
            self.head = head
        
        def getIntersectionNode(self, headA, headB):
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

        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")

solution = Solution()

pointA = ListNode(8, ListNode(4, ListNode(5)))
listA =  ListNode(4, ListNode(1, pointA))
listB =  ListNode(5, ListNode(6, ListNode(1, pointA)))

solution.set_head(listA)
solution.print_list()

solution.set_head(listB)
solution.print_list()

print(f"{solution.getIntersectionNode(listA, listB).val}")
