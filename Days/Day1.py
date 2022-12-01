class Day1:
    elf_list = {}
    elf = 0

    def __init__(self, file):
        self.elf_list.clear()
        with open(file) as f:
            for line in f.readlines():
                if line == "\n":
                    self.elf += 1
                else:
                    if self.elf_list.keys().__contains__(self.elf):
                        self.elf_list[self.elf] = self.elf_list.get(self.elf) + int(line)
                    else:
                        self.elf_list[self.elf] = int(line)

    def task1(self):
        return str(self.elf_list.get(max(self.elf_list, key=self.elf_list.get)))

    def task2(self):
        max_three = self.elf_list.pop(max(self.elf_list, key=self.elf_list.get))
        max_three += self.elf_list.pop(max(self.elf_list, key=self.elf_list.get))
        max_three += self.elf_list.pop(max(self.elf_list, key=self.elf_list.get))
        return str(max_three)
