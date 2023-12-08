from collections import Counter


def val(c: str) -> int:
    return "23456789TJQKA".index(c)


def main(path: str) -> int:
    """
    Day 7 solution to part 1
    """

    lines = [line.strip().split(" ") for line in open(path, encoding="utf-8")]
    lines = [[line[0], int(line[1])] for line in lines]

    for line in lines:
        count = Counter(line[0])
        line += sorted(count.values(), reverse=True)
        line += [val(char) for char in line[0]]

    lines = sorted(lines, key=lambda x: x[2:])
    return sum([line[1] * (i + 1) for i, line in enumerate(lines)])


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
