# Binary Search

Binary Search is a classic divide-and-conquer algorithm used to efficiently locate an element or satisfy a condition within a **sorted array**.  
Instead of scanning elements one by one (linear search), binary search repeatedly divides the search interval in half, making it much faster.

---

## 1. Traditional Binary Search (Lookup in Array)

### **Definition**
Binary search works on sorted arrays. It finds the middle element and compares it with the target:
- If the target equals the middle element → found.
- If the target is smaller → search the left half.
- If the target is larger → search the right half.  
This continues until the element is found or the search space becomes empty.

### **When to Use**
- When the array is **sorted**.
- When you need to quickly check the **presence** of an element or retrieve its index/value.
- Suitable for large datasets where linear search would be inefficient.

### **Time Complexity**
- **Best Case:** `O(1)` → target is the middle element.
- **Average Case:** `O(log n)`
- **Worst Case:** `O(log n)`

### **Space Complexity**
- `O(1)` → iterative approach uses constant extra memory.

---

## 2. Binary Search on a Condition

### **Definition**
Instead of searching for a specific value, this variation searches for the **first index where a given condition becomes true**.  
Example: In a sorted boolean array `[False, False, False, True, True, True]`, binary search can efficiently find the index of the first `True`.

### **When to Use**
- When you need to **find a boundary or threshold** where a condition changes.
- Common in problems like:
  - Finding the minimum/maximum value that satisfies a constraint.
  - Lower bound / upper bound problems.
  - Optimization and search space problems in competitive programming.

### **Time Complexity**
- **Average/Worst Case:** `O(log n)`
- **Best Case:** `O(1)`

### **Space Complexity**
- `O(1)` → iterative approach.

---

## Summary

| Variant                     | Use Case                              | Time Complexity | Space Complexity |
|-----------------------------|----------------------------------------|----------------|-----------------|
| **Traditional Binary Search** | Find exact element in a sorted array  | `O(log n)`     | `O(1)`          |
| **Condition-based Binary Search** | Find boundary/first true condition   | `O(log n)`     | `O(1)`          |

---

## Key Notes
- Binary Search only works on **monotonic data** (sorted or conditionally ordered).
- If the input is not sorted, the results are **undefined**.
- Iterative binary search is preferred over recursive to save stack memory (`O(1)` vs `O(log n)`).
