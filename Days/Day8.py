import numpy as np


class Day8:
    trees = []

    def __init__(self, file):
        self.trees.clear()
        with open(file) as f:
            line = f.readline().removesuffix("\n")
            i = 0
            while line != "":
                self.trees.append([])
                for ch in line:
                    self.trees[i].append(int(ch))
                line = f.readline().removesuffix("\n")
                i += 1

    def task1(self):
        counter = 0
        for i in range(1, len(self.trees) - 1):
            for j in range(1, len(self.trees[0]) - 1):
                if (self.check_right_visibility(i, j) or
                        self.check_left_visibility(i, j) or
                        self.check_upper_visibility(i, j) or
                        self.check_under_visibility(i, j)):
                    counter += 1

        counter += ((4 * len(self.trees)) - 4)
        return str(counter)

    def check_left_visibility(self, i, j):
        result = True
        for k in range(j):
            if self.trees[i][j] <= self.trees[i][k]:
                result = False
        return result

    def check_right_visibility(self, i, j):
        result = True
        for k in range(j + 1, len(self.trees[0])):
            if self.trees[i][j] <= self.trees[i][k]:
                result = False
        return result

    def check_upper_visibility(self, i, j):
        result = True
        for k in range(i):
            if self.trees[i][j] <= self.trees[k][j]:
                result = False
        return result

    def check_under_visibility(self, i, j):
        result = True
        for k in range(i + 1, len(self.trees)):
            if self.trees[i][j] <= self.trees[k][j]:
                result = False
        return result

    def task2(self):
        max_counter = 0
        for i in range(1, len(self.trees) - 1):
            for j in range(1, len(self.trees[0]) - 1):
                counter = self.check_left_scenic(i, j) * \
                          self.check_right_scenic(i, j) * \
                          self.check_upper_scenic(i, j) * \
                          self.check_under_scenic(i, j)
                max_counter = max(counter, max_counter)
        return str(max_counter)

    def check_left_scenic(self, i, j):
        result = 0
        for k in range(j-1, -1, -1):
            result += 1
            if self.trees[i][k] >= self.trees[i][j]:
                break

        return result

    def check_right_scenic(self, i, j):
        result = 0
        for k in range(j + 1, len(self.trees[0])):
            result += 1
            if self.trees[i][k] >= self.trees[i][j]:
                break

        return result

    def check_upper_scenic(self, i, j):
        result = 0
        for k in range(i-1, -1, -1):
            result += 1
            if self.trees[k][j] >= self.trees[i][j]:
                break
        return result

    def check_under_scenic(self, i, j):
        result = 0
        for k in range(i + 1, len(self.trees)):
            result += 1
            if self.trees[k][j] >= self.trees[i][j]:
                break
        return result
