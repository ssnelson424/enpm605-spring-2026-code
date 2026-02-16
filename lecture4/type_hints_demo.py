# ============================================================
# 6. Type Hints
# ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 34
# # ──────────────────────────────────────────────
# def add(a: int, b: int) -> int:
#     return a + b


# def greet(name: str) -> None:
#     print(f"Hello, {name}!")


# # Type hints are NOT enforced at runtime
# result = add("hello", " world")  # Works! Returns "hello world"

# # ──────────────────────────────────────────────
# # 📌 Snippet 35
# # ──────────────────────────────────────────────
# from typing import Optional


# def find_index(items: list[str], target: str) -> Optional[int]:
#     """Return the index of target in items, or None."""
#     for i, item in enumerate(items):
#         if item == target:
#             return i
#     return None


# sensors = ["lidar", "camera", "imu"]
# result = find_index(sensors, "camera")
# print(result)  # 1

# result = find_index(sensors, "radar")
# print(result)  # None

# # ──────────────────────────────────────────────
# # 📌 Snippet 36
# # ──────────────────────────────────────────────
# from typing import Union


# def normalize(data: Union[str, list]) -> list[str]:
#     """Convert input to a list of strings."""
#     if isinstance(data, str):
#         return [data]
#     return [str(item) for item in data]


# print(normalize("hello"))  # ['hello']
# print(normalize([1, 2, 3]))  # ['1', '2', '3']


# # ──────────────────────────────────────────────
# # 📌 Snippet 38
# # ──────────────────────────────────────────────
# def find_index(items: list[str], target: str) -> int | None:
#     """Return the index of target in items, or None."""
#     for i, item in enumerate(items):
#         if item == target:
#             return i
#     return None


# sensors = ["lidar", "camera", "imu"]
# result = find_index(sensors, "camera")
# print(result)  # 1

# result = find_index(sensors, "radar")
# print(result)  # None

# # ──────────────────────────────────────────────


# def process(data: str | list) -> str:
#     """Convert the input data to a single formatted string.

#     Args:
#         data (str | list): A string or a list of values to process.

#     Returns:
#         str: A comma-separated string representation of the input.
#     """
#     if isinstance(data, str):
#         return data
#     return ", ".join(str(item) for item in data)


# print(process("hello"))  # hello
# print(process([1, 2, 3]))  # 1, 2, 3
# print(process(["a", "b"]))  # a, b


# # ──────────────────────────────────────────────
# # 📌 Snippet 39
# # ──────────────────────────────────────────────
# # Python 3.9+ - use built-in types directly
# def process_readings(readings: list[float]) -> float:
#     return sum(readings) / len(readings)


# def get_config() -> dict[str, int]:
#     return {"timeout": 30, "retries": 3}


# def get_coordinates() -> tuple[float, float]:
#     return (3.14, 2.72)


# # Variable-length tuple (all same type)
# # A tuple of any length where every element is an int
# def get_ids() -> tuple[int, ...]:
#     return (1, 2, 3, 4, 5)


# # Combining with functions
# def transform(items: list[str], func: callable) -> list[str]:
#     return [func(item) for item in items]
