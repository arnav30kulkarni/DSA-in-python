# Hash Tables in Python

## 1. What is a Hash Table?
A **hash table** is a data structure that stores key-value pairs.  
- It uses a **hash function** to convert a key into an index, where the value is stored.  
- Average time complexity for lookup, insert, and delete is **O(1)**.  
- Collisions (when two keys hash to the same index) are handled using techniques like chaining or open addressing.  

---

## 2. Hash Functions
A **hash function** takes input data (key) and produces a fixed-size integer (the hash).  

Requirements for a good hash function:
- **Deterministic**: Same input → same hash.
- **Uniform distribution**: Minimize collisions.
- **Efficient**: Quick to compute.

In Python, the built-in `hash()` function is used.

---

## 3. Hashable vs Non-Hashable Types

| Hashable Types                  | Non-Hashable Types |
|---------------------------------|---------------------|
| int                             | list                |
| float                           | dict                |
| complex                         | set                 |
| bool                            | bytearray           |
| str                             |                     |
| tuple (if all elements hashable)|                     |
| frozenset                       |                     |
| bytes                           |                     |
| None                            |                     |

---

## 4. Sets in Python
A **set** is an unordered collection of unique, hashable elements.  

### Key Features:
- No duplicates allowed.  
- Membership tests (`in`, `not in`) are **O(1)** on average.  
- Constructing from an iterable takes **O(N)**.  
- Iteration through a set takes **O(N)**.  

**Common Methods**:
- `add(item)` → Insert an element.
- `remove(item)` / `discard(item)` → Delete an element.
- `clear()` → Remove all elements.
- `union()`, `intersection()`, `difference()` → Set operations.

---

## 5. Dictionaries (Hash Maps) in Python
A **dictionary** (`dict`) is a hash map in Python: it stores **key-value pairs**.

### Key Features:
- Keys must be hashable.
- Values can be of any type.
- Average-case operations are **O(1)**.  

**Common Methods**:
- `d[key] = value` → Add/Update key-value pair.
- `d.get(key)` → Get value safely.
- `key in d` → Check presence of key.
- `d.keys()`, `d.values()`, `d.items()` → Access keys, values, and pairs.
- Iteration through dictionary → **O(N)**.

---

## 6. defaultdict
The `defaultdict` (from `collections`) provides a default value for missing keys.  
Example: `defaultdict(int)` gives `0` for missing numeric keys.

---

## 7. Counter
`Counter` (from `collections`) counts elements in an iterable and stores them as a dictionary.  
Example: `Counter("banana") → {'b':1, 'a':3, 'n':2}`.

---

## 8. Time Complexities

| Operation            | Set (`set`) | Dict (`dict`) |
|----------------------|-------------|---------------|
| Insertion            | O(1)        | O(1)          |
| Lookup (by key)      | O(1)        | O(1)          |
| Deletion             | O(1)        | O(1)          |
| Iteration            | O(N)        | O(N)          |

- `Counter` builds frequency counts in **O(N)** from an iterable, but single lookups and updates remain **O(1)**.

---

