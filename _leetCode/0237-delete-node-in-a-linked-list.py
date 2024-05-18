#Delete Node In A Linked List
#https://leetcode.com/problems/delete-node-in-a-linked-list/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None

        def setHead(self, head):
            self.head = head

        def findAndDelete(self, node):
            current = self.head
            while current:
                if current.val == node:
                    self.deleteNode(current)
                    break

                current = current.next

        def deleteNode(self, node):
            node.val = node.next.val
            node.next = node.next.next

        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")


caseHead_1 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
caseNode_1 = 5

caseHead_2 = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
caseNode_2 = 1

solution = Solution()

solution.setHead(caseHead_1)
solution.print_list()
solution.findAndDelete(caseNode_1)
solution.print_list()

solution.setHead(caseHead_2)
solution.print_list()
solution.findAndDelete(caseNode_2)
solution.print_list()
