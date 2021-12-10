from typing import Callable, Tuple, Dict
from functools import reduce

commandMap1: Dict[str, Callable[[int, int, int, int], Tuple[int, int, int]]] = {
    "down": lambda a, d, p, m: (a, d + m, p),
    "up": lambda a, d, p, m: (a, d - m, p),
    "forward": lambda a, d, p, m: (
        a,
        d,
        p + m,
    ),
}

commandMap2: Dict[str, Callable[[int, int, int, int], Tuple[int, int, int]]] = {
    "down": lambda a, d, p, m: (a + m, d, p),
    "up": lambda a, d, p, m: (a - m, d, p),
    "forward": lambda a, d, p, m: (
        a,
        d + a * m,
        p + m,
    ),
}


def makeReducer(commandMap):
    return lambda a, d, p, c: commandMap[c[0]](a, d, p, c[1])


def solve(path: str, commandMap) -> int:
    def parseLine(input: str) -> Tuple[str, int]:
        data = input.rstrip().split(" ")
        return data[0], int(data[1])

    reducer = makeReducer(commandMap)

    commands = [parseLine(x) for x in open(path, "r")]

    aim, depth, position = 0, 0, 0

    for command in commands:
        aim, depth, position = reducer(aim, depth, position, command)

    return position * depth


def solvePart(commandMap):
    print(solve("./days/2/mike/test.txt", commandMap))
    print(solve("./days/2/mike/input.txt", commandMap))


solvePart(commandMap1)
solvePart(commandMap2)
