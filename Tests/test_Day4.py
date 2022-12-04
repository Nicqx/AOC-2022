from unittest import TestCase

from Days.Day4 import Day4


class Test(TestCase):
    def test_task1(self):
        expected_value = str(2)
        actual_value = Day4('../Resources/Day4/test').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(4)
        actual_value = Day4('../Resources/Day4/test').task2()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        expected_value_task1 = str(453)
        expected_value_task2 = str(919)
        d4 = Day4('../Resources/Day4/input')
        actual_value_task1 = d4.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        actual_value_task2 = d4.task2()
        self.assertEqual(expected_value_task2, actual_value_task2)
