from .keeper import Keeper
from .caretaker import Caretaker
from .lion import Lion
from .tiger import Tiger
from .vet import Vet
from .cheetah import Cheetah


class Zoo:

    def __init__(self, name, budget, animlal_capacity, workers_capacity):
        self.__animal_capacity = animlal_capacity
        self.__workers_capacity = workers_capacity
        self.__budget = budget
        self.name = name
        self.animals = []
        self.workers = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, budget):
        if budget >= 0:
            self.__budget = budget

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if price <= self.__budget:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        workers_name_list = [w.name for w in self.workers]
        if worker_name in workers_name_list:
            del self.workers[workers_name_list.index(worker_name)]
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries_sum = sum([w.salary for w in self.workers])
        if self.__budget >= salaries_sum:
            self.__budget -= salaries_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tend_animals_sum = sum([a.get_needs() for a in self.animals])
        if self.__budget >= tend_animals_sum:
            self.__budget -= tend_animals_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        output = (f"You have {total_animals_count} animals")
        lions = [a.__repr__() for a in self.animals if type(a) == Lion]
        tigers = [a.__repr__() for a in self.animals if type(a) == Tiger]
        cheetahs = [a.__repr__() for a in self.animals if type(a) == Cheetah]

        output += (f"\n----- {len(lions)} Lions:\n")
        output += ('\n'.join(lions))
        output += (f"\n----- {len(tigers)} Tigers:\n")
        output += ('\n'.join(tigers))
        output += (f"\n----- {len(cheetahs)} Cheetahs:\n")
        output += ('\n'.join(cheetahs))

        return output

    def workers_status(self):
        total_workers_count = len(self.workers)
        keepers = [w.__repr__() for w in self.workers if type(w) == Keeper]
        caretakers = [w.__repr__() for w in self.workers if type(w) == Caretaker]
        vets = [w.__repr__() for w in self.workers if type(w) == Vet]

        output = f"You have {total_workers_count} workers"
        output += f"\n----- {len(keepers)} Keepers:\n"
        output += '\n'.join(keepers)
        output += f"\n----- {len(caretakers)} Caretakers:\n"
        output += '\n'.join(caretakers)
        output += f"\n----- {len(vets)} Vets:\n"
        output += '\n'.join(vets)

        return output
