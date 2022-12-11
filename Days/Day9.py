class Day9:
    commands = []
    h = [0, 0]
    t = [0, 0]
    visited = set()

    def __init__(self, file):
        self.h = [0, 0]
        self.t = [0, 0]
        self.visited.clear()
        self.commands.clear()
        with open(file) as f:
            for line in f.readlines():
                if line != "\n":
                    self.commands.append(line.removesuffix("\n"))

    def task1(self):
        self.visited.add((0, 0))
        for command in self.commands:
            match (command.split(" ")[0]):
                case "R":
                    for i in range(int(command.split(" ")[1])):
                        self.h[0] += 1
                        self.check_if_t_needs_move()
                case "L":
                    for i in range(int(command.split(" ")[1])):
                        self.h[0] -= 1
                        self.check_if_t_needs_move()
                case "U":
                    for i in range(int(command.split(" ")[1])):
                        self.h[1] += 1
                        self.check_if_t_needs_move()
                case "D":
                    for i in range(int(command.split(" ")[1])):
                        self.h[1] -= 1
                        self.check_if_t_needs_move()

        return str(len(self.visited))

    def check_if_t_needs_move(self):
        # right
        if self.h[0] == self.t[0] + 2 and self.h[1] == self.t[1]:
            self.t[0] += 1
        # left
        elif self.h[0] == self.t[0] - 2 and self.h[1] == self.t[1]:
            self.t[0] -= 1
        # up
        elif self.h[1] == self.t[1] + 2 and self.h[0] == self.t[0]:
            self.t[1] += 1
        # down
        elif self.h[1] == self.t[1] - 2 and self.h[0] == self.t[0]:
            self.t[1] -= 1
        # up right
        elif (self.h[0] == self.t[0] + 1 and self.h[1] == self.t[1] + 2) or (
                self.h[0] == self.t[0] + 2 and self.h[1] == self.t[1] + 1):
            self.t[0] += 1
            self.t[1] += 1
        # up left
        elif (self.h[0] == self.t[0] - 1 and self.h[1] == self.t[1] + 2) or (
                self.h[0] == self.t[0] -2 and self.h[1] == self.t[1] +1):
            self.t[0] -= 1
            self.t[1] += 1
        # down right
        elif (self.h[0] == self.t[0] +1 and self.h[1] == self.t[1] -2) or (
                self.h[0] == self.t[0] + 2 and self.h[1] == self.t[1] - 1):
            self.t[0] += 1
            self.t[1] -= 1
        # down left
        elif (self.h[0] == self.t[0] - 2 and self.h[1] == self.t[1] - 1) or (
                self.h[0] == self.t[0] - 1 and self.h[1] == self.t[1] - 2):
            self.t[0] -= 1
            self.t[1] -= 1

        self.visited.add((self.t[0], self.t[1]))
