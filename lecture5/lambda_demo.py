"""
Course: ENPM605
Lecture: Advanced Functions
Section: Lambda Functions

Author: zeidk
Created: 2026-02-23
"""

# # ──────────────────────────────────────────────
# # 📌 Snippet 11
# # ──────────────────────────────────────────────
# # Regular function
# def add(a, b):
#     return a + b


# # Equivalent lambda
# add_lambda = lambda a, b: a + b

# print(add(3, 4))  # 7
# print(add_lambda(3, 4))  # 7

# # ──────────────────────────────────────────────
# # 📌 Snippet 12
# # ──────────────────────────────────────────────
# # Sort a list of tuples by the second element
# pairs = [(1, "banana"), (3, "apple"), (2, "cherry")]
# sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
# print(sorted_pairs)
# # [(3, 'apple'), (1, 'banana'), (2, 'cherry')]

# # Sort robots by speed (descending)
# robots = [
#     {"name": "TurtleBot", "speed": 0.26},
#     {"name": "Spot", "speed": 1.6},
#     {"name": "Atlas", "speed": 2.5},
# ]
# fastest_first = sorted(robots, key=lambda r: r["speed"], reverse=True)
# for r in fastest_first:
#     print(f"  {r['name']}: {r['speed']} m/s")

# # ──────────────────────────────────────────────
# # 📌 Snippet 13
# # ──────────────────────────────────────────────
# # Convert sensor readings from Celsius to Fahrenheit
# celsius = [0.0, 20.0, 37.5, 100.0]
# fahrenheit = list(map(lambda c: c * 9 / 5 + 32, celsius))
# print(fahrenheit)  # [32.0, 68.0, 99.5, 212.0]

# # Filter out negative sensor readings
# readings = [12.5, -3.1, 8.0, -0.5, 15.2]
# valid = list(filter(lambda x: x >= 0, readings))
# print(valid)  # [12.5, 8.0, 15.2]

# # ──────────────────────────────────────────────
# # 📌 Snippet 14
# # ──────────────────────────────────────────────
# # Lambda with a default parameter
# compute_power = lambda base, exp=2: base**exp
# print(compute_power(3))  # 9
# print(compute_power(3, 3))  # 27

# # ──────────────────────────────────────────────
# # 📌 Snippet 15
# # ──────────────────────────────────────────────
# # Conditional expression in a lambda (valid)
# classify = lambda x: "positive" if x > 0 else "non-positive"
# print(classify(5))  # "positive"
# print(classify(-3))  # "non-positive"

# # Multi-line logic is NOT possible in a lambda
# # Use a regular function instead
