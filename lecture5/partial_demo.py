"""
Course: ENPM605
Lecture: Advanced Functions
Section: Partial Functions

Author: zeidk
Created: 2026-02-23
"""

from functools import partial

# # ──────────────────────────────────────────────
# # 📌 Snippet 29
# # ──────────────────────────────────────────────

# def compute_power(base, exponent):
#     return base**exponent


# # Create specialized functions by freezing one argument
# square = partial(compute_power, exponent=2)
# cube = partial(compute_power, exponent=3)

# print(square(5))  # 25
# print(cube(5))  # 125

# # ──────────────────────────────────────────────
# # 📌 Snippet 30
# # ──────────────────────────────────────────────
# def compute_power(base, exponent):
#     return base**exponent


# # Freezing a keyword argument
# square = partial(compute_power, exponent=2)
# print(square.func)  # <function compute_power at 0x...>
# print(square.args)  # ()
# print(square.keywords)  # {'exponent': 2}
# print(square(10))  # 100

# # Freezing a positional argument (fills left to right)
# power_of_ten = partial(compute_power, 10)
# print(power_of_ten.func)  # <function compute_power at 0x...>
# print(power_of_ten.args)  # (10,)
# print(power_of_ten.keywords)  # {}
# print(power_of_ten(3))  # 1000  (10 ** 3)


# # ──────────────────────────────────────────────
# # 📌 Snippet 31
# # ──────────────────────────────────────────────
# def convert_distance(value, from_unit, to_unit):
#     """Convert between distance units."""
#     # Lookup table: how many meters one unit equals
#     to_meters = {"m": 1.0, "cm": 0.01, "ft": 0.3048, "in": 0.0254}

#     # Step 1: Convert the input value to meters (common denominator)
#     meters = value * to_meters[from_unit]

#     # Step 2: Convert from meters to the target unit
#     # We need: how many target units fit in 'meters'?
#     # 1 target_unit = to_meters[to_unit] meters
#     # So: meters / to_meters[to_unit] = number of target units
#     return meters / to_meters[to_unit]


# # Create specialized converters by freezing from_unit and to_unit
# ft_to_m = partial(convert_distance, from_unit="ft", to_unit="m")
# cm_to_in = partial(convert_distance, from_unit="cm", to_unit="in")

# # Only 'value' remains as an argument
# print(f"{ft_to_m(10):.2f} m")  # 3.05 m
# print(f"{cm_to_in(100):.2f} in")  # 39.37 in


# # ──────────────────────────────────────────────
# # 📌 Snippet 32
# # ──────────────────────────────────────────────
# def compute_power(base, exponent):
#     return base**exponent


# # Using partial
# square_partial = partial(compute_power, exponent=2)

# # Using lambda
# square_lambda = lambda base: compute_power(base, exponent=2)


# # Using closure
# def make_power_func(exp):
#     def compute_value(base):
#         return compute_power(base, exp)

#     return compute_value


# square_closure = make_power_func(2)

# # All produce the same result
# print(square_partial(5), square_lambda(5), square_closure(5))
# # 25 25 25
