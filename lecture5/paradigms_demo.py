"""
Course: ENPM605
Lecture: Advanced Functions
Section: Programming Paradigms

Author: zeidk
Created: 2026-02-23
"""

# # ──────────────────────────────────────────────
# # 📌 Snippet 1
# # ──────────────────────────────────────────────


# Pure function (no side effects, depends only on inputs)
def add(a: int, b: int) -> int:
    return a + b


# Impure function (side effect: modifies external state)
results = []


def add_and_store(a: int, b: int) -> int:
    result = a + b
    results.append(result)  # Side effect!
    return result
