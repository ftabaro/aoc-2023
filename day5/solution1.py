import re


def parse_ranges(seeds: list[int], ranges: list[tuple[int, int, int]]) -> list[int]:
    mapping = []
    for values in ranges:
        dest, source, r = values

        tomap = list(filter(lambda x: source <= x < source + r, seeds))

        if len(tomap) == 0:
            continue

        diff = map(lambda x: x - source, tomap)
        idx = map(lambda x: seeds.index(x), tomap)

        for i, d in zip(idx, diff):
            mapping.append((i, dest + d))

    for i, d in mapping:
        seeds[i] = d

    return seeds


def main(path: str) -> int:
    """
    Day 5 solution to part 1
    """

    with open(path, encoding="utf-8") as file_handler:
        seeds = file_handler.readline()
        seeds = [int(x) for x in re.findall(r"\d+", seeds)]

        ranges = []
        for line in file_handler:
            line = line.strip()
            if "map" in line:
                continue
            elif line != "" and not "map" in line:
                dest, source, r = [int(x) for x in re.findall(r"\d+", line)]
                ranges.append((dest, source, r))
            else:
                seeds = parse_ranges(seeds, ranges)
                ranges = []

    seeds = parse_ranges(seeds, ranges)

    return min(seeds)


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)

# 452473875 is too low
