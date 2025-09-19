# Recursion and Call Stacks in Python

This project demonstrates how **recursion** works in Python with two examples:
1. Computing Fibonacci numbers
2. Reversing a linked list

It also explains how the **call stack** executes recursive functions and why understanding base cases is critical.

---

## 🔁 What is Recursion?

Recursion is a programming technique where a function calls itself to solve a smaller subproblem until it reaches a **base case**. Each recursive call is stored on the **call stack** and resolved in reverse order (LIFO — Last In, First Out).

---

## 📌 Example 1: Fibonacci Sequence

### Problem
The Fibonacci sequence is defined as:
- Base cases:  
  `f(0) = 0`  
  `f(1) = 1`
- Recursive case:  
  `f(n) = f(n-1) + f(n-2)` for `n > 1`

### Call Stack Behavior
If you compute `f(5)`, the function expands like this:

f(5)
├─ f(4)
│ ├─ f(3)
│ │ ├─ f(2)
│ │ │ ├─ f(1) → 1
│ │ │ └─ f(0) → 0
│ │ └─ f(1) → 1
│ └─ f(2)
│ ├─ f(1) → 1
│ └─ f(0) → 0
└─ f(3)
├─ f(2)
│ ├─ f(1) → 1
│ └─ f(0) → 0
└─ f(1) → 1


### Complexity
- **Time Complexity**: `O(2^N)` (due to repeated subproblems)  
- **Space Complexity**: `O(N)` (maximum depth of recursion stack)

---

## 📌 Example 2: Reverse a Linked List

### Problem
Given a singly linked list, print its elements in reverse order using recursion.

### Call Stack Behavior
For a list:

Head → 1 → 2 → 3 → 4 → None


The recursive process looks like this:

reverse(1)
└─ reverse(2)
└─ reverse(3)
└─ reverse(4)
└─ reverse(None) → base case


When the recursion **unwinds**:

print(4)
print(3)
print(2)
print(1)

So, the list is **printed in reverse order**.  
⚠️ Important: This version **does not modify the list**, it only prints the nodes backwards.

### Complexity
- **Time Complexity**: `O(N)` (each node is visited once)  
- **Space Complexity**: `O(N)` (recursion stack holds `N` calls)

---

## ✅ Key Takeaways
- Each recursive call is placed on the **call stack** until the base case is reached.
- The base case prevents infinite recursion.
- Fibonacci recursion demonstrates **overlapping subproblems**, which makes it inefficient without optimization (e.g., memoization or dynamic programming).
- Linked list reversal demonstrates how recursion can naturally handle problems that require **backtracking**.
- Always analyze **time and space complexity** when writing recursive functions.

---
