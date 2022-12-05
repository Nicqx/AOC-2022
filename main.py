from Days.Day1 import Day1
from Days.Day2 import Day2
from Days.Day3 import Day3
from Days.Day4 import Day4
from Days.Day5 import Day5

if __name__ == '__main__':
    d1 = Day1('Resources/Day1/input')
    print("day1 task1: " + d1.task1())
    print("day1 task2: " + d1.task2())

    d2 = Day2('Resources/Day2/input')
    print("day2 task1: " + d2.task1())
    print("day2 task2: " + d2.task2())

    d3 = Day3('Resources/Day3/input')
    print("day3 task1: " + d3.task1())
    print("day3 task2: " + d3.task2())

    d4 = Day4('Resources/Day4/input')
    print("day4 task1: " + d4.task1())
    print("day4 task2: " + d4.task2())

    d5 = Day5('Resources/Day5/input')
    print("day5 task1: " + d5.task1())
    d5 = Day5('Resources/Day5/input')
    print("day5 task2: " + d5.task2())
