class Day9:
    commands = []
    rope = []
    visited = set()

    def __init__(self, file):
        self.rope = []
        self.visited.clear()
        self.commands.clear()
        with open(file) as f:
            for line in f.readlines():
                if line != "\n":
                    self.commands.append(line.removesuffix("\n"))

    def task1(self):
        self.rope.clear()
        self.visited.clear()
        self.visited.add((0, 0))
        for i in range(2):
            self.rope.append([0, 0])
        self.process_commands()

        return str(len(self.visited))

    def task2(self):
        self.rope.clear()
        self.visited.clear()
        self.visited.add((0, 0))
        for i in range(10):
            self.rope.append([0, 0])
        self.process_commands()
        return str(len(self.visited))

    def process_commands(self):
        for command in self.commands:
            match (command.split(" ")[0]):
                case "R":
                    for i in range(int(command.split(" ")[1])):
                        self.rope[0][0] += 1
                        for j in range(1, len(self.rope)):
                            self.rope[j] = self.check_if_tail_needs_move(self.rope[j - 1], self.rope[j])
                case "L":
                    for i in range(int(command.split(" ")[1])):
                        self.rope[0][0] -= 1
                        for j in range(1, len(self.rope)):
                            self.rope[j] = self.check_if_tail_needs_move(self.rope[j - 1], self.rope[j])
                case "U":
                    for i in range(int(command.split(" ")[1])):
                        self.rope[0][1] += 1
                        for j in range(1, len(self.rope)):
                            self.rope[j] = self.check_if_tail_needs_move(self.rope[j - 1], self.rope[j])
                case "D":
                    for i in range(int(command.split(" ")[1])):
                        self.rope[0][1] -= 1
                        for j in range(1, len(self.rope)):
                            self.rope[j] = self.check_if_tail_needs_move(self.rope[j - 1], self.rope[j])

    def check_if_tail_needs_move(self, head, tail):
        # right
        if head[0] == tail[0] + 2 and head[1] == tail[1]:
            tail[0] += 1
        # left
        elif head[0] == tail[0] - 2 and head[1] == tail[1]:
            tail[0] -= 1
        # up
        elif head[1] == tail[1] + 2 and head[0] == tail[0]:
            tail[1] += 1
        # down
        elif head[1] == tail[1] - 2 and head[0] == tail[0]:
            tail[1] -= 1
        # up right
        elif (head[0] == tail[0] + 1 and head[1] == tail[1] + 2) or (
                head[0] == tail[0] + 2 and head[1] == tail[1] + 1) or (
                head[0] == tail[0] + 2 and head[1] == tail[1] + 2):
            tail[0] += 1
            tail[1] += 1
        # up left
        elif (head[0] == tail[0] - 1 and head[1] == tail[1] + 2) or (
                head[0] == tail[0] - 2 and head[1] == tail[1] + 1) or (
                head[0] == tail[0] - 2 and head[1] == tail[1] + 2):
            tail[0] -= 1
            tail[1] += 1
        # down right
        elif (head[0] == tail[0] + 1 and head[1] == tail[1] - 2) or (
                head[0] == tail[0] + 2 and head[1] == tail[1] - 1) or (
                head[0] == tail[0] + 2 and head[1] == tail[1] - 2):
            tail[0] += 1
            tail[1] -= 1
        # down left
        elif (head[0] == tail[0] - 2 and head[1] == tail[1] - 1) or (
                head[0] == tail[0] - 1 and head[1] == tail[1] - 2) or (
                head[0] == tail[0] - 2 and head[1] == tail[1] - 2):
            tail[0] -= 1
            tail[1] -= 1

        self.visited.add((self.rope[-1][0], self.rope[-1][1]))
        return tail
