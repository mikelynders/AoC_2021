from typing import Counter, List, Tuple
import re
from dataclasses import dataclass
from collections import Counter

VentPoint = Tuple[int, int]


def interpolate(a, b):
    return range(a, b + 1) if a < b else range(a, b - 1, -1)


@dataclass(frozen=True)
class VentLine:
    x1: int
    y1: int
    x2: int
    y2: int

    def to_vent_points(self, enable_diagonals=False) -> List[VentPoint]:

        if self.x1 == self.x2:
            return [(self.x1, y) for y in interpolate(self.y1, self.y2)]
        elif self.y1 == self.y2:
            return [(x, self.y1) for x in interpolate(self.x1, self.x2)]
        if enable_diagonals:
            return list(
                zip(interpolate(self.x1, self.x2), interpolate(self.y1, self.y2))
            )

    def parse(data: str):
        m = re.search("(\d+),(\d+)\s->\s(\d+),(\d+)", data)
        return VentLine(int(m[1]), int(m[2]), int(m[3]), int(m[4]))


def solve(path: str):
    with open(path) as f:
        vent_lines = [VentLine.parse(line) for line in f]

    counter = Counter(
        [
            vent_point
            for vent_line in vent_lines
            for vent_point in vent_line.to_vent_points()
        ]
    )

    score = len(list(x for x in counter.most_common() if x[1] >= 2))

    print(score)

    with open("days/5/mike/output.txt", "w") as f:
        for y in range(0, 10):
            for x in range(0, 10):
                f.write(str(counter[(x, y)]).replace("0", "."))
            f.write("\n")


solve("days/5/mike/input.txt")
