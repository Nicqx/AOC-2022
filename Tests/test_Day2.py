from unittest import TestCase

from Days.Day2 import Day2


class Test(TestCase):
    def test_task1(self):
        expected_value = str(15)
        actual_value = Day2('../Resources/Day2/test').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(12)
        actual_value = Day2('../Resources/Day2/test').task2()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        expected_value_task1 = str(11475)
        expected_value_task2 = str(16862)
        d2 = Day2('../Resources/Day2/input')
        actual_value_task1 = d2.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        actual_value_task2 = d2.task2()
        self.assertEqual(expected_value_task2, actual_value_task2)
