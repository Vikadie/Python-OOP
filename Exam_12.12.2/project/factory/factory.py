from abc import ABC, abstractmethod


class Factory(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = dict()

    @abstractmethod
    def add_ingredient (self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient (self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        if self.capacity >= sum(self.ingredients.values()) + value:
            return True
        return False
