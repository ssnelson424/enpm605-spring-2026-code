"""
Course: ENPM605
Lecture: OOP Part 2

Author: zeidk
Created: 2026-03-06
"""

# # ──────────────────────────────────────────────
# # 📌 Snippet 5
# # ──────────────────────────────────────────────
class Robot:
    def __init__(self, name: str, battery: int = 100):
        self._name = name
        self._battery = battery

    @property
    def name(self) -> None:
        return self._name


class Team:
    def __init__(self, team_name: str):
        self._team_name = team_name
        self._robots: list[Robot] = []

    def add_robot(self, robot: Robot) -> None:
        self._robots.append(robot)


if __name__ == "__main__":
    scout = Robot("Scout")  # Created independently
    hauler = Robot("Hauler", 80)  # Created independently
    alpha = Team("Alpha")
    alpha.add_robot(scout)
    alpha.add_robot(hauler)
    del alpha  # Team dissolved
    print(scout.name)  # Scout (still exists)
