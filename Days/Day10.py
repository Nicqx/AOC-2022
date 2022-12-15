class Day10:
    commands = []
    cycle = 1
    register_x = 1
    signal_strength = 0
    crt = ["." for i in range(40 * 6)]

    def __init__(self, file):
        self.commands.clear()
        with open(file) as f:
            for line in f.readlines():
                self.commands.append(line.removesuffix("\n"))

    def task1(self):
        for command in self.commands:
            if command == "noop":
                self.check_signal()
                self.draw_crt()
                self.cycle += 1
            elif command.startswith("addx "):
                self.check_signal()
                self.draw_crt()
                self.cycle += 1
                self.check_signal()
                self.draw_crt()
                self.register_x += int(command.removeprefix("addx "))
                self.cycle += 1
        return str(self.signal_strength)

    def task2(self):
        return ""

    def check_signal(self):
        if (self.cycle - 20) % 40 == 0:
            self.signal_strength += (self.cycle * self.register_x)

    def draw_crt(self):
        pixel = (self.cycle - 1) % 40
        if (pixel == self.register_x) or (pixel == self.register_x - 1) or (pixel == self.register_x + 1):
            self.set_lit(pixel + (int((self.cycle - 1) / 40)) * 40)

    def print_crt(self):
        for i in range(40 * 6):
            if i % 40 == 0:
                print("\n", end='')
            print(self.crt[i], end='')
        print("\n", end='')

    def set_lit(self, x):
        self.crt[x] = "#"
