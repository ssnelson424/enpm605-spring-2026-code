"""
ENPM605 - Python Applications for Robotics
Lecture 3: Python Fundamentals — Part II
Spring 2026 | University of Maryland

Section: Exercises
"""

# ============================================================
# Exercise 1: Loop Practice (10 min)
# ============================================================

# ──────────────────────────────────────────────
# 📌 Snippet 17 — Exercise 1: Loop Practice
# ──────────────────────────────────────────────

# 1. Use range() to print all multiples of 3 from 3 to 30


# 2. Given the string below, use a for loop to count 
#    how many times the letter 'o' appears
robot_name = "TurtleBot3 Waffle Robot"


# 3. Use a while loop to find the first space in the string
#    and print everything before it
sentence = "Robotics is fun"


# 4. Print this string in reverse using range()
text = "ENPM605"


# 5. Use enumerate() to print each character with its position
message = "Hello"

# # ============================================================
# # Exercise 2: Modifying a Dictionary (5 min)
# # ============================================================
# # ──────────────────────────────────────────────
# # 📌 Snippet 60 
# # ──────────────────────────────────────────────
# sensor = {
#     "type": "lidar",
#     "range_m": 100,
#     "manufacturer": "Velodyne",
#     "channels": 64
# }
# # 1. Update the sensor range to 120 m
# # 2. Rename the key range_m to max_range_m (one line)


# ============================================================
# Exercise 3: Robot Sensor Analysis (15 min)
# ============================================================

# # ──────────────────────────────────────────────
# # 📌 Snippet 67 — Exercise 3: Robot Sensor Analysis
# # ──────────────────────────────────────────────
# # Sensor data from multiple robots
# sensor_data = {
#     "robot_1": [0.5, 1.2, 0.8, 2.1, 0.3],
#     "robot_2": [1.1, 0.9, 1.5, 0.7, 1.3],
#     "robot_3": [0.2, 0.4, 0.6, 0.8, 1.0],
# }

# # 1. Use a for loop to print each robot name and its readings


# # 2. For each robot, calculate and print the average reading


# # 3. Use a list comprehension to get all readings above 1.0
# #    from robot_1's data


# # 4. Create a set of all unique readings across all robots
# #    (Hint: you may need to round to avoid float comparison issues)


# # 5. Create a new dictionary mapping robot names to their max reading


# # 6. Use tuple unpacking to process (robot, readings) pairs
# #    and find the robot with the highest total sum of readings
