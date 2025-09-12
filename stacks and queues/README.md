# Stacks and Queues in Python

This project demonstrates **Stack** and **Queue** data structures in Python, along with their basic operations and time complexities.

---

## 📚 Stacks

A **stack** follows the **LIFO (Last In, First Out)** principle.  
The element that is added last is the one removed first.

### Operations:
- **Push**: Add an element to the top of the stack.  
- **Pop**: Remove the element from the top of the stack.  
- **Peek/Top**: Look at the top element without removing it.  
- **Check if Empty**: Verify whether the stack contains elements.

Stacks in Python are typically implemented using a `list`, since `append()` and `pop()` on the end of a list run in constant time.

Push → add on top
Pop → remove from top


---

## 📚 Queues

A **queue** follows the **FIFO (First In, First Out)** principle.  
The element that is added first is the one removed first.

### Operations:
- **Enqueue**: Add an element to the right side of the queue.  
- **Dequeue**: Remove an element from the left side of the queue.  
- **Peek**: Look at the first or last element without removing it.  
- **Check if Empty**: Verify whether the queue contains elements.

Queues in Python are typically implemented using `collections.deque`, which provides efficient O(1) operations from both ends.

### Visual:

Queue (FIFO):

Front → [ 5 ] [ 3 ] [ 7 ] ← Rear

Enqueue → add to rear
Dequeue → remove from front


---

## ⏱️ Time Complexity

| Operation        | Stack (`list`) | Queue (`deque`) |
|------------------|----------------|-----------------|
| Push / Append    | O(1)           | O(1)            |
| Pop              | O(1)           | O(1) (from left with `popleft`) |
| Peek / Top       | O(1)           | O(1)            |
| Check Empty      | O(1)           | O(1)            |

---

## ✅ Key Points
- Use **list** for stack-like behavior.  
- Use **deque** for queue-like behavior (more efficient than `list.pop(0)` for FIFO).  
- Both support constant time operations for push, pop, and peek.  
- Good to know: Python also has `queue.Queue`, which is thread-safe and useful in multithreaded programs, but less lightweight than `deque`.

---
