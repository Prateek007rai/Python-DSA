# 🐍 Python Deep Guide

> (https://preview--pk-dsa.lovable.app/)
> (https://preview--pk-dsa-visuals.lovable.app/)
---

## 📌 Table of Contents

1. [Variables & Data Types](#1-variables--data-types)
2. [Strings & String Methods](#2-strings--string-methods)
3. [Type Conversion](#3-type-conversion)
4. [Lists & List Methods](#4-lists--list-methods)
5. [Tuples & Tuple Methods](#5-tuples--tuple-methods)
6. [Sets & Set Methods](#6-sets--set-methods)
7. [Dictionaries & Dict Methods](#7-dictionaries--dict-methods)
8. [List vs Tuple vs Set vs Dict — Comparison](#8-list-vs-tuple-vs-set-vs-dict--comparison)
9. [Slicing — Strings, Lists & Arrays](#9-slicing--strings-lists--arrays)
10. [Arrays (via `array` module)](#10-arrays-via-array-module)
11. [Loops & Iteration](#11-loops--iteration)
12. [Comprehensions](#12-comprehensions)
13. [Functions — Basics to Advanced](#13-functions--basics-to-advanced)
14. [Quick Cheat Sheet](#14-quick-cheat-sheet)

---

## 1. Variables & Data Types

```python
# Integer
age = 25

# Float
pi = 3.14159

# String
name = "Python"

# Boolean
is_active = True

# NoneType
nothing = None

# Check type
print(type(age))       # <class 'int'>
print(type(pi))        # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_active)) # <class 'bool'>
print(type(nothing))   # <class 'NoneType'>
```

---

## 2. Strings & String Methods

> Strings are **immutable** sequences of characters enclosed in `'single'`, `"double"`, or `"""triple"""` quotes.

### 2.1 Creating Strings

```python
s1 = 'Hello'
s2 = "World"
s3 = """Multi
line
string"""

# String repetition
print("Ha" * 3)   # HaHaHa

# String concatenation
print(s1 + " " + s2)  # Hello World
```

### 2.2 String Indexing

```python
word = "Python"
#       P  y  t  h  o  n
# idx:  0  1  2  3  4  5
# neg: -6 -5 -4 -3 -2 -1

print(word[0])   # P
print(word[-1])  # n
print(word[2])   # t
```

### 2.3 String Methods

```python
s = "  Hello, Python World!  "

# Case methods
print(s.upper())          # "  HELLO, PYTHON WORLD!  "
print(s.lower())          # "  hello, python world!  "
print(s.title())          # "  Hello, Python World!  "
print(s.swapcase())       # "  hELLO, pYTHON wORLD!  "
print(s.capitalize())     # "  hello, python world!  "

# Strip methods
print(s.strip())          # "Hello, Python World!"
print(s.lstrip())         # "Hello, Python World!  "
print(s.rstrip())         # "  Hello, Python World!"

# Search methods
print(s.find("Python"))   # 9  (index of first occurrence, -1 if not found)
print(s.index("World"))   # 16 (like find but raises ValueError if not found)
print(s.count("l"))       # 3

# Check methods
print("hello".isalpha())     # True  (only letters)
print("123".isdigit())       # True  (only digits)
print("abc123".isalnum())    # True  (letters + digits)
print("   ".isspace())       # True  (only whitespace)
print("Hello".startswith("He"))  # True
print("Hello".endswith("lo"))    # True

# Replace & Split
print("a-b-c".replace("-", "/"))    # a/b/c
print("a,b,c".split(","))           # ['a', 'b', 'c']
print("a,b,c".split(",", 1))        # ['a', 'b,c'] (maxsplit=1)
print(" ".join(["Hello", "World"])) # Hello World

# Alignment & Fill
print("Hi".center(10, "*"))   # ****Hi****
print("Hi".ljust(10, "-"))    # Hi--------
print("Hi".rjust(10, "-"))    # --------Hi
print("42".zfill(5))          # 00042

# Format
name = "Alice"
score = 95.5
print(f"Name: {name}, Score: {score:.2f}")   # f-string (recommended)
print("Name: {}, Score: {:.2f}".format(name, score))  # .format()
print("Name: %s, Score: %.2f" % (name, score))        # % formatting
```

---

## 3. Type Conversion

> Converting between `str`, `int`, `float`, and `bool`.

### 3.1 String → Number

```python
# str to int
s = "42"
n = int(s)
print(n)         # 42
print(type(n))   # <class 'int'>

# str to float
s2 = "3.14"
f = float(s2)
print(f)         # 3.14
print(type(f))   # <class 'float'>

# ⚠️ Invalid conversion raises ValueError
# int("3.14")   → ValueError
# int("abc")    → ValueError

# Safe conversion with try/except
try:
    result = int("hello")
except ValueError:
    print("Cannot convert 'hello' to int!")
```

### 3.2 Number → Float

```python
n = 10
f = float(n)
print(f)          # 10.0
print(type(f))    # <class 'float'>

# Arithmetic auto-converts to float
print(7 / 2)      # 3.5  (true division → float)
print(7 // 2)     # 3    (floor division → int)
```

### 3.3 Number → String

```python
n = 42
f = 3.14

s1 = str(n)
s2 = str(f)

print(s1)          # "42"
print(s2)          # "3.14"
print(type(s1))    # <class 'str'>

# Format with precision
print(f"{f:.4f}")  # "3.1400"

# Using repr() — gives eval-safe string
print(repr(42))    # '42'
```

### 3.4 Conversion Table

| From → To     | Function      | Example                        |
|---------------|---------------|--------------------------------|
| `str → int`   | `int(x)`      | `int("10")` → `10`            |
| `str → float` | `float(x)`    | `float("3.14")` → `3.14`     |
| `int → float` | `float(x)`    | `float(5)` → `5.0`           |
| `float → int` | `int(x)`      | `int(3.9)` → `3` (truncates) |
| `int → str`   | `str(x)`      | `str(42)` → `"42"`           |
| `float → str` | `str(x)`      | `str(3.14)` → `"3.14"`       |
| `any → bool`  | `bool(x)`     | `bool(0)` → `False`          |

---

## 4. Lists & List Methods

> Lists are **ordered**, **mutable**, and allow **duplicate** values. Defined with `[ ]`.

### 4.1 Creating Lists

```python
empty = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print(numbers[0])     # 1
print(nested[1][0])   # 3
```

### 4.2 List Methods

```python
fruits = ["banana", "apple", "cherry"]

# Add elements
fruits.append("mango")          # Add to end → ['banana', 'apple', 'cherry', 'mango']
fruits.insert(1, "grape")       # Insert at index 1 → ['banana', 'grape', 'apple', ...]
fruits.extend(["kiwi", "plum"]) # Add multiple elements

# Remove elements
fruits.remove("apple")   # Remove first occurrence by value
popped = fruits.pop()    # Remove & return last item
popped2 = fruits.pop(0)  # Remove & return item at index 0
fruits.clear()           # Remove ALL elements

# Search & Info
nums = [3, 1, 4, 1, 5, 9, 2, 6, 1]
print(nums.index(5))     # 4 (index of first '5')
print(nums.count(1))     # 3 (how many times '1' appears)

# Reorder
nums.sort()              # Sort ascending in-place → [1, 1, 1, 2, 3, 4, 5, 6, 9]
nums.sort(reverse=True)  # Sort descending in-place
nums.reverse()           # Reverse in-place

# Copy
original = [1, 2, 3]
shallow = original.copy()     # Shallow copy
import copy
deep = copy.deepcopy(original) # Deep copy (for nested lists)

# Sorted (non-destructive)
nums2 = [3, 1, 2]
sorted_nums = sorted(nums2)    # Returns NEW sorted list, original unchanged
```

---

## 5. Tuples & Tuple Methods

> Tuples are **ordered**, **immutable**, and allow **duplicates**. Defined with `( )`.

### 5.1 Creating Tuples

```python
empty = ()
single = (42,)         # ← comma is REQUIRED for single-element tuple
coords = (10.5, 20.3)
mixed = (1, "hello", 3.14)
nested = ((1, 2), (3, 4))
```

### 5.2 Tuple Methods

```python
t = (3, 1, 4, 1, 5, 9, 1)

# Only 2 methods!
print(t.count(1))   # 3 — count occurrences
print(t.index(5))   # 4 — index of first occurrence

# Tuple unpacking
x, y, z = (10, 20, 30)
print(x, y, z)   # 10 20 30

# Extended unpacking
a, *rest = (1, 2, 3, 4, 5)
print(a)     # 1
print(rest)  # [2, 3, 4, 5]

# Swap variables using tuple
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5

# Convert list ↔ tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)   # list → tuple
back_list = list(my_tuple)  # tuple → list
```

---

## 6. Sets & Set Methods

> Sets are **unordered**, **mutable**, have **no duplicates**, and are **NOT indexed**. Defined with `{ }`.

### 6.1 Creating Sets

```python
empty = set()          # ← NOT {} — that creates an empty dict!
nums = {1, 2, 3, 4, 5}
with_dupes = {1, 2, 2, 3, 3, 3}
print(with_dupes)      # {1, 2, 3} — duplicates auto-removed
```

### 6.2 Set Methods

```python
s = {1, 2, 3, 4, 5}

# Add / Remove
s.add(6)           # Add single element → {1,2,3,4,5,6}
s.remove(3)        # Remove element (raises KeyError if not found)
s.discard(99)      # Remove element (NO error if not found)
popped = s.pop()   # Remove & return arbitrary element
s.clear()          # Remove all elements

# Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)           # Union: {1,2,3,4,5,6}          → a.union(b)
print(a & b)           # Intersection: {3,4}            → a.intersection(b)
print(a - b)           # Difference: {1,2}              → a.difference(b)
print(a ^ b)           # Symmetric diff: {1,2,5,6}      → a.symmetric_difference(b)

# Subset / Superset
x = {1, 2}
y = {1, 2, 3, 4}
print(x.issubset(y))    # True  — all of x is in y
print(y.issuperset(x))  # True  — y contains all of x
print(x.isdisjoint(b))  # False — they share no common elements → False here

# Frozen set (immutable set)
frozen = frozenset({1, 2, 3})
# frozen.add(4)  → AttributeError — cannot modify
```

---

## 7. Dictionaries & Dict Methods

> Dicts are **ordered** (Python 3.7+), **mutable**, with **unique keys**. Defined with `{ key: value }`.

### 7.1 Creating Dicts

```python
empty = {}
person = {"name": "Alice", "age": 30, "city": "Delhi"}
from_keys = dict.fromkeys(["a", "b", "c"], 0)  # {'a':0, 'b':0, 'c':0}
nested = {
    "user": {
        "name": "Bob",
        "scores": [85, 92, 78]
    }
}

# Access
print(person["name"])            # Alice
print(person.get("age"))         # 30
print(person.get("email", "N/A")) # N/A (default if key missing)
```

### 7.2 Dict Methods

```python
d = {"a": 1, "b": 2, "c": 3}

# Views
print(d.keys())    # dict_keys(['a', 'b', 'c'])
print(d.values())  # dict_values([1, 2, 3])
print(d.items())   # dict_items([('a',1),('b',2),('c',3)])

# Add / Update
d["d"] = 4                  # Add new key
d.update({"e": 5, "f": 6}) # Add/update multiple keys
d["a"] = 99                 # Update existing key

# Remove
removed = d.pop("a")        # Remove key & return value → 99
d.popitem()                 # Remove & return LAST inserted (key, value) pair
d.clear()                   # Remove all

# Safe access with setdefault
d2 = {"x": 1}
d2.setdefault("y", 0)       # Adds 'y':0 only if 'y' doesn't exist
d2.setdefault("x", 99)      # Does nothing — 'x' already exists

# Copy
import copy
shallow = d2.copy()
deep = copy.deepcopy(d2)

# Merge dicts (Python 3.9+)
dict1 = {"a": 1}
dict2 = {"b": 2}
merged = dict1 | dict2     # {'a': 1, 'b': 2}
```

---

## 8. List vs Tuple vs Set vs Dict — Comparison

| Feature           | **List** `[]`        | **Tuple** `()`       | **Set** `{}`         | **Dict** `{k:v}`       |
|-------------------|----------------------|----------------------|----------------------|------------------------|
| **Ordered**       | ✅ Yes               | ✅ Yes               | ❌ No                | ✅ Yes (3.7+)          |
| **Mutable**       | ✅ Yes               | ❌ No                | ✅ Yes               | ✅ Yes                 |
| **Duplicates**    | ✅ Allowed           | ✅ Allowed           | ❌ Not allowed       | ❌ Keys must be unique |
| **Indexed**       | ✅ Yes               | ✅ Yes               | ❌ No                | ✅ By key              |
| **Syntax**        | `[1, 2, 3]`         | `(1, 2, 3)`         | `{1, 2, 3}`         | `{"a": 1}`            |
| **Use when**      | Order matters, need to modify | Fixed data, hashable keys | Unique items, set math | Key-value pairs       |
| **Speed (lookup)**| O(n)                | O(n)                | O(1) avg            | O(1) avg               |

```python
# Use list → shopping cart, tasks, ordered data
cart = ["apple", "banana", "apple"]  # duplicates OK

# Use tuple → GPS coordinates, RGB colors, DB records
point = (40.7128, -74.0060)

# Use set → remove duplicates, membership test, math ops
unique_ids = {101, 102, 103}

# Use dict → user profile, config, any key→value mapping
config = {"debug": True, "version": "3.11"}
```

---

## 9. Slicing — Strings, Lists & Arrays

> Syntax: `sequence[start : stop : step]`
> - `start` — index to begin (inclusive), default `0`
> - `stop`  — index to end (exclusive), default `len`
> - `step`  — how many to skip, default `1`

### 9.1 String Slicing

```python
s = "Hello, Python!"
#    0123456789...

print(s[0:5])      # "Hello"    → index 0 to 4
print(s[7:])       # "Python!"  → from index 7 to end
print(s[:5])       # "Hello"    → from start to index 4
print(s[-7:])      # "Python!"  → last 7 characters
print(s[::2])      # "Hlo yhn"  → every 2nd character
print(s[::-1])     # "!nohtyP ,olleH" → reversed string
print(s[7:13])     # "Python"
```

### 9.2 List Slicing

```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:6])     # [2, 3, 4, 5]
print(nums[:4])      # [0, 1, 2, 3]
print(nums[6:])      # [6, 7, 8, 9]
print(nums[::3])     # [0, 3, 6, 9]   → every 3rd
print(nums[::-1])    # [9, 8, 7, ... 0] → reversed
print(nums[1:8:2])   # [1, 3, 5, 7]

# Slice assignment — ONLY possible with lists (not strings/tuples)
nums[2:5] = [20, 30, 40]
print(nums)  # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

# Delete a slice
del nums[2:5]
print(nums)  # [0, 1, 5, 6, 7, 8, 9]

# Copy a list using slice
original = [1, 2, 3]
copy = original[:]   # Full copy — independent from original
```

### 9.3 Slice Object (Named Slice)

```python
# Reusable slice
first_three = slice(0, 3)
data = [10, 20, 30, 40, 50]
print(data[first_three])   # [10, 20, 30]

text = "Hello World"
print(text[first_three])   # "Hel"
```

---

## 10. Arrays (via `array` module)

> Python's `array` module stores **homogeneous** (same type) data — more memory-efficient than lists for large numeric data.

```python
import array

# Create array of integers ('i' = signed int)
arr = array.array('i', [1, 2, 3, 4, 5])

# Type codes:
# 'b' → signed char   | 'B' → unsigned char
# 'i' → signed int    | 'I' → unsigned int
# 'f' → float         | 'd' → double
# 'l' → signed long   | 'L' → unsigned long

print(arr[0])       # 1
print(arr[1:4])     # array('i', [2, 3, 4])

# Methods
arr.append(6)
arr.insert(0, 0)
arr.remove(3)          # Remove first occurrence of value 3
popped = arr.pop()     # Remove & return last element
print(arr.index(2))    # Index of first occurrence of 2
print(arr.count(1))    # Count occurrences

# Convert to list
as_list = arr.tolist()   # [0, 1, 2, 4, 5]

# Convert to bytes & back
byte_data = arr.tobytes()
new_arr = array.array('i')
new_arr.frombytes(byte_data)
```

> **💡 Tip:** For heavy numeric computing, prefer **NumPy arrays** over the `array` module:
> ```python
> import numpy as np
> np_arr = np.array([1, 2, 3, 4, 5])
> print(np_arr * 2)   # [2 4 6 8 10]  — vectorized ops
> ```

---

## 11. Loops & Iteration

### 11.1 For Loops

```python
# Loop over list
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# Loop with index using enumerate
for i, val in enumerate(["a", "b", "c"]):
    print(i, val)   # 0 a, 1 b, 2 c

# Loop over dict
d = {"name": "Alice", "age": 30}
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(f"{key}: {value}")

# Loop with range
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2): # 2, 4, 6, 8
    print(i)
```

### 11.2 While Loops

```python
count = 0
while count < 5:
    print(count)
    count += 1

# Loop control
for i in range(10):
    if i == 3:
        continue    # Skip this iteration
    if i == 7:
        break       # Exit loop
    print(i)
else:
    print("Loop finished normally")  # Runs if no break occurred
```

---

## 12. Comprehensions

> Elegant one-liner syntax to create collections.

```python
# List Comprehension
squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# With condition
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# Nested
matrix = [[j for j in range(3)] for i in range(3)]
# [[0,1,2], [0,1,2], [0,1,2]]

# Dict Comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
# {1:1, 2:4, 3:9, 4:16, 5:25}

# Set Comprehension
unique_lengths = {len(word) for word in ["hi", "hello", "hey", "world"]}
# {2, 5}

# Generator Expression (lazy evaluation — memory efficient)
total = sum(x**2 for x in range(1000000))  # Doesn't build full list in memory
```

---

## 13. Functions — Basics to Advanced

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!

# Default arguments
def power(base, exp=2):
    return base ** exp

print(power(3))     # 9   (exp defaults to 2)
print(power(2, 10)) # 1024

# *args — variable positional arguments
def total(*args):
    return sum(args)

print(total(1, 2, 3, 4))  # 10

# **kwargs — variable keyword arguments
def info(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {val}")

info(name="Alice", age=30, city="Delhi")

# Lambda — anonymous function
double = lambda x: x * 2
print(double(5))   # 10

# Used in sorted/filter/map
names = ["Charlie", "Alice", "Bob"]
print(sorted(names))                         # alphabetical
print(sorted(names, key=lambda x: len(x)))  # by length

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4, 6]
doubled = list(map(lambda x: x * 2, nums))         # [2, 4, 6, 8, 10, 12]
```

---

## 14. Quick Cheat Sheet

### String Methods Summary

| Method | Description | Example |
|---|---|---|
| `.upper()` | All uppercase | `"hi".upper()` → `"HI"` |
| `.lower()` | All lowercase | `"HI".lower()` → `"hi"` |
| `.strip()` | Remove whitespace | `" hi ".strip()` → `"hi"` |
| `.split(x)` | Split by x | `"a,b".split(",")` → `["a","b"]` |
| `.join(x)` | Join iterable | `",".join(["a","b"])` → `"a,b"` |
| `.replace(a,b)` | Replace a with b | `"hi".replace("h","H")` → `"Hi"` |
| `.find(x)` | Index of x (-1 if not found) | `"hello".find("l")` → `2` |
| `.count(x)` | Count occurrences | `"hello".count("l")` → `2` |
| `.startswith(x)` | Starts with x? | `"hello".startswith("he")` → `True` |
| `.endswith(x)` | Ends with x? | `"hello".endswith("lo")` → `True` |
| `.isdigit()` | All digits? | `"123".isdigit()` → `True` |
| `.isalpha()` | All letters? | `"abc".isalpha()` → `True` |

### Slicing Quick Reference

```
sequence[start:stop:step]

s[:]      → full copy
s[::-1]   → reversed
s[0:3]    → first 3 elements
s[-3:]    → last 3 elements
s[::2]    → every 2nd element
```

### Type Conversion Quick Reference

```python
int("42")       # "42"  → 42
float("3.14")   # "3.14"→ 3.14
str(42)         # 42    → "42"
float(5)        # 5     → 5.0
int(3.9)        # 3.9   → 3   (truncated!)
bool(0)         # 0     → False
bool("hello")   # any non-empty string → True
list((1,2,3))   # tuple → list
tuple([1,2,3])  # list  → tuple
set([1,2,2,3])  # list  → set (removes dupes)
```

---

*Made with ❤️ for Python learners. Happy coding!* 🐍
