from unittest import TestCase

from Days.Day3 import Day3


class TestDay1(TestCase):
    def test_task1(self):
        expected_value = str(157)
        actual_value = Day3('../Resources/Day3/test').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(70)
        actual_value = Day3('../Resources/Day3/test').task2()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        expected_value_task1 = str(7674)
        expected_value_task2 = str(2805)
        d3 = Day3('../Resources/Day3/input')
        actual_value_task1 = d3.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        actual_value_task2 = d3.task2()
        self.assertEqual(expected_value_task2, actual_value_task2)
