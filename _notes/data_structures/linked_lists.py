#Linked List
#Linked lists are a linear data structure consisting of nodes. Each node contains a data element
#and a reference (pointer) to the next node in the sequence

#Unlike arrays, linked lists do not store elements in contiguous memory locations. Instead they use
#pointers to link nodes togeather forming a chain 

#Linked lists offer effcient insertion and deletion operations, especially at the beginning or middle
#of the list, but accessing elements by index can be less efficient that compared to arrays 


#Contiguous memory locations refers to a situation where the memory locations occupied by elements 
#of a data structure are adjacent to each other in memory

#Memory address:    1000   1001   1002   1003   1004
#Array elements:      1      2      3      4      5
 
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = new_node

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