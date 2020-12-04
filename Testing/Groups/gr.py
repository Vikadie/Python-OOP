class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return self.name + ' ' + self.surname

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __str__(self):
        people_str = ', '.join([str(person) for person in self.people])
        return "Group " + self.name + " with members " + people_str

    def __len__(self):
        return len(self.people)

    def __getitem__(self, index):
        return "Person " + str(index) + ": " + str(self.people[index])

    def __add__(self, other):
        return Group(self.name, self.people + other.people)