"""
Course: ENPM605
Lecture: Advanced Functions
Section: Closures

Author: zeidk
Created: 2026-02-23
"""


# # ──────────────────────────────────────────────
# # 📌 Snippet 17
# # ──────────────────────────────────────────────
# def make_greeter(greeting):
#     """Return a function that greets with the given greeting."""

#     def greet(name):
#         return f"{greeting}, {name}!"

#     return greet


# hello = make_greeter("Hello")
# howdy = make_greeter("Howdy")

# print(hello("Alice"))  # Hello, Alice!
# print(howdy("Bob"))  # Howdy, Bob!


# # ──────────────────────────────────────────────
# # 📌 Snippet 18
# # ──────────────────────────────────────────────
# def make_logger(prefix: str):
#     """Return a logging function with a fixed prefix."""

#     def log(message: str) -> None:
#         print(f"[{prefix}] {message}")

#     return log


# info = make_logger("INFO")
# error = make_logger("ERROR")
# debug = make_logger("DEBUG")

# info("System started")  # [INFO] System started
# error("Sensor timeout")  # [ERROR] Sensor timeout
# debug("x = 42")  # [DEBUG] x = 42


# # ──────────────────────────────────────────────
# # 📌 Snippet 19
# # ──────────────────────────────────────────────
# def make_counter(start=0):
#     """Return a counter function that increments on each call."""
#     count = start

#     def increment():
#         nonlocal count
#         count += 1
#         return count

#     return increment


# counter_a = make_counter()
# print(counter_a())  # 1
# print(counter_a())  # 2
# print(counter_a())  # 3

# counter_b = make_counter(10)
# print(counter_b())  # 11
