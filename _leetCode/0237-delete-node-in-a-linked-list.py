#Delete Node In A Linked List
#https://leetcode.com/problems/delete-node-in-a-linked-list/description/

if True:
    def deleteNode(node):
        node.val = node.next.val
        node.next = node.next.next