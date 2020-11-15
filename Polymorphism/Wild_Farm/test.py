from project.animals.animal import Mammal, Bird, Animal
from project.animals.birds import Hen, Owl
from project.animals.mammals import Mouse, Cat, Dog, Tiger
from project.food import Food, Meat, Vegetable, Fruit, Seed

owl = Mouse("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
print(owl.feed(meat))
veg = Vegetable(3)
fruit = Fruit(4)
seed = Seed(1)
print(owl.feed(veg))
print(owl.feed(seed))
print(owl.feed(fruit))
print(owl)

print("-"*25)

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(4)
seed = Seed(1)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(seed)
hen.feed(meat)
print(hen)