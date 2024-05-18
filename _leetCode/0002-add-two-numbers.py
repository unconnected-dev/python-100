#Add Two Numbers
#https://leetcode.com/problems/add-two-numbers/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Goes through the two lists creating a string which are then reversed and added togeather
#After reverse the string again, then go through each character and create a new linked list
if False:
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

#Goes through the two linked lists and adds the numbers togeather
#Uses % and // to get what numbers needs to be put into the node and 
#what value needs to be carried over to the next node
if True:
    class Solution:
        def __init__(self) -> None:
            self.head = None

        def addTwoNumbers(self, l1, l2):
            nxt = ListNode()
            head = nxt
            total, carry = 0, 0

            while l1 or l2 or carry:
                total = carry

                if l1:
                    total += l1.val
                    l1 = l1.next

                if l2:
                    total += l2.val
                    l2 = l2.next
                
                num = total % 10
                carry = total // 10

                nxt.next = ListNode(num)
                nxt = nxt.next

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