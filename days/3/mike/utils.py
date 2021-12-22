from typing import List


def transpose(data: List[List[int]]) -> List[List[int]]:
    return list(zip(*data))


def bit_list_to_int(bits: List[int]):
    x = 0
    for bit in bits:
        x = (x << 1) + bit
    return x
