class Hamster:
    def __init__(self, h, g):
        self.h = h
        self.g = g

    def total_food_for_hamster(self, n):
        return self.h + n * self.g

    @staticmethod
    def find_number_of_hamsters(input_file):
        with open(input_file, mode="r") as f:
            s = int(f.readline())
            c = int(f.readline())
            hamsters = []
            for i in range(c):
                hams = Hamster(*list(map(int, f.readline().split(" "))))
                if hams.h <= s:
                    hamsters.append(hams)
        result = 0
        while result < len(hamsters):
            result += 1
            hamsters.sort(key=lambda hamster: hamster.total_food_for_hamster(result - 1))
            s_current = sum(hamster.total_food_for_hamster(result - 1) for hamster in hamsters[:result])
            if s_current > s:
                result -= 1
                break
        with open("hamsters_out.txt", mode="w") as f:
            f.write(f"{result}")
        return result