from .animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity


class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if not isinstance(food, Food):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 0.35 * food.quantity
            self.food_eaten += food.quantity