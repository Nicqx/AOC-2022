from unittest import TestCase

from Days.Day9 import Day9


class TestDay9(TestCase):
    def test_task1(self):
        expected_value = str(13)
        actual_value = Day9('../Resources/Day9/test').task1()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        expected_value_task1 = str(5619)
        expected_value_task2 = str(2250)
        d9 = Day9('../Resources/Day9/input')
        actual_value_task1 = d9.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        # d9 = Day9('../Resources/Day9/input')
        # actual_value_task2 = d9.task2()
        # self.assertEqual(expected_value_task2, actual_value_task2)
