from typing import List


def transpose(data: List[List[int]]) -> List[List[int]]:
    return [*zip(*data)]


def bit_list_to_int(bits: List[int]):
    x = 0
    for bit in bits:
        x = (x << 1) + bit
    return x


def find_code_recursive(index, rows, bit_criteria) -> int:

    indexed_column = transpose(rows)[index]

    new_rows = [row for row in rows if bit_criteria(indexed_column, row[index])]

    if len(new_rows) == 1:
        return bit_list_to_int(new_rows[0])

    return find_code_recursive(index + 1, new_rows, bit_criteria)


def oxygen_bit_criteria(column, bit):
    return bit == (sum(column) >= len(column) / 2)


def co2_bit_criteria(column, bit):
    return bit == (sum(column) < len(column) / 2)


def solve(path: str) -> int:

    rows = [[int(char) for char in line.strip()] for line in open(path)]

    oxygen = find_code_recursive(0, rows, oxygen_bit_criteria)
    co2 = find_code_recursive(0, rows, co2_bit_criteria)

    return oxygen * co2


print(solve("days/3/mike/test.txt"))
print(solve("days/3/mike/input.txt"))
