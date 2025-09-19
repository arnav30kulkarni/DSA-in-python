# fibonacci sequence 

# Base cases f(0)=0 and f(1)=1
# n>1 f(n)=f(n-1)+f(n-2)

# time complexity - O(2^N)
def f(n):
    #base cases
    if n==0:
        return 0 
    if n==1:
        return 1
    # actual logic
    if n>1:
        return f(n-1)+f(n-2)
    
print(f(10))

# reverse a linked list 

## creating a list 

class SinglyNode:
    def __init__(self,val,next=None):
        self.val = val 
        self.next = next

    def __str__(self):
        return str(self.val)

Head = SinglyNode(1)
A = SinglyNode(2)
B = SinglyNode(3)
C = SinglyNode(4)

Head.next = A 
A.next = B
B.next = C

## reversing the string 

# time complexity - O(N)
# space complexity - O(N)
def reverse(node):
    if not node:
        return 
    
    reverse(node.next)
    print(node)

reverse(Head)

        
