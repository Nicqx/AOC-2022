from unittest import TestCase

from Days.Day5 import Day5


class TestDay5(TestCase):
    def test_task1(self):
        expected_value = "CMZ"
        actual_value = Day5('../Resources/Day5/test').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = "MCD"
        actual_value = Day5('../Resources/Day5/test').task2()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        expected_value_task1 = "QPJPLMNNR"
        expected_value_task2 = "BQDNWJPVJ"
        d5 = Day5('../Resources/Day5/input')
        actual_value_task1 = d5.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        d5 = Day5('../Resources/Day5/input')
        actual_value_task2 = d5.task2()
        self.assertEqual(expected_value_task2, actual_value_task2)
