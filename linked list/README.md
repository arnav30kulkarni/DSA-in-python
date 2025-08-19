# Linked List in Python

This project demonstrates **Singly Linked List** and **Doubly Linked List** in Python.  
It covers creation of nodes, traversal, searching, and insertion operations.

---

## 📌 What is a Linked List?
A **Linked List** is a linear data structure where elements (**nodes**) are connected using pointers.  
Each node typically contains:
- **Value** → data stored in the node
- **Next** → reference (pointer) to the next node
- **Prev** (in doubly linked list) → reference to the previous node

Unlike arrays:
- Linked lists do **not** use indexes
- Size is **dynamic**
- Insertion/deletion does **not require shifting** elements

---

## 🔗 Types of Linked Lists

### Singly Linked List
- Each node stores `value` + pointer to the **next** node.
- Traversal is **one-way** (head → tail).
- Example:

> Head -> 1 -> 3 -> 6 -> 7 -> None


---

### Doubly Linked List
- Each node stores `value` + pointer to **next** and **previous** nodes.
- Traversal can happen **both ways**.
- Example:

> Head <-> 3 <-> 1 <-> Tail 


---

## ⚡ Operations Implemented

### Singly Linked List
- Create nodes and connect them
- Traverse and display all nodes
- Search for a node by value

### Doubly Linked List
- Create nodes and connect them
- Traverse and display all nodes
- Insert at the beginning

---

## ⏱ Time Complexity

| Operation                | Singly Linked List | Doubly Linked List |
|--------------------------|--------------------|--------------------|
| Traversal (Display)      | **O(N)**           | **O(N)**           |
| Search                   | **O(N)**           | **O(N)**           |
| Insert at Beginning      | **O(1)**           | **O(1)**           |
| Insert at End (with tail)| **O(N)**           | **O(1)**           |
| Delete Node              | **O(N)**           | **O(N)**           |

---

## 🚀 Why Linked Lists?
- Dynamic memory usage (no fixed size like arrays).
- Efficient insertions/deletions compared to arrays.
- Basis for stacks, queues, graphs, and memory management systems.

---




