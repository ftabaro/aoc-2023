import sys

if sys.version_info.minor > 9:
    from itertools import pairwise, accumulate
else:
    from itertools import accumulate
    from typing import Generator

    def pairwise(values: list[int]) -> Generator:
        return zip(values[1:], values[::-1])


def diff(series: list[int]) -> list[int]:
    last_values = [series[-1]]

    values = series
    while not all(map(lambda x: x == 0, values)):
        differences = map(lambda x: x[1] - x[0], pairwise(values))
        differences = list(differences)
        last_values.append(differences[-1])
        values = differences

    last_values = last_values[::-1]
    s = list(accumulate(last_values))
    return s[-1]


def main(path: str) -> int:
    """
    Day 9 solution to part 1
    """
    numbers = []
    with open(path, encoding="utf-8") as file_handler:
        for series in file_handler:
            series = list(map(int, series.strip().split(" ")))
            last_value = diff(series)
            numbers.append(last_value)
    return sum(numbers)


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
