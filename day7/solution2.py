from collections import Counter
from re import T


def val(c: str) -> int:
    return "J23456789TQKA".index(c)


def get_count(hand: str) -> list[int]:
    if "J" in hand:
        counts = []
        for c in "23456789TQKA":
            x = hand.replace("J", c)
            count = Counter(x)
            counts.append(sorted(count.values(), reverse=True))
        ret = max(counts)
    else:
        count = Counter(hand)
        ret = sorted(count.values(), reverse=True)
    return ret


def main(path: str) -> int:
    """
    Day 7 solution to part 2
    """

    lines = [line.strip().split(" ") for line in open(path, encoding="utf-8")]
    lines = [[line[0], int(line[1])] for line in lines]

    for line in lines:
        line += get_count(line[0])
        line += [val(char) for char in line[0]]

    lines = sorted(lines, key=lambda x: x[2:])

    return sum([line[1] * (i + 1) for i, line in enumerate(lines)])


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
