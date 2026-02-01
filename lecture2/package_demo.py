"""
ENPM605 - Python Applications for Robotics
L2: Python Fundamentals — Part I
Spring 2026 | University of Maryland

Code snippets and exercises from Lecture 2.
Run each section to follow along with the slides.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ============================================================
# SECTION 1: PACKAGES AND MODULES
# ============================================================
# (See slides for full package/directory examples)

print("=" * 60)
print("SECTION 1: PACKAGES AND MODULES")
print("=" * 60)

# --- Import strategies ---

# Approach 1 — Full module path
import shape.square
print(shape.square.compute_area(4))

# # Approach 2 — Alias
# import shape.circle as ci
# print(ci.compute_area(5))

# # Approach 3 — Import specific names
# from shape.triangle import compute_area, compute_perimeter
# print(compute_area(3, 4))
# print(compute_perimeter(3, 4, 5))


# # --- Demonstrating __init__.py usage ---
# # In a package structure:
# #   lecture2/
# #       __init__.py
# #       shape/
# #           __init__.py
# #           square.py    -> contains compute_area(a), compute_perimeter(a)
# #           triangle.py  -> contains compute_area(base, h), compute_perimeter(a,b,c)
# # You would import with:
# #   from shape.square import compute_area
# #   from shape.triangle import compute_perimeter


# # ============================================================
# # SECTION 2: INDENTATION
# # ============================================================

# print("\n" + "=" * 60)
# print("SECTION 2: INDENTATION")
# print("=" * 60)

# # Python uses indentation to define code blocks
# # ALWAYS use 4 spaces per level (PEP 8)

# def greeting(name: str) -> None:
#     """Demonstrate indentation with nested blocks."""
#     print(f"Hello, {name}")
#     if name == "Alice":
#         print("Welcome back!")  # 2 levels of indentation

# greeting("Alice")
# greeting("Bob")


# # ============================================================
# # SECTION 3: OPERATORS
# # ============================================================

# print("\n" + "=" * 60)
# print("SECTION 3: OPERATORS")
# print("=" * 60)

# # --- 3.1 Arithmetic Operators ---
# print("\n--- Arithmetic Operators ---")

# print(f"7 + 3 = {7 + 3}")
# print(f"7 - 3 = {7 - 3}")
# print(f"7 * 3 = {7 * 3}")
# print(f"7 / 3 = {7 / 3}")       # Always float division
# print(f"7 // 3 = {7 // 3}")     # Floor division
# print(f"7 % 3 = {7 % 3}")       # Modulus (remainder)
# print(f"2 ** 10 = {2 ** 10}")   # Exponentiation

# # Floor division rounds toward negative infinity
# print(f"10 // 3 = {10 // 3}")    # 3
# print(f"10 // -3 = {10 // -3}")  # -4 (not -3!)

# # Augmented assignment operators
# x: int = 10
# x += 5   # x = x + 5
# print(f"After x += 5: {x}")
# x *= 2   # x = x * 2
# print(f"After x *= 2: {x}")


# # --- 3.2 Relational (Comparison) Operators ---
# print("\n--- Relational Operators ---")

# a: int = 5
# b: int = 3

# print(f"a={a}, b={b}")
# print(f"a == b: {a == b}")   # False
# print(f"a != b: {a != b}")   # True
# print(f"a > b:  {a > b}")    # True
# print(f"a < b:  {a < b}")    # False
# print(f"a >= 5: {a >= 5}")   # True
# print(f"a <= b: {a <= b}")   # False

# # Chained comparisons (Pythonic!)
# x = 5
# print(f"1 < x < 10: {1 < x < 10}")   # True
# print(f"1 < x > 3:  {1 < x > 3}")    # True


# # --- 3.3 Logical Operators ---
# print("\n--- Logical Operators ---")

# a_bool: bool = True
# b_bool: bool = False

# print(f"True and False: {a_bool and b_bool}")    # False
# print(f"True or False:  {a_bool or b_bool}")     # True
# print(f"not True:       {not a_bool}")            # False

# # Short-circuit evaluation
# x = 5
# print(f"x > 0 and x < 10: {x > 0 and x < 10}")    # True
# print(f"x > 10 or x == 5: {x > 10 or x == 5}")    # True

# # Logical operators with non-boolean values
# print(f'"hello" and 0:    {"hello" and 0}')       # 0
# print(f'"hello" or 0:     {"hello" or 0}')        # "hello"
# print(f'not "":           {not ""}')               # True
# print(f'0 or "default":   {0 or "default"}')      # "default"
# print(f'"hello" and "world": {"hello" and "world"}')  # "world"


# # --- 3.4 Membership Operators ---
# print("\n--- Membership Operators ---")

# x = "hello"
# print(f'"h" in "hello":      {"h" in x}')       # True
# print(f'"he" in "hello":     {"he" in x}')      # True
# print(f'"O" in "hello":      {"O" in x}')       # False (case-sensitive)
# print(f'"z" not in "hello":  {"z" not in x}')   # True


# # --- 3.5 Identity Operators ---
# print("\n--- Identity Operators ---")

# a_list: list = [1, 2, 3]
# b_list: list = [1, 2, 3]
# c_list: list = a_list

# print(f"a == b: {a_list == b_list}")  # True (same values)
# print(f"a is b: {a_list is b_list}")  # False (different objects)
# print(f"a is c: {a_list is c_list}")  # True (same object)


# # --- Exercise 1: Operators ---
# print("\n--- Exercise 1: Operators ---")
# print("Predict each output before looking!")

# print(f"17 // 5 = {17 // 5}")
# print(f"17 % 5 = {17 % 5}")
# print(f"2 ** 0.5 = {2 ** 0.5}")
# print(f"-7 // 2 = {-7 // 2}")
# print(f'0 or "default" = {0 or "default"}')
# print(f'"hello" and "world" = {"hello" and "world"}')
# print(f"not [] = {not []}")
# x = 15
# print(f"10 < 15 < 20 = {10 < x < 20}")
# print(f"10 < 15 > 20 = {10 < x > 20}")


# # ============================================================
# # SECTION 4: BOOLEAN TYPE
# # ============================================================

# print("\n" + "=" * 60)
# print("SECTION 4: BOOLEAN TYPE")
# print("=" * 60)

# # bool is a subclass of int
# print(f"True + True = {True + True}")    # 2
# print(f"True * 10 = {True * 10}")        # 10
# print(f"isinstance(True, int) = {isinstance(True, int)}")  # True

# # --- Falsy values ---
# print("\n--- Falsy values ---")
# print(f"bool(0):     {bool(0)}")       # False
# print(f"bool(0.0):   {bool(0.0)}")     # False
# print(f'bool(""):    {bool("")}')      # False
# print(f"bool([]):    {bool([])}")      # False
# print(f"bool({{}}):  {bool({})}")      # False
# print(f"bool(None):  {bool(None)}")    # False

# # --- Truthy values ---
# print("\n--- Truthy values ---")
# print(f"bool(1):     {bool(1)}")       # True
# print(f"bool(-2):    {bool(-2)}")      # True
# print(f'bool("hi"):  {bool("hi")}')   # True
# print(f'bool(" "):   {bool(" ")}')    # True (space is not empty!)
# print(f"bool([1]):   {bool([1])}")    # True

# # Pythonic truthiness usage
# my_list: list = [1, 2, 3]
# if my_list:  # Instead of: if len(my_list) > 0
#     print("List is not empty (Pythonic style)")


# # ============================================================
# # SECTION 5: NUMERIC TYPES
# # ============================================================

# print("\n" + "=" * 60)
# print("SECTION 5: NUMERIC TYPES")
# print("=" * 60)

# # --- Integer type ---
# print("\n--- Integer Type ---")

# # Python ints have unlimited precision
# big: int = 10**100
# print(f"10^100 has {len(str(big))} digits")
# print(f"type(big) = {type(big)}")

# # Type conversion
# print(f"int(3.7) = {int(3.7)}")            # 3 (truncates toward zero)
# print(f"int('42') = {int('42')}")           # 42
# print(f"int('101011', 2) = {int('101011', 2)}")  # 43 (binary to int)

# # --- Float type ---
# print("\n--- Float Type ---")

# # Floating-point precision issues
# print(f"0.1 + 0.2 = {0.1 + 0.2}")                # 0.30000000000000004
# print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}")   # False!

# # The safe way to compare floats
# import math
# print(f"math.isclose(0.1 + 0.2, 0.3): {math.isclose(0.1 + 0.2, 0.3)}")  # True

# # Type conversion
# print(f'float("3.5") = {float("3.5")}')
# print(f"float(3) = {float(3)}")
# print(f'float("inf") = {float("inf")}')

# # --- Interning ---
# print("\n--- Interning (CPython optimization) ---")

# # Integer interning
# a, b = 20, 20
# print(f"20 is 20: {a is b}")   # True (cached)

# # String interning
# a_str: str = "hello"
# b_str: str = "hello"
# c_str: str = "h" + "ello"  # Compile-time concatenation
# d_str: str = "".join(["h", "e", "l", "l", "o"])  # Runtime

# print(f'"hello" is "hello" (literal): {a_str is b_str}')  # True
# print(f'"h"+"ello" is "hello" (compile-time): {a_str is c_str}')  # True
# print(f'join() result is "hello" (runtime): {a_str is d_str}')  # False

# import sys
# e_str: str = sys.intern(d_str)
# print(f"After sys.intern(): {a_str is e_str}")  # True


# # ============================================================
# # SECTION 6: STRING TYPE
# # ============================================================

# print("\n" + "=" * 60)
# print("SECTION 6: STRING TYPE")
# print("=" * 60)

# # --- 6.1 String basics ---
# print("\n--- String Basics ---")

# greeting_single: str = 'Hello, World!'
# greeting_double: str = "Hello, World!"
# multiline: str = """This is a
# multi-line string."""
# print(greeting_single)
# print(multiline)

