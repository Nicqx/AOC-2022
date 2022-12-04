class Day4:
    elf1 = []
    elf2 = []

    def __init__(self, file):
        self.elf1 = []
        self.elf2 = []

        with open(file) as f:
            for line in f.readlines():
                self.elf1.append(line.split(",")[0])
                self.elf2.append(line.split(",")[1].removesuffix("\n"))

    def task1(self):
        counter = 0
        for i in range(len(self.elf1)):
            e1_start = int(self.elf1[i].split("-")[0])
            e1_end = int(self.elf1[i].split("-")[1])
            e2_start = int(self.elf2[i].split("-")[0])
            e2_end = int(self.elf2[i].split("-")[1])
            if (e1_start <= e2_start and e1_end >= e2_end) or (e2_start <= e1_start and e2_end >= e1_end):
                counter += 1
        return str(counter)

    def task2(self):
        counter = 0
        for i in range(len(self.elf1)):
            e1_start = int(self.elf1[i].split("-")[0])
            e1_end = int(self.elf1[i].split("-")[1])
            e2_start = int(self.elf2[i].split("-")[0])
            e2_end = int(self.elf2[i].split("-")[1])
            if (e1_start <= e2_start <= e1_end) or (e2_start <= e1_start <= e2_end):
                counter += 1
        return str(counter)
