import re
import math


def solve(time: int, distance: int) -> int:
    time_press1 = math.floor((time - math.sqrt(time * time - 4 * distance)) / 2)
    time_press2 = math.ceil((time + math.sqrt(time * time - 4 * distance)) / 2)

    return len(list(range(time_press1 + 1, time_press2)))


def main(path: str) -> int:
    """
    Day 6 solution to part 2
    """

    with open(path, encoding="utf-8") as file_handler:
        lines = file_handler.readlines()

    time = int("".join(re.findall(r"\d+", lines[0])))
    distance = int("".join(re.findall(r"\d+", lines[1])))

    ret = solve(time, distance)

    return ret


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
