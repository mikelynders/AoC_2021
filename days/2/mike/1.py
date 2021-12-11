from typing import Callable, Tuple, Dict

command_map_1: Dict[str, Callable[[int, int, int, int], Tuple[int, int, int]]] = {
    "down": lambda a, d, p, m: (a, d + m, p),
    "up": lambda a, d, p, m: (a, d - m, p),
    "forward": lambda a, d, p, m: (
        a,
        d,
        p + m,
    ),
}

command_map_2: Dict[str, Callable[[int, int, int, int], Tuple[int, int, int]]] = {
    "down": lambda a, d, p, m: (a + m, d, p),
    "up": lambda a, d, p, m: (a - m, d, p),
    "forward": lambda a, d, p, m: (
        a,
        d + a * m,
        p + m,
    ),
}


def make_reducer(commandMap):
    return lambda a, d, p, c: commandMap[c[0]](a, d, p, c[1])


def solve(path: str, command_map) -> int:
    def parse_line(input: str) -> Tuple[str, int]:
        data = input.rstrip().split(" ")
        return data[0], int(data[1])

    reducer = make_reducer(command_map)

    commands = [parse_line(x) for x in open(path, "r")]

    aim, depth, position = 0, 0, 0

    for command in commands:
        aim, depth, position = reducer(aim, depth, position, command)

    return position * depth


def solve_part(command_map):
    print(solve("./days/2/mike/test.txt", command_map))
    print(solve("./days/2/mike/input.txt", command_map))


solve_part(command_map_1)
solve_part(command_map_2)
