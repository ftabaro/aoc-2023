import sys
import math

sys.setrecursionlimit(20000)

allowed_symbols = {
    (0, -1): "-FL",
    (-1, 0): "|7F",
    (0, 1): "-J7",
    (1, 0): "L|J",
}

directions = {
    "S": [(0, -1), (-1, 0), (0, 1), (1, 0)],  # all directions
    "|": [(-1, 0), (1, 0)],  # NS
    "-": [(0, -1), (0, 1)],  # EW
    "L": [(-1, 0), (0, 1)],  # NE
    "J": [(-1, 0), (0, -1)],  # NW
    "7": [(1, 0), (0, -1)],  # SW
    "F": [(1, 0), (0, 1)],  # SE
    ".": [],
}


def get_neighbors(
    m: list[list[str]], r: int, c: int, d: int, visited: set[tuple[int, int]] = set()
) -> list[tuple[int, int]]:
    neighbors = set()

    n = m[r][c]

    allowed_directions = directions[n]

    for i, j in allowed_directions:
        rr = r + i
        cc = c + j
        if 0 <= rr < len(m) and 0 <= cc < len(m[0]):
            nn = m[rr][cc]
            if (not (rr, cc) in visited) and (nn in allowed_symbols[(i, j)]):
                neighbors.add((rr, cc, d + 1))
                visited.add((rr, cc))

    return neighbors, visited


def dfs(
    m: list[list[str]],
    r: int,
    c: int,
    visited: set[tuple[int, int]] = set(),
    corners: list[tuple[int, int]] = [],
) -> list[tuple[int, int]]:
    n = m[r][c]

    allowed_directions = directions[n]

    for i, j in allowed_directions:
        rr = r + i
        cc = c + j
        if 0 <= rr < len(m) and 0 <= cc < len(m[0]):
            nn = m[rr][cc]

            if (not (rr, cc) in visited) and (nn in allowed_symbols[(i, j)]):
                corners.append((r, c))
                visited.add((rr, cc))
                dfs(m, rr, cc, visited, corners)

    return corners


def get_start(_map: str) -> tuple[int, int]:
    start = _map.index("S")
    newlines = _map[:start].count("\n")
    start -= newlines

    _map = _map.splitlines()
    ncols = len(_map[0])

    (r, c) = divmod(start, ncols)

    return _map, r, c


def shoelace(x, y):
    """Calculates the area of an arbitrary polygon given its verticies"""
    area = 0.0
    for i in range(len(x)):
        ii = (i + 1) % len(x)
        area += x[i] * y[ii] - x[ii] * y[i]
    return abs(area) / 2


def main(path: str) -> int:
    """
    Day 10 solution to part 1
    """

    _map = open(path, encoding="utf-8").read()
    _map, start_row, start_col = get_start(_map)

    visited = set([(start_row, start_col)])
    corners = dfs(_map, start_row, start_col, visited, [(start_row, start_col)])

    x = [v[0] for v in corners]
    y = [v[1] for v in corners]

    a = shoelace(x, y)

    return math.ceil(a - (len(corners) / 2) + 1)


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
