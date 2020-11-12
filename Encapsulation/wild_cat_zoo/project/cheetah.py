class Cheetah:

    def __init__(self, name: str, gender: str, age: float):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs():
        return 60  # amount of money needed to tend the animal

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"