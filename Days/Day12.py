import sys


class Day12:
    level_map = "SabcdefghijklmnopqrstuvwxyzE"
    map_table = []
    level_table = []
    paths = set()
    max_x = 0
    max_y = 0

    def __init__(self, file):
        self.map_table.clear()
        with open(file) as f:
            line = f.readline().removesuffix("\n")
            while line != "":
                one_line = []
                one_line.clear()
                for letter in line:
                    one_line.append(letter)
                self.map_table.append(one_line)
                line = f.readline().removesuffix("\n")

    def task1(self):
        counter = 0
        shortest = sys.maxsize
        start = self.get_coord('S')
        end = self.get_coord('E')
        self.map_table[start[1]][start[0]] = 'a'
        self.map_table[end[1]][end[0]] = 'z'
        self.max_x = len(self.map_table[0])
        self.max_y = len(self.map_table)
        self.crate_level_table()
        self.paths.add(tuple([start]))
        while (self.genPath()):
            pass

        return ""

    def genPath(self):
        is_new = False
        for path in self.paths:
            self.genRoute(path)

        return is_new

    def genRoute(self, path):
        point = path[-1]
        point_value = self.level_table[point[1]][point[0]]
        # up
        if (point[0] >= 1) and not (path.__contains__([point[0] - 1, point[1]])) and self.compare_the_values(
                self.level_table[point[1]][point[0] - 1], point_value):
            p = path
            p.add([point[0] - 1, point[1]])
            self.paths.add(tuple(p))
        # down
        if (point[0] < self.max_x - 1) and not (
                path.__contains__([point[0] + 1, point[1]])) and self.compare_the_values(
                self.level_table[point[1]][point[0] + 1], point_value):
            p = path
            p.add([point[0] + 1, point[1]])
            self.paths.add(tuple(p))
        # left
        if (point[1] >= 1) and not (path.__contains__([point[0], point[1] + 1])) and self.compare_the_values(
                self.level_table[point[1] + 1][point[0]], point_value):
            p = path
            p.add([point[0], point[1] + 1])
            self.paths.add(tuple(p))
        # right
        if (point[1] < self.max_y - 1) and not (
                path.__contains__([point[0], point[1] - 1])) and self.compare_the_values(
                self.level_table[point[1] - 1][point[0]], point_value):
            p = path
            p.add([point[0], point[1] - 1])
            self.paths.add(tuple(p))
        self.paths.remove(path)

    def compare_the_values(self, new, old):
        return new == old or new == old + 1 or new < old

    def collectValidRoutesFromPaths(self):
        pass

    def get_coord(self, char):
        for y in range(len(self.map_table)):
            for x in range(len(self.map_table[y])):
                if self.map_table[y][x] == char:
                    return [x, y]

    def get_value_fom_map(self, char):
        return self.level_map.index(char)

    def crate_level_table(self):
        for y in range(len(self.map_table)):
            row = []
            row.clear()
            for x in range(len(self.map_table[y])):
                row.append(self.get_value_fom_map(self.map_table[y][x]))
            self.level_table.append(row)
