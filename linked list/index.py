# singly linked list

class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

# create nodes
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(6)
C = SinglyNode(7)

# connect nodes
Head.next = A
A.next = B
B.next = C

# traverse (O(N))
curr = Head
while curr:
    print(curr)
    curr = curr.next

# display linked list (O(N))
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(elements))

# call display
display(Head)


# Search for node value - O(n)
def search(head,val):
    curr=head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next

    return False

print(search(Head,7))

# Doubly linked list 

class DoublyNode:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return(str(self.val))        
    
head = tail = DoublyNode(1)
    
# display - O(N)
def display(head):
    curr = head
    elements=[]
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))

display(head)

# inserting at the beginning -O(1)

def insert_at_beginning(head,tail,val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
display(head)