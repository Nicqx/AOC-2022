import math


class Monkeys:
    monkey_list = []
    mod = None

    def __init__(self):
        self.monkey_list.clear()

    def calc_mod(self):
        self.mod = math.prod([m.test_val for m in self.monkey_list])

    def add_monkey(self, m):
        self.monkey_list.append(m)

    def give_monkey(self, name, value):
        for monkey in self.monkey_list:
            if monkey.name == name:
                monkey.starting_items.append(value)
                break

    def monkey_business(self):
        result = []
        for monkey in self.monkey_list:
            result.append(monkey.inspected_items)
        result.sort(reverse=True)
        return result[0] * result[1]

    def round(self):
        for monkey in self.monkey_list:
            results = monkey.action()
            for result in results:
                self.give_monkey(result[1], result[0])


class Monkey:
    name = 0
    starting_items = []
    inspected_items = 0
    boring_val = True
    test_val = ""
    operation_val = ""
    if_true = 0
    if_false = 0
    mod = None

    def __init__(self, name, boring_val, starting_items, test_val, operation_val, if_true, if_false):
        self.starting_items.clear()
        self.name = name
        self.boring_val = boring_val
        self.starting_items = starting_items
        self.test_val = test_val
        self.operation_val = operation_val
        self.if_true = if_true
        self.if_false = if_false

    def operation(self, old):
        new_elem = eval(self.operation_val)
        self.inspected_items += 1
        return new_elem

    def boring(self, x):
        return int(x / 3)

    def test(self, x):
        if (x % self.test_val) == 0:
            return self.if_true
        else:
            return self.if_false

    def action(self):
        result = []
        while len(self.starting_items) != 0:
            element = self.starting_items.__getitem__(0)
            self.starting_items.__delitem__(0)
            new_element = self.operation(element)
            if self.boring_val:
                new_element = self.boring(new_element)
            else:
                new_element %= self.mod
            result.append([new_element, self.test(new_element)])
        return result


class Day11:
    monkeys = Monkeys()
    operations = []

    def __init__(self, file):
        self.operations.clear()
        self.monkeys = Monkeys()
        with open(file) as f:
            self.operations = f.readlines()

    def task1(self):
        i = 0
        while i < len(self.operations):
            name = self.operations[i].removesuffix(":\n").removeprefix("Monkey ")
            i += 1
            starting_items = list(map(int, self.operations[i].removeprefix("  Starting items: ").split(", ")))
            i += 1
            operation_val = self.operations[i].removeprefix("  Operation: new = ").removesuffix("\n")
            i += 1
            test_val = int(self.operations[i].removeprefix("  Test: divisible by ").removesuffix("\n"))
            i += 1
            if_true = self.operations[i].removeprefix("    If true: throw to monkey ").removesuffix("\n")
            i += 1
            if_false = self.operations[i].removeprefix("    If false: throw to monkey ").removesuffix("\n")
            i += 1
            i += 1
            self.monkeys.add_monkey(Monkey(name, True, starting_items, test_val, operation_val, if_true, if_false))

        for i in range(20):
            self.monkeys.round()

        return str(self.monkeys.monkey_business())

    def task2(self):
        i = 0
        while i < len(self.operations):
            name = self.operations[i].removesuffix(":\n").removeprefix("Monkey ")
            i += 1
            starting_items = list(map(int, self.operations[i].removeprefix("  Starting items: ").split(", ")))
            i += 1
            operation_val = self.operations[i].removeprefix("  Operation: new = ").removesuffix("\n")
            i += 1
            test_val = int(self.operations[i].removeprefix("  Test: divisible by ").removesuffix("\n"))
            i += 1
            if_true = self.operations[i].removeprefix("    If true: throw to monkey ").removesuffix("\n")
            i += 1
            if_false = self.operations[i].removeprefix("    If false: throw to monkey ").removesuffix("\n")
            i += 1
            i += 1
            self.monkeys.add_monkey(Monkey(name, False, starting_items, test_val, operation_val, if_true, if_false))

        self.monkeys.calc_mod()
        for monkey in self.monkeys.monkey_list:
            monkey.mod = self.monkeys.mod

        for i in range(10000):
            self.monkeys.round()

        return str(self.monkeys.monkey_business())
