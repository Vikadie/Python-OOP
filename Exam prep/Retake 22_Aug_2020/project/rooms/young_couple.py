from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    room_cost = 20
    appliances = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(name=family_name, budget=salary_one + salary_two, members_count=2)
        self.appliances *= 2
        self.calculate_expenses(*self.appliances)