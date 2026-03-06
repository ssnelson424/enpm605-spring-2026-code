"""
Course: ENPM605
Lecture: OOP Part 2

Author: zeidk
Created: 2026-03-06
"""


# # ──────────────────────────────────────────────
# # 📌 Snippet 4
# # ──────────────────────────────────────────────
# class Task:
#     def __init__(self, name: str, priority: int):
#         self._name = name
#         self._priority = priority


# class Robot:
#     def __init__(self, name: str):
#         self._name = name
#         self._current_task: Task | None = None

#     def assign_task(self, task: Task):
#         self._current_task = task
#         print(f"{self._name} assigned: {task.name}")


# if __name__ == "__main__":
#     pick = Task("pick widget", priority=1)
#     scout = Robot("Scout")
#     scout.assign_task(pick)  # Scout assigned: pick widget


# # ──────────────────────────────────────────────
# # 📌 Snippet 5
# # ──────────────────────────────────────────────
# class Robot:
#     def __init__(self, name: str, battery: int = 100):
#         self._name = name
#         self._battery = battery

#     @property
#     def name(self) -> None:
#         return self._name


# class Team:
#     def __init__(self, team_name: str):
#         self._team_name = team_name
#         self._robots: list[Robot] = []

#     def add_robot(self, robot: Robot) -> None:
#         self._robots.append(robot)


# if __name__ == "__main__":
#     scout = Robot("Scout")  # Created independently
#     hauler = Robot("Hauler", 80)  # Created independently
#     alpha = Team("Alpha")
#     alpha.add_robot(scout)
#     alpha.add_robot(hauler)
#     del alpha  # Team dissolved
#     print(scout.name)  # Scout (still exists)


# # ──────────────────────────────────────────────
# # 📌 Snippet 6
# # ──────────────────────────────────────────────
# class Sensor:
#     def __init__(self, sensor_type: str, range_m: float):
#         self._sensor_type = sensor_type
#         self._range_m = range_m

#     def __repr__(self) -> str:
#         return f"Sensor('{self._sensor_type}', {self._range_m})"


# class Robot:
#     def __init__(self, name: str):
#         self._name = name
#         self._lidar = Sensor("lidar", 50.0)

#     def __repr__(self) -> str:
#         return f"Robot('{self._name}', {self._lidar})"


# if __name__ == "__main__":
#     scout = Robot("Scout")
#     print(scout)  # Robot('Scout', Sensor('lidar', 50.0))
#     # Sensors are created and destroyed with the Robot
