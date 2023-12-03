import re
import math


def main(path: str) -> int:
    """
    Day 3 solution to part 2
    """

    d = {}

    with open(path, encoding="utf-8") as file_handler:
        schematics = [line.strip() for line in file_handler]

    symbol_indexes = {
        (i, j)
        for i, line in enumerate(schematics)
        for j, char in enumerate(line)
        if char != "." and not char.isdigit()
    }

    for i, line in enumerate(schematics):
        for match in re.finditer("[0-9]+", line):
            number = int(match.group())
            s, e = match.span()

            neighborhood = {
                (i + ii, j + jj)
                for ii in (-1, 0, 1)
                for jj in (-1, 0, 1)
                for j in range(s, e)
            }

            intersection = symbol_indexes & neighborhood

            for symbol_index in intersection:
                if symbol_index not in d:
                    d[symbol_index] = []
                d[symbol_index].append(number)

    tot = sum(math.prod(v) for k, v in d.items() if len(v) == 2)
    return tot


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
