from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30
    appliances = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        self.members_count = 2 + len(children)
        super().__init__(name=family_name, budget=salary_one + salary_two, members_count=self.members_count)
        self.children = list(children)
        self.appliances *= self.members_count
        exp_lst = (self.appliances + self.children)
        self.calculate_expenses(*exp_lst)
