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


def get_start(_map: str) -> tuple[int, int]:
    start = _map.index("S")
    newlines = _map[:start].count("\n")
    start -= newlines

    _map = _map.splitlines()
    ncols = len(_map[0])

    (r, c) = divmod(start, ncols)

    return _map, r, c


def main(path: str) -> int:
    """
    Day 10 solution to part 1
    """

    _map = open(path, encoding="utf-8").read()
    _map, start_row, start_col = get_start(_map)

    visited = set()
    neighbors, visited = get_neighbors(_map, start_row, start_col, 0, visited)
    farthest = 0
    while neighbors:
        r, c, d = neighbors.pop()
        if d > farthest:
            farthest = d
        new_neighbors, visited = get_neighbors(_map, r, c, d, visited)
        neighbors |= new_neighbors

    return farthest


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
