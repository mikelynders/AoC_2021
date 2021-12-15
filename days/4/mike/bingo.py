from dataclasses import dataclass
from io import FileIO, TextIOWrapper
from typing import List, Union
from utils import transpose


@dataclass(frozen=True)
class Board:
    rows: List[List[int]]

    def transpose(self):
        return transpose(self.rows)

    def flatten(self):
        return [i for j in self.rows for i in j]

    def is_winner(self, numbers: List[int]):
        def testRows(rows):
            def testrow(row):
                return all((x in numbers) for x in row)

            return any([testrow(row) for row in rows])

        return testRows(self.rows) or testRows(transpose(self.rows))

    def score(self, numbers: List[int]):
        return numbers[-1] * sum([x for x in self.flatten() if not x in numbers])

    def parse(f: TextIOWrapper, rows=[]):
        line = f.readline()
        if line == "":
            return Board(rows) if len(rows) > 0 else None
        if line == "\n":
            return Board(rows) if len(rows) > 0 else Board.parse(f)

        row = [int(substring) for substring in line.split()]

        return Board.parse(
            f,
            rows=[*rows, row],
        )


class BingoParser:
    def parseBoards(f: TextIOWrapper, boards: List[Board] = []) -> List[Board]:
        board = Board.parse(f)
        if board == None:
            return boards

        return BingoParser.parseBoards(f, boards=[*boards, board])

    def parseNumbers(f: TextIOWrapper):
        return [int(char) for char in f.readline().replace(",", " ").split()]

    def parse(path):
        with open(path) as f:
            numbers = BingoParser.parseNumbers(f)
            boards = BingoParser.parseBoards(f)

        return numbers, boards


numbers, boards = BingoParser.parse("days/4/mike/input.txt")


def part1() -> int:

    for i in range(len(numbers)):
        called_numbers = numbers[:i]
        for board in boards:
            if board.is_winner(called_numbers):
                return board.score(called_numbers)


def part2(losing_boards=boards, index=0) -> int:
    called_numbers = numbers[:index]

    if len(losing_boards) <= 1 and losing_boards[0].is_winner(called_numbers):
        return losing_boards[0].score(called_numbers)

    return part2(
        losing_boards=[
            board for board in losing_boards if not board.is_winner(called_numbers)
        ],
        index=index + 1,
    )


print(part1())
print(part2())
