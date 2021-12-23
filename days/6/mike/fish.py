from typing import Counter, Dict, List
from typing_extensions import IntVar


class FishSchool:
    def __init__(self, data: List[int]):
        self.data = data

    def from_list(data: List[int]):
        new_data = [0] * 9
        for key, value in Counter(data).items():
            new_data[key] = value

        return FishSchool(new_data)

    def simulate_day(self):
        return FishSchool(
            [*self.data[1:7], self.data[7] + self.data[0], self.data[8], self.data[0]]
        )

    def score(self):
        return sum(self.data)


def solve(path: str, days: int):
    with open(path) as f:
        fishes = [int(x) for x in f.readlines()[0].strip().split(",")]

    fish_school = FishSchool.from_list(fishes)

    for x in range(days):
        fish_school = fish_school.simulate_day()

    return fish_school.score()


print(solve("days/6/mike/input.txt", 256))
