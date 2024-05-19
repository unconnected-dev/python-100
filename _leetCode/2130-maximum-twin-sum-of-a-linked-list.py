#Maximum Twin Sum Of A Linked List
#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
if False:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def pairSum(self, head):
            self.head = head
            current = head
            prev = None

            reverse = ListNode()
            while current:
                prev = current
                current = current.next

                reverse_ = ListNode()
                reverse_.val = prev.val
                reverse_.next = reverse
                reverse = reverse_

            res = 0
            current = head
            while current and reverse:
                res = max(res, current.val + reverse.val)
                current = current.next
                reverse = reverse.next
            
            return res

        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")

if False:
    class Solution:
        def __init__(self) -> None:
            self.head = None
            
        def pairSum(self, head):
            self.head = head
            vals = []
            current = head

            while current:
                vals.append(current.val)
                current = current.next

            res = 0
            mid = len(vals)//2
            i, j = 0, len(vals) - 1
            while i <= mid:
                res = max(res, vals[i] + vals[j])
                i += 1
                j -=1
            
            return res

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
            
        def pairSum(self, head):
            self.head = head
            slow, fast = head, head
            
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            prev = None
            while slow:
                next = slow.next
                slow.next = prev
                prev = slow
                slow = next
            
            res = 0
            while prev:
                res = max(res, prev.val + head.val)
                prev = prev.next
                head = head.next
            
            return res
            
        def print_list(self):
            current_node = self.head
            while current_node:
                print(f"{current_node.val}", end=" -> ")
                current_node = current_node.next
                
            print(f"{None}")
    
caseHead_1 = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
caseHead_2 = ListNode(4, ListNode(2, ListNode(2, ListNode(3))))
caseHead_3 = ListNode(1, ListNode(100000))

solution = Solution()

print(f"{solution.pairSum(caseHead_1)}")
print(f"{solution.print_list()}")

print(f"{solution.pairSum(caseHead_2)}")
print(f"{solution.print_list()}")

print(f"{solution.pairSum(caseHead_3)}")
print(f"{solution.print_list()}")