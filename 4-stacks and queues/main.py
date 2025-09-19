# stacks 
# follow LIFO - last in first out 

stk = [] 

# append to the top of the stack - O(1)
stk.append(5)
print(stk)

# pop from the stack - O(1)
arr=[12,1,23,4,5]
x = arr.pop()
print(x)
print(arr)

#ask what is on the top of the stack- O(1)
print(arr[-1])

# ask if something in the stack - O(1)

if arr:
    print(True)

# queues 
#follow FIFO- first in first out 

from collections import deque

q = deque()
print(q)

# Enqueue - Add a element to the right - O(1)
q.append(5)
q.append(3)
q.append(7)
print(q)

#dequeue- Remove element from the left-O(1)
q.popleft()
print(q)

# peak from left side and right side - O(1)
print(q[0])
print(q[-1])
