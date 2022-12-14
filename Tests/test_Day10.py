from unittest import TestCase

from Days.Day10 import Day10


class TestDay10(TestCase):
    def test_task1(self):
        expected_value = str(13140)
        actual_value = Day10('../Resources/Day10/test').task1()
        self.assertEqual(expected_value, actual_value)
        Day10('../Resources/Day10/test').task2()

    def test_task2(self):
        expected_value = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '.',
                          '.', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#',
                          '#', '.', '#', '#', '#', '.', '.', '.', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.',
                          '.', '#', '#', '#', '.', '.', '#', '#', '#', '#', '.', '.', '.', '#', '#', '#', '#', '.', '#',
                          '#', '#', '#', '.', '#', '#', '#', '#', '.', '.', '.', '#', '#', '#', '#', '#', '#', '.', '.',
                          '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '.', '.', '.', '#', '#',
                          '#', '#', '#', '#', '.', '.', '#', '#', '#', '#', '#', '.', '#', '.', '.', '.', '#', '#', '#',
                          '#', '#', '#', '#', '#', '.', '.', '#', '#', '#', '#', '#', '#', '.', '.', '.', '.', '#', '#',
                          '#', '#', '#', '#', '.', '.', '.', '.', '#', '#', '#', '#', '#', '#', '.', '.', '.', '.', '#',
                          '.', '#', '#', '#', '#', '#', '#', '.', '.', '#', '.', '.', '#', '#', '#', '#', '#', '#', '#',
                          '#', '.', '.', '.', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
                          '.', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '#', '.', '.',
                          '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '.', '.']
        actual_value = Day10('../Resources/Day10/test')
        self.assertEqual(expected_value, actual_value.crt)

    def test_original(self):
        expected_value_task1 = str(14720)
        expected_value_task2 = ['#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '.', '.', '#', '#',
                                '#', '.', '.', '#', '#', '#', '.',
                                '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#',
                                '.', '.', '.', '.', '.', '.', '.',
                                '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.', '#', '.', '.', '#', '.',
                                '#', '.', '.', '.', '.', '.', '.',
                                '.', '#', '.', '#', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '.', '#', '.',
                                '.', '#', '#', '#', '.', '.', '#',
                                '.', '.', '#', '.', '#', '#', '#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '#',
                                '.', '.', '#', '#', '#', '.', '.',
                                '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '#', '.', '#', '#',
                                '#', '.', '.', '#', '.', '.', '#',
                                '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.', '.', '#',
                                '.', '.', '.', '.', '#', '.', '.',
                                '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#', '.',
                                '#', '.', '.', '.', '.', '#', '.',
                                '.', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '#', '#', '#',
                                '.', '#', '#', '#', '.', '.', '#',
                                '.', '.', '.', '.', '#', '#', '#', '.', '.', '#', '.', '.', '.', '.', '#', '#', '#',
                                '#', '.', '#', '.', '.', '.', '.']
        d10 = Day10('../Resources/Day10/input')
        actual_value_task1 = d10.task1()
        self.assertEqual(expected_value_task1, actual_value_task1)
        self.assertEqual(expected_value_task2, d10.crt)
