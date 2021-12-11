from typing import List


def transpose(data: List[List[int]]) -> List[List[int]]:
    return list(zip(*data))


def bit_list_to_int(bits: List[int]):
    x = 0
    for bit in bits:
        x = (x << 1) + bit
    return x


def get_bit_recursive(index, rows, bit_criteria):

    indexed_column = transpose(rows)[index]

    new_rows = [row for row in rows if bit_criteria(indexed_column, row[index])]

    if len(new_rows) == 1:
        return new_rows[0]

    return get_bit_recursive(index + 1, new_rows, bit_criteria)


def oxygen_bit_criteria(column, bit):
    return bit == (sum(column) >= len(column) / 2)


def co2_bit_criteria(column, bit):
    return bit == (sum(column) < len(column) / 2)


def solve(path: str) -> int:

    rows = [list(int(char) for char in line.strip()) for line in open(path)]

    oxygen = bit_list_to_int(get_bit_recursive(0, rows, oxygen_bit_criteria))
    co2 = bit_list_to_int(get_bit_recursive(0, rows, co2_bit_criteria))

    return oxygen * co2


print(solve("days/3/mike/test.txt"))
print(solve("days/3/mike/input.txt"))
