from unittest import TestCase

from Days.Day11 import Day11


class Test(TestCase):

    def test_task1(self):
        expected_value = str(10605)
        actual_value = Day11('../Resources/Day11/test').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(2713310158)
        actual_value = Day11('../Resources/Day11/test').task2()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        expected_value_task1 = str(112815)
        d11 = Day11('../Resources/Day11/input')
        actual_value_task1 = d11.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        expected_value_task2 = str(25738411485)
        d11 = Day11('../Resources/Day11/input')
        actual_value_task2 = d11.task2()
        self.assertEqual(expected_value_task2, actual_value_task2)
