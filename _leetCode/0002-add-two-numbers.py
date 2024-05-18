#Add Two Numbers
#https://leetcode.com/problems/add-two-numbers/description/

if True:
    def addTwoNumbers(l1, l2):
        sl1 = ''
        sl2 = ''

        current = l1
        while current:
            sl1 += current.val
            current = current.next

        current = l2
        while current:
            sl2 += current.val
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

        return head.next


