#Reorder List
#https://leetcode.com/problems/reorder-list/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def reorderList(self, head):
            self.head = head
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

        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")
            
caseHead_1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
caseHead_2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

solution = Solution()

solution.reorderList(caseHead_1)
solution.print_list()

solution.reorderList(caseHead_2)
solution.print_list()