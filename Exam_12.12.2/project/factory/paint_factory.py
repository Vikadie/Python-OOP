from project.factory.factory import Factory


class PaintFactory(Factory):

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)

    @property
    def products(self):
        return self.ingredients

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if not ingredient_type in ["white", "yellow", "blue", "green", "red"]:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        self.ingredients[ingredient_type] = self.ingredients.get(ingredient_type, 0) + quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if not ingredient_type in self.ingredients.keys():
            raise KeyError("No such ingredient in the factory")
        if self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")
        self.ingredients[ingredient_type] -= quantity
