import re


class Day5:
    cargo = {}
    movements = []

    def __init__(self, file):
        self.cargo.clear()
        self.movements.clear()

        with open(file) as f:
            loads = []
            line = f.readline()
            while line != "\n":
                loads.append(line.removesuffix("\n"))
                line = f.readline()
            line = f.readline()
            while line != "":
                self.movements.append(line.removesuffix("\n"))
                line = f.readline()

        for number in loads[-1].split(" "):
            if number != "":
                self.cargo[int(number)] = []

        for load in range(len(loads) - 1):
            if len(loads[load]) > 2 and loads[load][1] != " ":
                self.cargo.get(1).append(loads[load][1])
            if len(loads[load]) > 6 and loads[load][5] != " ":
                self.cargo.get(2).append(loads[load][5])
            if len(loads[load]) > 10 and loads[load][9] != " ":
                self.cargo.get(3).append(loads[load][9])
            if len(loads[load]) > 14 and loads[load][13] != " ":
                self.cargo.get(4).append(loads[load][13])
            if len(loads[load]) > 18 and loads[load][17] != " ":
                self.cargo.get(5).append(loads[load][17])
            if len(loads[load]) > 22 and loads[load][21] != " ":
                self.cargo.get(6).append(loads[load][21])
            if len(loads[load]) > 26 and loads[load][25] != " ":
                self.cargo.get(7).append(loads[load][25])
            if len(loads[load]) > 30 and loads[load][29] != " ":
                self.cargo.get(8).append(loads[load][29])
            if len(loads[load]) > 34 and loads[load][33] != " ":
                self.cargo.get(9).append(loads[load][33])

        for keys in self.cargo:
            tmp = []
            for element in self.cargo[keys]:
                tmp.insert(0, element)
            self.cargo[keys] = tmp

    def task1(self):
        result = ""
        for movement in self.movements:
            z = re.match(r"move (\d+) from (\d+) to (\d+)", movement)
            if z:
                for i in range(int(z.group(1))):
                    tmp = self.cargo[int(z.group(2))].pop()
                    self.cargo[int(z.group(3))].append(tmp)

        for keys in self.cargo:
            result += self.cargo[keys].pop()

        return result

    def task2(self):
        result = ""
        for movement in self.movements:
            z = re.match(r"move (\d+) from (\d+) to (\d+)", movement)
            if z:
                tmp = self.cargo[int(z.group(2))][-int(z.group(1)):]
                del (self.cargo[int(z.group(2))][-int(z.group(1)):])
                self.cargo[int(z.group(3))].extend(tmp)

        for keys in self.cargo:
            result += self.cargo[keys].pop()

        return result
