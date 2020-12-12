from project.factory.factory import Factory


class ChocolateFactory(Factory):

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = dict()
        self.products = dict()

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if not ingredient_type in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        if not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        self.ingredients[ingredient_type] = self.ingredients.get(ingredient_type, 0) + quantity

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if not ingredient_type in self.ingredients.keys():
            raise KeyError("No such product in the factory")
        if self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")
        self.ingredients[ingredient_type] -= quantity

    def add_recipe(self, recipe_name: str, recipe: dict):
        if not recipe_name in self.recipes.keys():
            self.recipes[recipe_name] = recipe
        self.recipes[recipe_name] = recipe  # is adding as new and updating, means the same thing?

    def make_chocolate(self, recipe_name: str):
        if not recipe_name in self.recipes.keys():
            raise TypeError("No such recipe")
        self.products[recipe_name] = self.products.get(recipe_name, 0) + 1
        for ingr_type, q in self.recipes[recipe_name].items():
            self.remove_ingredient(ingr_type, q)


