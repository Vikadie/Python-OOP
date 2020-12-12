import unittest

from project.spaceship.spaceship import Spaceship


class TestSpaceship(unittest.TestCase):

    def setUp(self) -> None:
        self.spaceship = Spaceship('Apollo', 2)

    def test_proper_init_name_capacity_astronauts(self):
        self.assertEqual('Apollo', self.spaceship.name)
        self.assertEqual(2, self.spaceship.capacity)
        self.assertEqual([], self.spaceship.astronauts)

    def test_add_astronauts_ok_plus_existing(self):
        self.assertEqual("Added astronaut Pesho", self.spaceship.add('Pesho'))
        with self.assertRaises(ValueError) as exc:
            self.spaceship.add('Pesho')
        self.assertEqual("Astronaut Pesho Exists", str(exc.exception))

    def test_add_astronauts_too_crowded(self):
        self.spaceship.add('Pesho')
        self.spaceship.add('Gosho')
        with self.assertRaises(ValueError) as exc:
            self.spaceship.add('Tretiq')
        self.assertEqual("Spaceship is full", str(exc.exception))

    def test_remove_astronauts_ok(self):
        self.spaceship.add('Pesho')
        self.assertEqual('Removed Pesho', self.spaceship.remove('Pesho'))
        self.assertEqual([], self.spaceship.astronauts)

    def test_remove_astronauts_not_in_names(self):
        self.spaceship.add('Pesho')
        with self.assertRaises(ValueError) as exc:
            self.spaceship.remove('Gosho')
        self.assertEqual("Astronaut Not Found", str(exc.exception))


if __name__ == '__main__':
    unittest.main()