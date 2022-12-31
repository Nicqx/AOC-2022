from unittest import TestCase

from Days.Day12 import Day12


class TestDay12(TestCase):
    def test_task1(self):
        expected_value = str(31)
        actual_value = Day12('../Resources/Day12/test').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(29)
        actual_value = Day12('../Resources/Day12/test').task2()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        expected_value_task1 = str(423)
        expected_value_task2 = str(416)
        d12 = Day12('../Resources/Day12/input')
        actual_value_task1 = d12.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        d12 = Day12('../Resources/Day12/input')
        actual_value_task2 = d12.task2()
        self.assertEqual(expected_value_task2, actual_value_task2)


