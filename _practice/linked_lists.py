

if False:
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

if True:
    class Node:
        def __init__(self, val) -> None:
            self.val = val
            self.prev = None
            self.next = None
    
    class DoubleLinkedList:
        def __init__(self) -> None:
            self.head = None
            self.tail = None
        
        def generate_from_list(self, arr):

            a_node = Node(arr[0])
            self.head = a_node

            prev = self.head
            for i in range(1, len(arr)):
                new_node = Node(arr[i])
                new_node.prev = prev

                prev.next = new_node

                prev = new_node

            self.tail = prev

        def delete_data(self, data):
            current = self.head
            prev = None

            if current.val == data:

                if current.next:
                    nxt = current.next
                    self.head = nxt
                    nxt.prev = None
                    return
                else:
                    self.head = None
                    self.tail = None
                    return
                
            while current:
                if current.val == data:
                    nxt = current.next

                    if prev != None:
                        prev.next = nxt

                    if nxt != None:    
                        nxt.prev = prev
                    
                    if current == self.tail:
                        self.tail = prev

                    return

                prev = current
                current = current.next


        def print_list(self):
            current = self.head

            while current:
                print(f"{current.val}", end ='->')
                current = current.next
            
            print(f"{None}")
    
        def print_list_reverse(self):
            current = self.tail

            while current:
                print(f"{current.val}", end="<-")
                current = current.prev
            
            print(f"{None}")

    a_list = [1,2,3,4,5]

    new_linked_list = DoubleLinkedList()
    new_linked_list.generate_from_list(a_list)
    new_linked_list.print_list()
    # new_linked_list.print_list_reverse()

    new_linked_list.delete_data(3)
    new_linked_list.print_list()
    new_linked_list.print_list_reverse()