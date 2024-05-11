#Linked List

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.data}", end=" -> ")
            current_node = current_node.next
            
        print(f"{None}")

my_list = LinkedList()
for n in range(10):
    my_list.append(n)

my_list.print_list()