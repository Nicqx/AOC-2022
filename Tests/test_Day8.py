from unittest import TestCase

from Days.Day8 import Day8


class TestDay8(TestCase):
    def test_task1(self):
        expected_value = str(21)
        actual_value = Day8('../Resources/Day8/test').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(8)
        actual_value = Day8('../Resources/Day8/test').task2()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        expected_value_task1 = str(1832)
        expected_value_task2 = str(157320)
        d8 = Day8('../Resources/Day8/input')
        actual_value_task1 = d8.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        d8 = Day8('../Resources/Day8/input')
        actual_value_task2 = d8.task2()
        self.assertEqual(expected_value_task2, actual_value_task2)
