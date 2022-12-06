class Day6:
    input = ""

    def __init__(self, file):
        with open(file) as f:
            self.input = f.readline()

    def task1(self):
        buffer = ""
        for char in range(len(self.input)):
            buffer += self.input[char]
            if len(buffer) >= 5:
                tmp_set = set()
                buffer = buffer[1:]
                for i in range(4):
                    tmp_set.add(buffer[i])
                if len(tmp_set) == 4:
                    return str(char + 1)

    def task2(self):
        buffer = ""
        for char in range(len(self.input)):
            buffer += self.input[char]
            if len(buffer) >= 15:
                tmp_set = set()
                buffer = buffer[1:]
                for i in range(14):
                    tmp_set.add(buffer[i])
                if len(tmp_set) == 14:
                    return str(char + 1)
