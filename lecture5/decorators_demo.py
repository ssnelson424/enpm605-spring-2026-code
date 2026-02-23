"""
Course: ENPM605
Lecture: Advanced Functions
Section: Decorators

Author: zeidk
Created: 2026-02-23
"""

import time
from functools import wraps

# # ──────────────────────────────────────────────
# # 📌 Snippet 20
# # ──────────────────────────────────────────────
# def trace_calls(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")

#     return wrapper


# def say_hello():
#     print("Hello!")


# # Manually applying the decorator
# say_hello = trace_calls(say_hello)
# say_hello()


# # ──────────────────────────────────────────────
# # 📌 Snippet 21
# # ──────────────────────────────────────────────
# def trace_calls(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")

#     return wrapper


# @trace_calls
# def say_hello():
#     print("Hello!")


# # This is equivalent to: say_hello = trace_calls(say_hello)
# say_hello()
# # Before the function call
# # Hello!
# # After the function call


# # ──────────────────────────────────────────────
# # 📌 Snippet 22
# # ──────────────────────────────────────────────
# def trace_calls(func):
#     def wrapper():
#         print("Before the function call")
#         func()
#         print("After the function call")

#     return wrapper


# @trace_calls
# def greet(name):
#     print(f"Hello, {name}!")


# greet("Alice")
# # TypeError: wrapper() takes 0 positional arguments but 1 was given


# # ──────────────────────────────────────────────
# # 📌 Snippet 23
# # ──────────────────────────────────────────────
# def trace_calls(func):
#     def wrapper(*args, **kwargs):
#         print(f"Before calling {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"After calling {func.__name__}")
#         return result

#     return wrapper


# @trace_calls
# def greet(name):
#     print(f"Hello, {name}!")


# @trace_calls
# def say_hello():
#     print("Hello!")


# greet("Alice")
# say_hello()


# # ──────────────────────────────────────────────
# # 📌 Snippet 24
# # ──────────────────────────────────────────────
# def measure_time(func):
#     """Measure and print the execution time of a function."""

#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         elapsed = time.perf_counter() - start
#         print(f"{func.__name__} took {elapsed:.4f}s")
#         return result

#     return wrapper


# @measure_time
# def compute_sum(n: int) -> int:
#     """Compute sum of range(n)."""
#     return sum(range(n))


# print(compute_sum.__name__)  # 'wrapper'  (not 'compute_sum'!)
# print(compute_sum.__doc__)  # None       (docstring is lost!)


# # ──────────────────────────────────────────────
# # 📌 Snippet 25
# # ──────────────────────────────────────────────
# def measure_time(func):
#     @wraps(func)  # Copies metadata from func to wrapper
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         elapsed = time.perf_counter() - start
#         print(f"{func.__name__} took {elapsed:.4f}s")
#         return result

#     return wrapper


# @measure_time
# def compute_sum(n: int) -> int:
#     """Compute sum of range(n)."""
#     return sum(range(n))


# print(compute_sum.__name__)  # 'compute_sum'
# print(compute_sum.__doc__)  # 'Compute sum of range(n).'

# print(compute_sum(1_000_000_000))


# # ──────────────────────────────────────────────
# # 📌 Snippet 26
# # ──────────────────────────────────────────────
# def apply_bold(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return f"<b>{func(*args, **kwargs)}</b>"

#     return wrapper


# def apply_italic(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return f"<i>{func(*args, **kwargs)}</i>"

#     return wrapper


# # @apply_bold @apply_italic def greet <=> greet = apply_bold(apply_italic(greet))
# @apply_bold  # executed second
# @apply_italic  # executed first
# def greet(name):
#     return f"Hello, {name}"


# print(greet("Alice")) # <b><i>Hello, Alice</i></b>


# # ──────────────────────────────────────────────
# # 📌 Snippet 27
# # ──────────────────────────────────────────────
# def repeat(n: int):
#     """Decorator factory: repeat the function call n times."""

#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             result = None
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result

#         return wrapper

#     return decorator


# @repeat(3)
# def say_hello():
#     print("Hello!")


# say_hello()
# # Hello!
# # Hello!
# # Hello!
