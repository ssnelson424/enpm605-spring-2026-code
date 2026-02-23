"""
Course: ENPM605
Lecture: Advanced Functions
Section: Callables

Author: zeidk
Created: 2026-02-23
"""

# # ──────────────────────────────────────────────
# # 📌 Snippet 2
# # ──────────────────────────────────────────────
def do_nothing():
    pass


print(callable(do_nothing))  # True
print(callable(lambda x: x))  # True
print(callable(int))  # True (classes are callable)
print(callable(42))  # False (integers are not callable)
print(callable("hello"))  # False
