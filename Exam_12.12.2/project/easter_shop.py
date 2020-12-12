from project.factory.chocolate_factory import ChocolateFactory
from project.factory.egg_factory import EggFactory
from project.factory.paint_factory import PaintFactory


class EasterShop:

    def __init__(self, name, chocolate_factory: ChocolateFactory, egg_factory: EggFactory,
                 paint_factory: PaintFactory):

        self.name = name
        self.chocolate_factory = chocolate_factory
        self.egg_factory = egg_factory
        self.paint_factory = paint_factory
        self.storage = dict()

    def add_chocolate_ingredient(self, type: str, quantity: int):
        self.chocolate_factory.add_ingredient(type, quantity)

    def add_egg_ingredient(self, type: str, quantity: int):
        self.egg_factory.add_ingredient(type, quantity)

    def add_paint_ingredient(self, type: str, quantity: int):
        self.paint_factory.add_ingredient(type, quantity)

    def make_chocolate(self, recipe: str):
        self.chocolate_factory.make_chocolate(recipe)
        self.storage[recipe] = self.storage.get(recipe, 0) + 1

    def paint_egg(self, color: str, egg_type: str):
        if egg_type not in self.egg_factory.products or color not in self.paint_factory.products:
            raise ValueError("Invalid commands")
        if self.egg_factory.products[egg_type] == 0 or self.paint_factory.products[color] == 0:
            raise ValueError("Invalid commands")
        key = f"{color} {egg_type}"
        self.storage[key] = self.storage.get(key, 0) + 1
        self.egg_factory.remove_ingredient(egg_type, 1)
        self.paint_factory.remove_ingredient(color, 1)


    def __repr__(self):
        items_list = ''
        for item_name, item_quantity in self.storage.items():
            items_list += f'{item_name}: {item_quantity}\n'
        return f"Shop name: {self.name}\nShop Storage:\n{items_list}"


# cf = ChocolateFactory('chocolate factory', 3)
# eg = EggFactory('egg_factory', 4)
# pf = PaintFactory('paint_factory', 5)
# shop = EasterShop('shop', cf, eg, pf)
#
# eg.add_ingredient('chicken egg', 1)
# print(eg.products)
# print(('egg' not in shop.egg_factory.products and shop.egg_factory.products['egg'] == 0))
# shop.egg_factory.remove_ingredient('egg', 1)
# print(eg.products)
# print(cf.products)
# print(pf.products)