class Node: 
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addtoend(self, data):
        new_node = Node(data)
        #data is what is added
        #creating a new node that currently doesn't have any data - but it has access to class node which contains self data and self next
        if not self.head:
            #check to make sure that the linked list is not empty
            self.head = new_node
            #what if it is empty? should set current node (new_node) as the head of the linked list
            return None
            #because we set this new node as the head, we want the code to end
        
        current = self.head
        while current.next: #while there exists a current.next, we want to move from the current to the end of the list
            current = current.next
            #this us moving from the front of the list to the very end of the list
        current.next = new_node
        new_node.prev = current
        print("added item to linked list")




dll=DoublyLinkedList()

dll.addtoend(10)
dll.addtoend(20)

print(dll.addtoend(30))

