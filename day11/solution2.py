from itertools import combinations


def find_empty_rows(universe: list[str]) -> list[int]:
    idx = []
    for i, row in enumerate(universe):
        if "#" not in row:
            idx.append(i)
    return idx


def find_empty_cols(universe: list[str]) -> list[int]:
    idx = []
    for j in range(len(universe[0])):
        col = ""
        for row in universe:
            col += row[j]
        if all(map(lambda x: x == ".", col)):
            idx.append(j)
    return idx


def find_galaxies(universe: list[str]) -> list[tuple[int, int]]:
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[0])):
            if universe[i][j] != ".":
                galaxies.append((i, j))
    return galaxies


def main(path: str, expansion_factor: int = 1000000) -> int:
    """
    Day 11 solution to part 2
    """

    universe = open(path, encoding="utf-8").read().splitlines()
    idx_rows = find_empty_rows(universe)
    idx_cols = find_empty_cols(universe)
    galaxies = find_galaxies(universe)

    for i in range(len(galaxies)):
        xg, yg = galaxies[i]

        bx = len(list(filter(lambda x: x < xg, idx_rows)))
        by = len(list(filter(lambda y: y < yg, idx_cols)))

        expansionx = bx * (expansion_factor - 1) if expansion_factor > 1 else bx
        expansiony = by * (expansion_factor - 1) if expansion_factor > 1 else by

        xfinal = xg + expansionx
        yfinal = yg + expansiony

        galaxies[i] = (xfinal, yfinal)

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

# 543018317006
