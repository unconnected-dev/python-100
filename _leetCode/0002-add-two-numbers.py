#Add Two Numbers
#https://leetcode.com/problems/add-two-numbers/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None

        def addTwoNumbers(self, l1, l2):
            sl1 = ''
            sl2 = ''

            current = l1
            while current:
                sl1 += str(current.val)
                current = current.next

            current = l2
            while current:
                sl2 += str(current.val)
                current = current.next
            
            n1 = int(sl1[::-1])
            n2 = int(sl2[::-1])

            res = str(n1 + n2)[::-1]

            prev = ListNode()
            head = prev
            for c in res:
                new_node = ListNode(int(c))
                prev.next = new_node
                
                prev = new_node

            self.head = head.next
            return head.next


        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")


solution = Solution()

caseList1_1 = ListNode(2, ListNode(4, ListNode(3)))
caseList2_1 = ListNode(5, ListNode(6, ListNode(4)))

solution.addTwoNumbers(caseList1_1, caseList2_1)
solution.print_list()

caseList1_2 = ListNode(0)
caseList2_2 = ListNode(0)

solution.addTwoNumbers(caseList1_2, caseList2_2)
solution.print_list()

caseList1_3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
caseList2_3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

solution.addTwoNumbers(caseList1_3, caseList2_3)
solution.print_list()