from typing import Callable, Tuple, Dict
from functools import reduce

commandsReactors: Dict[str, Callable[[int, int, int, int], Tuple[int, int, int]]] = {
    "down": lambda a, d, p, m: (a + m, d, p),
    "up": lambda a, d, p, m: (a - m, d, p),
    "forward": lambda a, d, p, m: (
        a,
        d + a * m,
        p + m,
    ),
}

def reducer(aim, depth, position, command):
    return commandsReactors[command[0]](aim, depth, position, command[1])


def solve(path: str) -> int:
    def parseLine(input: str) -> Tuple[str, int]:
        data = input.rstrip().split(" ")
        return data[0], int(data[1])

    commands = [parseLine(x) for x in open(path, "r")]

    aim, depth, position = 0, 0, 0

    for command in commands:
        aim, depth, position = reducer(aim, depth, position, command)

    return position * depth


print(solve("./days/2/test.txt"))
print(solve("./days/2/input.txt"))
