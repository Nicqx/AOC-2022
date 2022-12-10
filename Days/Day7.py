class Dir:
    name = ""
    content = []
    parent = None

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Day7:
    directory_list = [Dir("/", None)]

    commands = []

    def __init__(self, file):
        with open(file) as f:
            line = f.readline()
            while line != "":
                self.commands.append(line.removesuffix("\n"))
                line = f.readline()

    def task1(self):
        actual_directory = None
        for line in self.commands:
            if line == "":
                break
            elif line == "$ cd ..":
                actual_directory = actual_directory.parent
                continue
            elif line.startswith("$ cd "):
                actual_directory = self.directory_list.index(Dir(line.removeprefix("$ cd "), None))
                continue
            elif line == "$ ls":
                continue
            elif line.startswith("dir "):
                self.directory_list.append(Dir(line.removeprefix("dir "), actual_directory))
                actual_directory.content.append(Dir(line.removeprefix("dir "), actual_directory))
            else:
                actual_directory.content.append(
                    File(line.split(" ")[1], int(line.split(" ")[0])))

        # every_directory = []
        # for file in self.every_file:
        #     if isinstance(file, Dir):
        #         every_directory.append(file.name)
        #
        total_sum = 0
        # for element in every_directory:
        #     actual = self.calculate_content(element)
        #     if int(actual) <= 100000:
        #         total_sum += int(actual)

        return str(total_sum)

    def calculate_content(self, name):
        sum_size = 0
        for file in self.every_file:
            if isinstance(file, File) and file.parent == name:
                sum_size += file.size
            elif isinstance(file, Dir) and file.parent == name:
                sum_size += self.calculate_content(file.name)
        return sum_size