# # Type conversion
# number: int = 123
# number_str: str = str(number)
# print(f"str(123) = '{number_str}', type = {type(number_str)}")

# # --- 6.2 Escape sequences ---
# print("\n--- Escape Sequences ---")

# print("Line 1\nLine 2")            # Newline
# print("Col1\tCol2\tCol3")          # Tab
# print("She said: \"Hi!\"")         # Escaped quotes
# print('It\'s Python!')             # Escaped apostrophe
# print(r"C:\Users\tony\notes")      # Raw string (no escapes)
# print('''He said: "I'm here!"''')  # Triple quotes handle both

# # --- 6.3 String interpolation ---
# print("\n--- String Interpolation ---")

# name: str = "Alice"
# age: int = 25

# # Old-style (legacy)
# print("Name: %s, Age: %d" % (name, age))

# # str.format()
# print("Name: {}, Age: {}".format(name, age))
# print("Name: {name}, Age: {age}".format(name="Alice", age=25))

# # f-strings (RECOMMENDED)
# print(f"Name: {name}, Age: {age}")
# print(f"Next year: {age + 1}")
# print(f"Pi: {3.14159:.2f}")       # Format specifier
# print(f"{'hello':>20}")            # Right-align in 20 chars
# print(f"{'hello':<20}|")           # Left-align in 20 chars
# print(f"{'hello':^20}")            # Center in 20 chars

