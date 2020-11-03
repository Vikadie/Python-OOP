from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))

# c = Customer("Sofia", "Lozen", "blabla@maimun.com")
# print(c)
#
# m = Customer("Sofia", "Lozen", "ihaha@maimun.com")
# print(c)
# print(m)
# equip1 = Equipment("Number 1")
# equip2 = Equipment("Number 2")
# print(equip1)
# print(equip2)
# ep1 = ExercisePlan(1, 1, 32)
# ep2 = ExercisePlan.from_hours(1, 1, 3)
# ep3 = ExercisePlan(2, 1, 15)
# print(ep1)
# print(ep2)
# print(ep3)
# sub1 = Subscription("14.05.2020", 1, 1, 2)
# sub2 = Subscription("22.06.2020", 23, 3, 2)
# print(sub1)
# print(sub2)
# tr1 = Trainer("Serioza")
# tr2 = Trainer("NeSerioza")
# print(tr1)
# print(tr2)

