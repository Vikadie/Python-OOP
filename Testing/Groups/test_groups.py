from groups import Person, Group

import unittest


class PersonTest(unittest.TestCase):

    def setUp(self):
        self.p = Person('John', 'Doe')

    def test_init(self):
        self.assertEqual(self.p.name, 'John')
        self.assertEqual(self.p.surname, 'Doe')

    def test_adding_persons(self):
        p0 = self.p
        p1 = Person('Doe', 'Smith')
        act = p0 + p1
        self.assertEqual(act.name, self.p.name)
        self.assertEqual(act.surname, p1.surname)

    def test_person_representation_string(self):
        self.assertEqual(str(self.p), 'John Doe')


class GroupTest(unittest.TestCase):

    def setUp(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        p2 = Person('Warren', 'Buffet')
        self.first_group = Group('__VIP__', [p0, p1, p2])

    def test_group_init(self):
        self.assertEqual(self.first_group.name, '__VIP__')
        self.assertEqual(self.first_group.people[0].name, 'Aliko')

    def test_group_len_linst_people(self):
        self.assertEqual(len(self.first_group.people), 3)

    def test_group_print(self):
        self.assertEqual(str(self.first_group),
                         'Group __VIP__ with members Aliko Dangote, '
                         'Bill Gates, Warren Buffet')

    def test_group_item_print(self):
        self.assertEqual(self.first_group.__getitem__(0), 'Person 0: Aliko Dangote')

    def test_group_item_print_with_for_cycle(self):
        expected = ['Person 0: Aliko Dangote','Person 1: Bill Gates',
                    'Person 2: Warren Buffet']
        self.assertEqual(list(self.first_group), expected) # list involes iter() method under the hood

    def test_group_adding(self):
        p0 = Person('Aliko', 'Dangote')
        p1 = Person('Bill', 'Gates')
        second_group = Group("Second", [p0, p1])
        third = self.first_group + second_group
        expected_name = self.first_group.name
        self.assertEqual(third.name, expected_name)
        expected_len = len(self.first_group) + len(second_group)
        self.assertEqual(len(third), expected_len)



if __name__ == "__main__":
    unittest.main()