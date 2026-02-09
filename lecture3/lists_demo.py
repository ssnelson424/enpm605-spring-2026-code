"""
ENPM605 - Python Applications for Robotics
Lecture 3: Python Fundamentals — Part II
Spring 2026 | University of Maryland

Section: Lists
"""

# ============================================================
# List Basics
# ============================================================

# ──────────────────────────────────────────────
# 📌 Snippet 21 — List Basics
# ──────────────────────────────────────────────
# Lists can contain any objects
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

# Lists with same items in different order are different
a = [1, 2, 3]
b = [3, 2, 1]
print(a == b)  # False


# # ============================================================
# # Creating Lists
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 22--25 — Ways to Create Lists
# # ──────────────────────────────────────────────
# # Square brackets with comma-separated values
# fruits = ["apple", "banana", "cherry"]
# empty = []

# # list() constructor with an iterable
# chars = list("hello")       # ['h', 'e', 'l', 'l', 'o']
# nums = list(range(5))       # [0, 1, 2, 3, 4]
# empty = list()              # []

# # List comprehension
# squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# # Repetition operator
# zeros = [0] * 5             # [0, 0, 0, 0, 0]

# print(chars)
# print(nums)
# print(squares)
# print(zeros)


# # ============================================================
# # Indexing and Slicing
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 26 — List Indexing and Slicing
# # ──────────────────────────────────────────────
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# # Indexing
# print(fruits[0])      # apple
# print(fruits[-1])     # elderberry

# # Slicing
# print(fruits[1:4])    # ['banana', 'cherry', 'date']
# print(fruits[::2])    # ['apple', 'cherry', 'elderberry']

# # Modifying elements (lists are mutable!)
# fruits[0] = "apricot"
# print(fruits)         # ['apricot', 'banana', 'cherry', 'date', 'elderberry']

# # Modifying slices
# fruits[1:3] = ["blueberry"]
# print(fruits)         # ['apricot', 'blueberry', 'date', 'elderberry']


# # ============================================================
# # Iterating Over Lists
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 27 — Iterating Over Lists
# # ──────────────────────────────────────────────
# fruits = ["apple", "banana", "cherry"]

# # Direct iteration (preferred)
# for fruit in fruits:
#     print(fruit)

# # With index using enumerate()
# for i, fruit in enumerate(fruits):
#     print(f"{i}: {fruit}")

# # Using range() when you need the index
# for i in range(len(fruits)):
#     print(f"Item {i} is {fruits[i]}")

# # Building a list with a loop
# squares = []
# for x in range(5):
#     squares.append(x ** 2)
# print(squares)  # [0, 1, 4, 9, 16]


# # ============================================================
# # List Methods - Adding Elements
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 28-30 — Adding Elements to Lists
# # ──────────────────────────────────────────────
# # append(x) — Add item to end
# fruits = ["apple"]
# fruits.append("banana")
# print(fruits)  # ['apple', 'banana']

# # extend(iterable) — Add all items
# fruits = ["apple"]
# fruits.extend(["kiwi", "mango"])
# print(fruits)  # ['apple', 'kiwi', 'mango']

# # insert(i, x) — Insert at position
# fruits = ["apple", "cherry"]
# fruits.insert(1, "banana")
# print(fruits)  # ['apple', 'banana', 'cherry']


# # ============================================================
# # List Methods - Removing Elements
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 31-33 — Removing Elements from Lists
# # ──────────────────────────────────────────────
# # remove(x) — Remove first occurrence
# fruits = ["apple", "banana", "apple"]
# fruits.remove("apple")
# print(fruits)  # ['banana', 'apple']

# # pop([i]) — Remove and return item
# fruits = ["apple", "banana"]
# last = fruits.pop()    # 'banana'
# print(last)
# print(fruits)  # ['apple']

# fruits = ["apple", "banana", "cherry"]
# first = fruits.pop(0)  # 'apple'
# print(first)
# print(fruits)  # ['banana', 'cherry']

# # clear() — Remove all items
# fruits = ["apple", "banana"]
# fruits.clear()
# print(fruits)  # []


# # ============================================================
# # List Methods - Searching and Sorting
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippets 34-37 — Searching and Sorting Lists
# # ──────────────────────────────────────────────
# # index(x) — Return index of first occurrence
# nums = [10, 20, 30, 20]
# print(nums.index(20))  # 1

# # count(x) — Count occurrences
# nums = [1, 2, 2, 3, 2]
# print(nums.count(2))  # 3

# # sort() — Sort in-place
# nums = [3, 1, 4, 1, 5]
# nums.sort()                    # nums is now [1, 1, 3, 4, 5]
# print(nums)
# nums.sort(reverse=True)        # nums is now [5, 4, 3, 1, 1]
# print(nums)

# # sorted() — Return new sorted list (out-of-place)
# original = [3, 1, 4]
# new_list = sorted(original)    # new_list is [1, 3, 4], original unchanged
# print(original)
# print(new_list)

# # reverse() — Reverse in-place
# nums = [1, 2, 3]
# nums.reverse()
# print(nums)  # [3, 2, 1]


# # ============================================================
# # List Comprehensions
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 38 — List Comprehensions
# # ──────────────────────────────────────────────
# # Basic comprehension
# squares = [x**2 for x in range(5)]
# print(squares)  # [0, 1, 4, 9, 16]

# # With condition (filtering)
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)  # [0, 2, 4, 6, 8]

# # With transformation
# words = ["hello", "world"]
# upper = [w.upper() for w in words]
# print(upper)  # ['HELLO', 'WORLD']

# # Conditional expression (ternary in comprehension)
# labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# print(labels)  # ['even', 'odd', 'even', 'odd', 'even']


# # ============================================================
# # Shallow vs Deep Copy
# # ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 39 — Shallow Copy
# # ──────────────────────────────────────────────
# from copy import copy

# a = [1, [2, 3]]
# b = copy(a) # from copy import copy  
# # or b=a.copy() or b=list(a) or b=a[:]
# b[0] = 99
# b[1].append(4)

# print(a)  # [1, [2, 3, 4]]  -- nested list was modified!
# print(b)  # [99, [2, 3, 4]]


# # ──────────────────────────────────────────────
# # 📌 Snippet 40 — Deep Copy
# # ──────────────────────────────────────────────
# from copy import deepcopy

# a = [1, [2, 3]]
# b = deepcopy(a)
# b[0] = 99
# b[1].append(4)

# print(a)  # [1, [2, 3]]     -- original unchanged!
# print(b)  # [99, [2, 3, 4]]


# # ──────────────────────────────────────────────
# # 📌 Assignment Creates Alias (NOT a copy!)
# # ──────────────────────────────────────────────
# a = [1, 2, 3]
# b = a  # b is an alias for a, NOT a copy

# b.append(4)
# print(a)  # [1, 2, 3, 4]  -- a is also modified!
# print(b)  # [1, 2, 3, 4]
# print(a is b)  # True - they are the same object
