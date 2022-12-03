class Day3:
    rucksacks = []

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, file):
        self.rucksacks.clear()

        with open(file) as f:
            for line in f.readlines():
                self.rucksacks.append(line.removesuffix("\n"))

    def task1(self):
        priority_list = []
        priority_list.clear()
        for pack in self.rucksacks:
            first_compartment = pack[0:int(len(pack) / 2)]
            second_compartment = pack[int(len(pack) / 2):len(pack)]
            for letter in first_compartment:
                if second_compartment.__contains__(letter):
                    priority_list.append(self.chars.find(letter) + 1)
                    break
        return str(sum(priority_list))

    def task2(self):
        priority_list = []
        priority_list.clear()
        for lines in range(0, len(self.rucksacks) - 2, 3):
            for letter in self.rucksacks[lines]:
                if self.rucksacks[lines + 1].__contains__(letter) and self.rucksacks[lines + 2].__contains__(letter):
                    priority_list.append(self.chars.find(letter) + 1)
                    break
        return str(sum(priority_list))
