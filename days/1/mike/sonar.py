from typing import ItemsView, List

test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
sonar = [int(x, base=10) for x in open("input.txt", "r")]


def count_increasing(items):
    return sum([x > items[i - 1] for i, x in enumerate(items) if i > 0])


def test1():
    result = count_increasing(test_data)
    print(result)
    assert result == 7


def solve1():
    print(count_increasing(sonar))


# test()
# solve()


def calc_rolling_sum(items):
    return [sum(items[i : i + 3]) for i, x in enumerate(items) if i < len(items) - 2]


def count_increasing_rolling(items):
    return count_increasing(calc_rolling_sum(items))


def test2():
    result = count_increasing_rolling(test_data)
    print(result)
    assert result == 5


def solve2():
    print(count_increasing_rolling(sonar))


test1()
solve1()
test2()
solve2()


print("Part 2:", sum([sonar[i] > sonar[i - 3] for i in range(3, len(sonar))]))
