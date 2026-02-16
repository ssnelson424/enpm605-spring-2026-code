# ──────────────────────────────────────────────
# 📌 Snippet 6 - Exercise 1
# ──────────────────────────────────────────────
# 1. Write a function called 'calculate_rectangle_metrics' that takes
#    'length' and 'width' as parameters and returns both
#    the area and the perimeter as a tuple.
#    Include a Google-style docstring.

# 2. Call the function with length=7 and width=4.
#    Unpack the results into separate variables.
#    Print both values using f-strings.

# 3. Write a function called 'is_even' that takes an integer
#    and returns True if it is even, False otherwise.
#    Then call it with 10 and 7 and print the results.

# ──────────────────────────────────────────────
# 📌 Snippet 20 - Exercise 2
# ──────────────────────────────────────────────
# 1. Write a function called 'build_profile' that accepts
#    a first name and last name as positional arguments,
#    and any number of keyword arguments.
#    It should return a dictionary containing the first name,
#    last name, and all additional keyword-value pairs.

# Example usage:
# profile = build_profile("albert", "einstein",
#                         field="physics", location="princeton")
# print(profile)
# {'first': 'albert', 'last': 'einstein',
#  'field': 'physics', 'location': 'princeton'}

# 2. Create a dictionary with keyword arguments and call
#    build_profile by unpacking it.

# ──────────────────────────────────────────────
# 📌 Snippet 41 - Exercise 3
# ──────────────────────────────────────────────
# Write a function called sum_digits that takes a positive integer as input and returns the sum of its digits using recursion.
# Hints:
# - Base case: if n < 10, return n (single digit)
# - Recursive case: last digit is n % 10
#   remaining digits are n // 10

# Expected behavior:
# sum_digits(123)  -> 6   (1 + 2 + 3)
# sum_digits(456)  -> 15  (4 + 5 + 6)
# sum_digits(789)  -> 24  (7 + 8 + 9)

# ──────────────────────────────────────────────
# 📌 Snippet 42 - Exercise 4
# ──────────────────────────────────────────────
# # Predict the output on paper first, then verify by running
# x = 10
# data = {"count": 0}


# def outer():
#     x = 20
#     data["count"] += 1

#     def inner():
#         nonlocal x
#         x += 5
#         data["count"] += 1
#         print(f"inner: x={x}, data={data}")

#     inner()
#     print(f"outer: x={x}, data={data}")


# outer()
# print(f"global: x={x}, data={data}")