# # --- 6.4 String concatenation ---
# print("\n--- String Concatenation ---")

# first: str = "John"
# last: str = "Doe"
# full: str = first + " " + last
# print(f"Concatenation: {full}")

# words: list = ["Hello", "World", "from", "Python"]
# sentence: str = " ".join(words)
# print(f"join(): {sentence}")

# print("=" * 40)  # Repetition

# # --- 6.5 Common string methods ---
# print("\n--- Common String Methods ---")

# s: str = "Hello, World!"
# print(f"Original:    '{s}'")
# print(f"upper():     '{s.upper()}'")
# print(f"lower():     '{s.lower()}'")
# print(f"capitalize():(on 'hELLO') '{'hELLO'.capitalize()}'")
# print(f"swapcase():  '{s.swapcase()}'")
# print(f"strip():     '{'  hello  '.strip()}'")
# print(f"replace():   '{s.replace('World', 'Python')}'")
# print(f"split(', '): {s.split(', ')}")
# print(f"find('World'): {s.find('World')}")
# print(f"count('l'):  {s.count('l')}")
# print(f"startswith('Hello'): {s.startswith('Hello')}")
# print(f"endswith('!'): {s.endswith('!')}")
# print(f"isdigit() on '123': {'123'.isdigit()}")
# print(f"isalpha() on 'abc': {'abc'.isalpha()}")

