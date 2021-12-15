from typing import List
from utils import transpose, bit_list_to_int


def solve(path: str) -> int:

    columns = list(
        transpose([(int(char) for char in line.strip()) for line in open(path)])
    )  # transpose the matrix and covert each char to int

    bits = [
        sum(column) > len(column) / 2 for column in columns
    ]  # determine if number of 1's in each column is more than half

    gamma = epsilon = 0
    for bit in bits:
        gamma, epsilon = bit_list_to_int(gamma, bit), bit_list_to_int(
            epsilon, not bit
        )

    return gamma * epsilon


print(solve("days/3/mike/test.txt"))
print(solve("days/3/mike/input.txt"))
