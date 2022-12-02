class Day2:
    my_list = []
    opponent_list = []
    my_score = 0

    def __init__(self, file):
        self.my_list.clear()
        self.opponent_list.clear()
        self.my_score = 0

        with open(file) as f:
            for line in f.readlines():
                self.my_list.append(line.split(" ")[1].removesuffix("\n"))
                self.opponent_list.append(line.split(" ")[0])

    def task1(self):
        self.my_score = 0
        for rps_round in range(len(self.my_list)):
            match self.my_list[rps_round]:
                case "X":
                    self.my_score += 1
                    match self.opponent_list[rps_round]:
                        case "A":
                            self.my_score += 3
                        case "C":
                            self.my_score += 6
                case "Y":
                    self.my_score += 2
                    match self.opponent_list[rps_round]:
                        case "A":
                            self.my_score += 6
                        case "B":
                            self.my_score += 3
                case "Z":
                    self.my_score += 3
                    match self.opponent_list[rps_round]:
                        case "C":
                            self.my_score += 3
                        case "B":
                            self.my_score += 6

        return str(self.my_score)

    def task2(self):
        self.my_score = 0
        new_my_list = []
        for rps_round in range(len(self.my_list)):
            match self.my_list[rps_round]:
                case "X":
                    match self.opponent_list[rps_round]:
                        case "A":
                            new_my_list.append("Z")
                        case "B":
                            new_my_list.append("X")
                        case "C":
                            new_my_list.append("Y")
                case "Y":
                    match self.opponent_list[rps_round]:
                        case "A":
                            new_my_list.append("X")
                        case "B":
                            new_my_list.append("Y")
                        case "C":
                            new_my_list.append("Z")
                case "Z":
                    match self.opponent_list[rps_round]:
                        case "A":
                            new_my_list.append("Y")
                        case "B":
                            new_my_list.append("Z")
                        case "C":
                            new_my_list.append("X")

        for rps_round in range(len(new_my_list)):
            match new_my_list[rps_round]:
                case "X":
                    self.my_score += 1
                    match self.opponent_list[rps_round]:
                        case "A":
                            self.my_score += 3
                        case "C":
                            self.my_score += 6
                case "Y":
                    self.my_score += 2
                    match self.opponent_list[rps_round]:
                        case "A":
                            self.my_score += 6
                        case "B":
                            self.my_score += 3
                case "Z":
                    self.my_score += 3
                    match self.opponent_list[rps_round]:
                        case "C":
                            self.my_score += 3
                        case "B":
                            self.my_score += 6

        return str(self.my_score)
