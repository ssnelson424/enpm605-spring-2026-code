"""
Course: ENPM605
Lecture: Advanced Functions
Section: First-Class Functions

Author: zeidk
Created: 2026-02-23
"""

# # ──────────────────────────────────────────────
# # 📌 Snippet 3
# # ──────────────────────────────────────────────
# def compute_square(x):
#     return x**2


# # Assigning a function to a variable
# f = compute_square  # No parentheses! f is now the function object
# print(f(5))  # 25
# print(type(f))  # <class 'function'>


# # ──────────────────────────────────────────────
# # 📌 Snippet 4
# # ──────────────────────────────────────────────
# def apply_operation(func, a, b):
#     """Apply the given function to a and b."""
#     return func(a, b)


# def add(x, y):
#     return x + y


# def multiply(x, y):
#     return x * y


# print(apply_operation(add, 3, 4))  # 7
# print(apply_operation(multiply, 3, 4))  # 12


# # ──────────────────────────────────────────────
# # 📌 Snippet 5
# # ──────────────────────────────────────────────
# def make_multiplier(factor):
#     """Return a function that multiplies its input by factor."""

#     def multiply_value(x):
#         return x * factor

#     return multiply_value  # Return the inner function object


# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))  # 10
# print(triple(5))  # 15
# print(type(double))  # <class 'function'>


# # ──────────────────────────────────────────────
# # 📌 Snippet 6
# # ──────────────────────────────────────────────
# def add(a, b):
#     return a + b


# def multiply(a, b):
#     return a * b


# # Dispatch table: map operation names to functions
# operations = {
#     "add": add,
#     "multiply": multiply,
# }

# op_name = "multiply"
# result = operations[op_name](6, 7)
# print(f"{op_name}(6, 7) = {result}")  # multiply(6, 7) = 42


# # ──────────────────────────────────────────────
# # 📌 Snippet 7
# # ──────────────────────────────────────────────
# def compute_square(x):
#     return x**2


# nums = [1, 2, 3, 4, 5]
# squared = list(map(compute_square, nums))
# print(squared)  # [1, 4, 9, 16, 25]

# # Also works with built-in functions
# words = ["hello", "world"]
# upper_words = list(map(str.upper, words))
# print(upper_words)  # ['HELLO', 'WORLD']

# # ──────────────────────────────────────────────
# # 📌 Snippet 8
# # ──────────────────────────────────────────────
# def check_even(x):
#     return x % 2 == 0


# nums = [1, 2, 3, 4, 5, 6]
# evens = list(filter(check_even, nums))
# print(evens)  # [2, 4, 6]


# def check_positive(x):
#     return x > 0


# readings = [12.5, -3.1, 8.0, -0.5, 15.2]
# valid = list(filter(check_positive, readings))
# print(valid)  # [12.5, 8.0, 15.2]

# # ──────────────────────────────────────────────
# # 📌 Snippet 9
# # ──────────────────────────────────────────────
# # Sort strings by length
# words = ["banana", "apple", "cherry", "date"]
# by_length = sorted(words, key=len)
# print(by_length)  # ['date', 'apple', 'banana', 'cherry']


# # Sort tuples by second element using a named function
# def extract_score(pair):
#     return pair[1]


# students = [("Alice", 88), ("Bob", 95), ("Charlie", 72)]
# by_score = sorted(students, key=extract_score)
# print(by_score)  # [('Charlie', 72), ('Alice', 88), ('Bob', 95)]

# # Reverse order
# by_score_desc = sorted(students, key=extract_score, reverse=True)
# print(by_score_desc)  # [('Bob', 95), ('Alice', 88), ('Charlie', 72)]

# # ──────────────────────────────────────────────
# # 📌 Snippet 10
# # ──────────────────────────────────────────────
# nums = [1, 2, 3, 4, 5]

# # Using map + filter
# result_1 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
# print(result_1)  # [4, 16]

# # Using list comprehension (preferred)
# result_2 = [x**2 for x in nums if x % 2 == 0]
# print(result_2)  # [4, 16]
