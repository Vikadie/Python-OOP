import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.hw = Hardware('hw', "Heavy", 100, 100)

    def test_init_state(self):
        self.assertEqual('hw', self.hw.name)
        self.assertEqual('Heavy', self.hw.type)
        self.assertEqual(100, self.hw.capacity)
        self.assertEqual(100, self.hw.memory)
        self.assertEqual([], self.hw.software_components)

    def test_install_sw_successfully(self):
        sw = Software('name','Light', 20, 20)
        self.hw.install(sw)
        self.assertEqual([sw], self.hw.software_components)

    def test_install_sw_unsuccessful(self):
        sw = Software('name', 'Light', 110, 20)
        with self.assertRaises(Exception) as exc1:
            self.hw.install(sw)
        self.assertEqual('Software cannot be installed', str(exc1.exception))
        sw1 = Software('name', 'Light', 20, 120)
        with self.assertRaises(Exception) as exc2:
            self.hw.install(sw1)
        self.assertEqual('Software cannot be installed', str(exc2.exception))

    def test_uninstall_sw_successful(self):
        sw = Software('name', 'Light', 20, 20)
        self.hw.install(sw)
        self.assertEqual([sw], self.hw.software_components)
        self.hw.uninstall(sw)
        self.assertEqual([], self.hw.software_components)


if __name__ == '__main__':
    unittest.main()