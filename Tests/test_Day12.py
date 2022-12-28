from unittest import TestCase

from Days.Day12 import Day12


class TestDay12(TestCase):
    def test_task1(self):
        expected_value = str(31)
        actual_value = Day12('../Resources/Day12/test').task1()
        self.assertEqual(expected_value, actual_value)
