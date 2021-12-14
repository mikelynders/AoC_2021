from typing import List


def transpose(data: List[List[int]]) -> List[List[int]]:
    return [*zip(*data)]
