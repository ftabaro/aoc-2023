from itertools import combinations


def expand_rows(universe: list[str]) -> list[str]:
    idx = []
    for i, row in enumerate(universe):
        if "#" not in row:
            idx.append(i)

    expanded = []
    for i in range(len(universe)):
        if i in idx:
            expanded.append("." * len(universe[0]))
        expanded.append(universe[i])
    return expanded


def expand_cols(universe: list[str]) -> list[str]:
    idx = []
    for j in range(len(universe[0])):
        col = ""
        for row in universe:
            col += row[j]
        if all(map(lambda x: x == ".", col)):
            idx.append(j)

    expanded = []
    for i in range(len(universe)):
        row = universe[i]
        expanded_row = ""
        for j in range(len(row)):
            if j in idx:
                expanded_row += "."
            expanded_row += row[j]
        expanded.append(expanded_row)

    return expanded


def find_galaxies(universe: list[str]) -> list[tuple[int, int]]:
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] != ".":
                galaxies.append((i, j))
    return galaxies


def main(path: str) -> int:
    """
    Day 11 solution to part 1
    """

    universe = open(path, encoding="utf-8").read().splitlines()
    universe = expand_rows(universe)
    universe = expand_cols(universe)
    galaxies = find_galaxies(universe)

    distances = []
    for ga, gb in combinations(galaxies, 2):
        xa, ya = ga
        xb, yb = gb

        dx = abs(xb - xa)
        dy = abs(yb - ya)

        d = dx + dy

        distances.append(d)

    return sum(distances)


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
