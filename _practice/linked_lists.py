
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def generate_from_list(self, l):
        
        a_node = Node(l[0])
        self.head = a_node

        prev = self.head
        for i in range(1, len(l)):
            new_node = Node(l[i])
            prev.next = new_node
            prev = new_node            
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.data}", end=" -> ")
            current_node = current_node.next
            
        print(f"{None}")
        
a_list = [1,2,3,4,5]

new_linked_list = LinkedList()
new_linked_list.generate_from_list(a_list)
new_linked_list.print_list()