from unittest import TestCase

from Days.Day6 import Day6


class TestDay6(TestCase):
    def test_task1(self):
        expected_value = str(7)
        actual_value = Day6('../Resources/Day6/test1').task1()
        self.assertEqual(expected_value, actual_value)
        expected_value = str(5)
        actual_value = Day6('../Resources/Day6/test2').task1()
        self.assertEqual(expected_value, actual_value)
        expected_value = str(6)
        actual_value = Day6('../Resources/Day6/test3').task1()
        self.assertEqual(expected_value, actual_value)
        expected_value = str(10)
        actual_value = Day6('../Resources/Day6/test4').task1()
        self.assertEqual(expected_value, actual_value)
        expected_value = str(11)
        actual_value = Day6('../Resources/Day6/test5').task1()
        self.assertEqual(expected_value, actual_value)

    def test_task2(self):
        expected_value = str(19)
        actual_value = Day6('../Resources/Day6/test1').task2()
        self.assertEqual(expected_value, actual_value)
        expected_value = str(23)
        actual_value = Day6('../Resources/Day6/test2').task2()
        self.assertEqual(expected_value, actual_value)
        expected_value = str(23)
        actual_value = Day6('../Resources/Day6/test3').task2()
        self.assertEqual(expected_value, actual_value)
        expected_value = str(29)
        actual_value = Day6('../Resources/Day6/test4').task2()
        self.assertEqual(expected_value, actual_value)
        expected_value = str(26)
        actual_value = Day6('../Resources/Day6/test5').task2()
        self.assertEqual(expected_value, actual_value)

    def test_original(self):
        pass
        expected_value_task1 = str(1625)
        expected_value_task2 = str(2250)
        d6 = Day6('../Resources/Day6/input')
        actual_value_task1 = d6.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        d6 = Day6('../Resources/Day6/input')
        actual_value_task2 = d6.task2()
        self.assertEqual(expected_value_task2, actual_value_task2)
