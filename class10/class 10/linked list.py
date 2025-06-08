class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        #data is what is added
        #creating a new node that currently doesn't have any data - but it has access to class node which contains self data and self next
        if not self.head:
            #check to make sure that the linked list is not empty
            self.head = new_node
            #what if it is empty? should set current node (new_node) as the head of the linked list
            return
            #because we set this new node as the head, we want the code to end
        
        current = self.head
        while current.next: #while there exists a current.next, we want to move from the current to the end of the list
            current = current.next
            #this us moving from the front of the list to the very end of the list
        current.next = new_node
        print("added item to linked list")
   
    def insert_at_beginning(self, data):
        new_node = Node (data)
        new_node.next = self.head
        self.head= new_node
        #make a new node
        #set this node as the head


    def print_list(self):
        current = self.head

        while(current):
            print(current.data, end = ' -> ')
            current = current.next
        print("None")
        
    def search(self,key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
    
    def delete_first_node (self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return ("successfully deleted")
        
    def delete_specific_node (self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return ("successfully deleted")
        previous = None
        while current and current.data != key:
            previous = current
            current = current.next
        if current:
            previous.next = current.next

    def reverse_linkedlist (self):
        current = self.head
        previous = None
        next.node = current.next
        current = previous

        while current:
            current.next = previous

        self.head = current

    def find_middle (self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
        if slow:
            return (slow.data)
        return None
    
    def find_kth_term (self, k):
        slow = self.head
        fast = self.head
        for x in range (k):
            fast = fast.next
        while fast: 
            slow = slow.next
            fast = fast.next

        return (slow.data)
    
    def detect_cycle (self):
        slow =  self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print ("they are equal")
                return True
        
        print ("they are not equal")
        return False



ll=Linkedlist()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)

first = ll.head
second = first.next
third = second.next
fourth = third.next

fourth.next = second

print(ll.detect_cycle())

