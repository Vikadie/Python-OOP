class Room:
    children = []
    appliances = []

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        # each element of args will be a list ?!?!
        total_cost = 0
        for a in args:
            total_cost += a.get_monthly_expense()
        self.__expenses = total_cost
