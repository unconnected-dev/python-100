#Linked List Cycle
#https://leetcode.com/problems/linked-list-cycle/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
if False:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def hasCycle(self, head):
            self.head = head
            my_set = set()
            current = head
            while current:
                if current in my_set:
                    return True
                my_set.add(current)
                current = current.next
            
            return False
    
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
            
        def hasCycle(self, head):
            self.head = head
            fast = head
            slow = head
            
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
            
            return False
    
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")

#Examples not looping same as in leetcode
caseHead_1 = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))

point_1 = ListNode(1)
point_2 = ListNode(2)
point_1.next = point_2
point_2.next = point_1
caseHead_2 = point_1

caseHead_3 = ListNode(1)

solution = Solution()

print(f"{solution.hasCycle(caseHead_1)}")
solution.print_list()

#print_list would infinite loop in this case
print(f"{solution.hasCycle(caseHead_2)}")
# solution.print_list()

print(f"{solution.hasCycle(caseHead_3)}")
solution.print_list()