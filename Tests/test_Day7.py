from unittest import TestCase

from Days.Day7 import Day7


class TestDay7(TestCase):
    def test_task1(self):
        expected_value = str(95437)
        actual_value = Day7('../Resources/Day7/test').task1()
        self.assertEqual(expected_value, actual_value)
