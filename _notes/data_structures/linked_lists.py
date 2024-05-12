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


    def append(self, data, at_beginning=False):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        elif at_beginning == True:
            current_head = self.head
            new_node.next = current_head
            self.head = new_node            
        else:
            self.tail.next = new_node
            self.tail = new_node

    def append_index(self, index, data):
        new_node = Node(data)
        
        if index < 0:
            print(f"Invalid index")
            return
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        prev_node = None
        current_node = self.head
        i = 0
        while current_node and i < index:
            i += 1
            prev_node = current_node
            current_node = current_node.next
        
        if current_node == None:
            print(f"Index out of range")
        else:
            prev_node.next = new_node
            new_node.next = current_node
        
    def delete_index(self, index):

        if index < 0:
            print(f"Invalid index")
            return
        
        if index == 0:
            if self.head:
                self.head = self.head.next
            else:
                print(f"List is empty")

        prev_node = None
        current_node = self.head
        i = 0 
        while current_node and i < index:
            i += 1
            prev_node = current_node
            current_node = current_node.next

        if current_node == None:
            print(f"Index out of range")

        prev_node.next = current_node.next
        if prev_node.next == None:
            self.tail = prev_node


    def delete_data(self, data):

        current_node = self.head
        if current_node.data == data:
            self.head = current_node.next
            return
        
        prev_node = None
        while current_node.next and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        
        if current_node == None:
            print(f"Data not found")

        prev_node.next = current_node.next
        if prev_node.next == None:
            self.tail = prev_node


    def delete_data_mod(self, data, delete_all=False):
        current_node = self.head
        prev_node = None

        while current_node:

            if current_node.data == data:
                if prev_node:
                    prev_node.next = current_node.next
                    if prev_node.next == None:
                        self.tail = prev_node

                else:
                    self.head = current_node.next
                
                if not delete_all:
                    return
            
            else:
                prev_node = current_node

            current_node = current_node.next


    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.data}", end=" -> ")
            current_node = current_node.next
            
        print(f"{None}")


my_list = LinkedList()
for n in range(10):
    my_list.append(n)

#Adding duplicate values for delete_all
# for n in range(10):
#     my_list.append(n)

my_list.print_list()

# my_list.delete_index(9)
# print(f"After deleting by index")
# my_list.print_list()

# my_list.delete_data(9)
# print(f"After deleting by data")
# my_list.print_list()

# my_list.delete_data_mod(9,delete_all=True)
# print(f"After deleting by data mod")
# my_list.print_list()