# # Remember: string methods return NEW strings (immutable!)
# original: str = "hello"
# modified: str = original.upper()
# print(f"\noriginal unchanged: '{original}'")
# print(f"modified (new str):  '{modified}'")

# # --- 6.6 Indexing ---
# print("\n--- String Indexing ---")

# greeting = "hello"
# print(f"greeting = '{greeting}'")
# print(f"greeting[0] = '{greeting[0]}'")    # 'h'
# print(f"greeting[4] = '{greeting[4]}'")    # 'o'
# print(f"greeting[-1] = '{greeting[-1]}'")  # 'o'
# print(f"greeting[-5] = '{greeting[-5]}'")  # 'h'

# # Uncomment to see errors:
# # print(greeting[5])    # IndexError: string index out of range
# # greeting[0] = 'H'    # TypeError: 'str' object does not support item assignment

# # --- 6.7 Slicing ---
# print("\n--- String Slicing ---")

# greeting = "hello"
# print(f"greeting = '{greeting}'")
# print(f"greeting[0:3]   = '{greeting[0:3]}'")   # 'hel'
# print(f"greeting[:3]    = '{greeting[:3]}'")     # 'hel'
# print(f"greeting[2:]    = '{greeting[2:]}'")     # 'llo'
# print(f"greeting[:]     = '{greeting[:]}'")      # 'hello'
# print(f"greeting[-5:-2] = '{greeting[-5:-2]}'")  # 'hel'
# print(f"greeting[-3:]   = '{greeting[-3:]}'")    # 'llo'
# print(f"greeting[::2]   = '{greeting[::2]}'")    # 'hlo'
# print(f"greeting[::-1]  = '{greeting[::-1]}'")   # 'olleh'
# print(f"greeting[4:1:-1]= '{greeting[4:1:-1]}'") # 'oll'


# # --- Exercise 2: Strings ---
# print("\n--- Exercise 2: Strings ---")

# # Part A: Predict the outputs
# text: str = "Learn Python, be happy!"
# print(f"text[6:12]  = '{text[6:12]}'")
# print(f"text[-6:]   = '{text[-6:]}'")
# print(f"text[::3]   = '{text[::3]}'")

# # Part B: Slicing tasks
# quote: str = "Learn Python, be happy!"
# # Task 1: Extract "Python" using positive indices
# task1: str = quote[6:12]
# print(f"Task 1 (positive): '{task1}'")

# # Task 2: Extract "Python" using negative indices
# task2: str = quote[-17:-11]
# print(f"Task 2 (negative): '{task2}'")

# # Task 3: Reverse "Python" to get "nohtyP"
# task3: str = quote[11:5:-1]
# print(f"Task 3 (reverse):  '{task3}'")

# # Task 4: Reverse the entire string
# task4: str = quote[::-1]
# print(f"Task 4 (full reverse): '{task4}'")

# # Part C: Print second half
# text = "HelloWorld"
# second_half: str = text[len(text) // 2:]
# print(f"Second half of '{text}': '{second_half}'")


# # ============================================================
# # SECTION 7: CONTROL FLOW
# # ============================================================

# print("\n" + "=" * 60)
# print("SECTION 7: CONTROL FLOW")
# print("=" * 60)

# # --- 7.1 Simple if ---
# print("\n--- Simple if ---")

# x: int = 10
# if x > 0:
#     print("x is positive")
# print("This always runs")

# # --- 7.2 if-else ---
# print("\n--- if-else ---")

# x = -3
# if x >= 0:
#     print("Non-negative")
# else:
#     print("Negative")

# # --- 7.3 if-elif-else ---
# print("\n--- if-elif-else ---")

# score: int = 85
# if score >= 90:
#     grade: str = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print(f"Score: {score}, Grade: {grade}")

# # --- 7.4 Conditional (ternary) expression ---
# print("\n--- Ternary Expression ---")

# age = 20
# status: str = "adult" if age >= 18 else "minor"
# print(f"Age {age} -> {status}")

# # --- 7.5 Nested conditions ---
# print("\n--- Nested Conditions ---")

# temperature: int = 25
# humidity: int = 80

# if temperature > 30:
#     if humidity > 70:
#         print("Hot and humid")
#     else:
#         print("Hot and dry")
# elif temperature > 20:
#     print("Pleasant")
# else:
#     print("Cool")


