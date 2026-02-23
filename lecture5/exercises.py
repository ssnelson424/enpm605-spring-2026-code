"""
Course: ENPM605
Lecture: Advanced Functions
Section: Exercises

Author: zeidk
Created: 2026-02-23
"""

# # ──────────────────────────────────────────────
# # 📌 Snippet 16
# # ──────────────────────────────────────────────

# 1. Create a lambda function that squares a number.
#    Assign it to a variable called 'square'.
#    Test it with: square(5) should return 25


# 2. Create a lambda function that takes two numbers and
#    returns their sum. Assign it to a variable called 'add'.
#    Test it with: add(3, 7) should return 10


# 3. Create a lambda function that checks if a number is even.
#    It should return True if even, False otherwise.
#    Assign it to a variable called 'is_even'.
#    Test it with: is_even(4) should return True


# 4. Create a lambda function that converts a string to uppercase.
#    Assign it to a variable called 'to_upper'.
#    Test it with: to_upper("hello") should return "HELLO"

# 5. Given this list of tuples representing (name, age):
#    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
#    a) Use sorted() with a lambda to sort by age (ascending)
#    b) Use sorted() with a lambda to sort by name length

# # ──────────────────────────────────────────────
# # 📌 Snippet 28
# # ──────────────────────────────────────────────

# 1. Write a decorator called 'greet' that prints
#    "Hello from [function_name]!" before executing the function.
#    Apply it to a function called 'say_goodbye()' that prints "Goodbye!".
#    When you call say_goodbye(), you should see:
#      Hello from say_goodbye!
#      Goodbye!


# 2. Write a decorator called 'repeat_twice' that executes
#    the decorated function two times.
#    Apply it to a function called 'print_message()' that prints "Hello".
#    When you call print_message(), you should see:
#      Hello
#      Hello


# 3. Write a decorator called 'uppercase_result' that converts
#    the return value of a function to uppercase.
#    Apply it to a function called 'get_name()' that returns "alice".
#    When you call get_name(), it should return "ALICE".

# # ──────────────────────────────────────────────
# # 📌 Snippet 33
# # ──────────────────────────────────────────────

# 1. Write a closure called 'make_accumulator' that takes
#    an initial value and returns a function.
#    Each call to the returned function adds its argument
#    to a running total and returns the new total.
#    acc = make_accumulator(100)
#    print(acc(10))  # 110
#    print(acc(20))  # 130

# 2. Use functools.partial to create a function 'log_info'
#    from a general 'log_message(level, msg)' function
#    with level fixed to "INFO".

# # ──────────────────────────────────────────────
# # 📌 Snippet 34
# # ──────────────────────────────────────────────
# Build a simple data processing pipeline using the
# concepts from this lecture.

# 1. Write a decorator 'log_call' that prints the function
#    name when called. Use @functools.wraps.

# 2. Write a closure 'make_filter(threshold)' that returns
#    a function. The returned function takes a list of
#    numbers and returns only those above the threshold.

# 3. Use functools.partial to create 'to_fahrenheit' and 'to_celsius' from:
#    def convert_temp(value, from_scale, to_scale): ...

# 4. Create a pipeline:
#    readings = [15.2, -3.0, 22.8, 8.1, -1.5, 30.0, 17.6]
#    a) Filter out negative readings using make_filter(0)
#    b) Convert to Fahrenheit using to_fahrenheit
#    c) Apply @log_call to the pipeline function
#    d) Sort results using sorted() with a lambda key
