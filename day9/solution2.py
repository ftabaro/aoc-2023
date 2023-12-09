import sys

if sys.version_info.major == 3 and sys.version_info.minor < 10:
    from typing import Generator

    def pairwise(values: list[int]) -> Generator:
        return zip(values[:-1], values[1:])

else:
    from itertools import pairwise


def diff(series: list[int]) -> list[int]:
    first_values = [series[0]]
    values = series
    while not all(map(lambda x: x == 0, values)):
        differences = map(lambda x: x[1] - x[0], pairwise(values))
        differences = list(differences)
        first_values.append(differences[0])
        values = differences
    first_values = first_values[::-1]
    for i in range(1, len(first_values)):
        first_values[i] = first_values[i] - first_values[i - 1]
    return first_values[-1]


def main(path: str) -> int:
    """
    Day 9 solution to part 2
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