# # --- Exercise 3: Control Flow ---
# print("\n--- Exercise 3: Control Flow ---")

# # Part A: Robot battery classifier
# battery_level: int = 45

# if battery_level >= 80:
#     battery_status: str = "Full"
# elif battery_level >= 50:
#     battery_status = "Moderate"
# elif battery_level >= 20:
#     battery_status = "Low"
# else:
#     battery_status = "Critical — return to base!"
# print(f"Battery ({battery_level}%): {battery_status}")

# # Part B: Leap year checker
# year: int = 2024

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


# # ============================================================
# # SECTION 8: INTRODUCTION TO TYPE HINTS
# # ============================================================

# print("\n" + "=" * 60)
# print("SECTION 8: INTRODUCTION TO TYPE HINTS")
# print("=" * 60)

# # --- Variable annotations ---
# print("\n--- Variable Annotations ---")

# robot_name: str = "TurtleBot3"
# max_speed: float = 1.5
# is_active: bool = True
# sensor_readings: list[float] = [0.5, 1.2, 0.8, 2.1]

# print(f"Robot: {robot_name}")
# print(f"Speed: {max_speed} m/s")
# print(f"Active: {is_active}")
# print(f"Sensors: {sensor_readings}")

# # --- Function annotations ---
# print("\n--- Function Annotations ---")


# def compute_area(radius: float) -> float:
#     """Compute the area of a circle."""
#     return math.pi * radius**2


# def format_status(name: str, speed: float, active: bool) -> str:
#     """Format a robot status message."""
#     status: str = "ACTIVE" if active else "IDLE"
#     return f"{name}: {status} at {speed} m/s"


# def average_reading(readings: list[float]) -> float:
#     """Compute the average of sensor readings."""
#     return sum(readings) / len(readings)


# def log_message(message: str) -> None:
#     """Log a message (returns nothing)."""
#     print(f"[LOG] {message}")


# # Using the annotated functions
# area_result: float = compute_area(5.0)
# print(f"Area (r=5): {area_result:.2f}")

# status_msg: str = format_status(robot_name, max_speed, is_active)
# print(status_msg)

# avg: float = average_reading(sensor_readings)
# print(f"Average reading: {avg:.2f}")

# log_message("System initialized")


# # --- Exercise 4: Add type hints ---
# print("\n--- Exercise 4: Type Hints (solution) ---")

# # All variables and functions above already have type hints!
# # Run: mypy lecture2_snippets.py
# # to check for type errors.


# # ============================================================
# # SECTION 9: PUTTING IT ALL TOGETHER
# # ============================================================

# print("\n" + "=" * 60)
# print("EXERCISE 5: ROBOT STATUS MONITOR")
# print("=" * 60)

# # Robot parameters with type hints
# robot_name_ex: str = "Waffle_01"
# battery_ex: int = 65
# speed_ex: float = 0.8
# status_log_ex: str = "IDLE:MOVING:CHARGING:MOVING:IDLE"

# # 1. Formatted output with f-string
# print(f"Robot {robot_name_ex} | Battery: {battery_ex}%")

# # 2. Battery classification
# if battery_ex >= 80:
#     batt_class: str = "OK"
# elif battery_ex >= 50:
#     batt_class = "LOW"
# elif battery_ex >= 20:
#     batt_class = "WARNING"
# else:
#     batt_class = "CRITICAL"
# print(f"Battery status: {batt_class}")

# # 3. String methods
# moving_count: int = status_log_ex.count("MOVING")
# print(f"MOVING count: {moving_count}")

# status_list: list[str] = status_log_ex.split(":")
# print(f"Status list: {status_list}")

# is_idle: bool = status_list[-1] == "IDLE"
# print(f"Last status is IDLE: {is_idle}")

# # 4. Slicing to extract first status
# first_colon: int = status_log_ex.find(":")
# first_status: str = status_log_ex[:first_colon]
# print(f"First status: {first_status}")

# # 5. Comprehensive status message
# num_states: int = len(status_list)
# print(f"{robot_name_ex} | Battery: {batt_class} | Speed: {speed_ex:.2f} m/s | States: {num_states}")


# # ============================================================
# # MAIN GUARD
# # ============================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("All lecture 2 snippets executed successfully!")
    print("=" * 60)

