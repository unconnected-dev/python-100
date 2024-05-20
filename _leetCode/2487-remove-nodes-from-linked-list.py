#Remove Nodes From Linked List
#https://leetcode.com/problems/remove-nodes-from-linked-list/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Basic stack method means going from head to tail
#Updating the previous node .next to the current node 
if False:
    class Solution:
        def __init__(self) -> None:
            self.head = None
        
        def get_head(self):
            return self.head
        
        def removeNodes(self, head):
            my_stack = []
            current = head

            while current:
                
                while len(my_stack) > 0 and current.val > my_stack[-1].val:
                    my_stack.pop()

                if len(my_stack) > 0:
                    my_stack[-1].next = current

                my_stack.append(current)
                current = current.next
            
            self.head = my_stack[0]
            return my_stack[0]
        
        def generate_from_list(self, l):
            a_node = ListNode(l[0])
            self.head = a_node

            prev = self.head
            for i in range(1, len(l)):
                new_node = ListNode(l[i])
                prev.next = new_node
                prev = new_node  
            
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")

#Recursivly calling removeNodes will mean handling the tail first
if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None
        
        def get_head(self):
            return self.head
        
        def removeNodes(self, head):
            if not head: 
                return None

            head.next = self.removeNodes(head.next)

            if head.next and head.val < head.next.val:
                return head.next
                
            self.head = head
            return head
        
        def generate_from_list(self, l):
            a_node = ListNode(l[0])
            self.head = a_node

            prev = self.head
            for i in range(1, len(l)):
                new_node = ListNode(l[i])
                prev.next = new_node
                prev = new_node  
            
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")
            
solution = Solution()

solution.generate_from_list([5,2,13,3,8])
solution.print_list()
solution.removeNodes(solution.get_head())
solution.print_list()

solution.generate_from_list([1,1,1,1])
solution.print_list()
solution.removeNodes(solution.get_head())
solution.print_list()