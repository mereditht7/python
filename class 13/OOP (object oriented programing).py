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

    def getIntersection(headA, headB):
        currentA = listA.head
        currentB = listB.head
        while currentA is not currentB:
            if currentA is None:
                currentA = listB.head
            else:
                currentA = currentA.next
            if currentB is None:
                currentB = listA.head
            else:
                currentB = currentB.next
        return currentA.data




ll=Linkedlist()


c = Node('c')
c1 = Node ('c1')
c2 = Node ('c2')

c.next = c1
c1.next = c2

a1 = Node('a')
a2 = Node ('a2')

a1.next = a2
a2.next = c

listA = Linkedlist()
listA.head = a1

b1 = Node('b1')
b2 = Node('b2')
b3 = Node('b3')

b1.next = b2
b2.next = b3
b3.next = c

listB = Linkedlist()
listB.head = b1

print(Linkedlist.getIntersection(listA.head, listB.head))