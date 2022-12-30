import sys
from collections import deque


class Day12:
    level_map = "SabcdefghijklmnopqrstuvwxyzE"
    map_table = []
    level_table = []
    paths = deque()
    s_e_path = []
    max_x = 0
    max_y = 0
    start = []
    end = []

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
        self.start = self.get_coord('S')
        self.end = self.get_coord('E')
        self.map_table[self.start[1]][self.start[0]] = 'a'
        self.map_table[self.end[1]][self.end[0]] = 'z'
        self.max_x = len(self.map_table[0])
        self.max_y = len(self.map_table)
        self.crate_level_table()
        self.paths.append([self.start])
        while len(self.paths) > 0:
            self.gen_route(self.paths.popleft())

        return str(self.find_shortest_path())

    def find_shortest_path(self):
        minimal = sys.maxsize
        for item in self.s_e_path:
            if len(item) < minimal:
                minimal = len(item)
        return minimal - 1

    def gen_route(self, path):
        point = path[-1]
        point_value = self.level_table[point[1]][point[0]]
        if self.check_if_the_e_reached(path):
            return
        # up
        if (point[0] >= 1) and not (path.__contains__([point[0] - 1, point[1]])) and self.compare_the_values(
                self.level_table[point[1]][point[0] - 1], point_value):
            p = path.copy()
            p.append([point[0] - 1, point[1]])
            self.paths.append(p)
        # down
        if (point[0] < self.max_x - 1) and not (
                path.__contains__([point[0] + 1, point[1]])) and self.compare_the_values(
                self.level_table[point[1]][point[0] + 1], point_value):
            p = path.copy()
            p.append([point[0] + 1, point[1]])
            self.paths.append(p)
        # left
        if (point[1] >= 1) and not (path.__contains__([point[0], point[1] - 1])) and self.compare_the_values(
                self.level_table[point[1] - 1][point[0]], point_value):
            p = path.copy()
            p.append([point[0], point[1] - 1])
            self.paths.append(p)
        # right
        if (point[1] < self.max_y - 1) and not (
                path.__contains__([point[0], point[1] + 1])) and self.compare_the_values(
                self.level_table[point[1] + 1][point[0]], point_value):
            p = path.copy()
            p.append([point[0], point[1] + 1])
            self.paths.append(p)

    @staticmethod
    def compare_the_values(new, old):
        return new == old or new == old + 1 or new < old

    def check_if_the_e_reached(self, path):
        if path[-1] == self.end:
            self.s_e_path.append(path)
            return True
        else:
            return False

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
