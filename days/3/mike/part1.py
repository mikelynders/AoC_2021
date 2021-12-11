from typing import List


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return list(zip(*matrix))

def bit_list_to_int(bits: List[int]):
    x = 0
    for bit in bits:
        x = (x << 1) + bit
    return x


def solve(path: str) -> int:

    columns = list(
        transpose([(int(char) for char in line.strip()) for line in open(path)])
    )  # transpose the matrix and covert each char to int

    bits = [
        sum(column) > len(column) / 2 for column in columns
    ]  # determine if number of 1's in each column is more than half

    int_from_bits_iter = lambda x, bit: (x << 1) + bit

    gamma = epsilon = 0
    for bit in bits:
        gamma, epsilon = int_from_bits_iter(gamma, bit), int_from_bits_iter(
            epsilon, not bit
        )

    return gamma * epsilon


print(solve("days/3/mike/test.txt"))
print(solve("days/3/mike/input.txt"))

