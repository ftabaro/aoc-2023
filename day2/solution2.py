import math


def main(path: str) -> int:
    """
    Day 2 solution to part 1
    """

    games = []

    tot = 0

    with open(path, encoding="utf-8") as file_handler:
        for i, line in enumerate(file_handler):
            line = line.strip()
            game_id, game_record = line.split(": ")

            ncubes = {"red": -math.inf, "green": -math.inf, "blue": -math.inf}

            for sampling in game_record.split("; "):
                for s in sampling.split(", "):
                    sampled_cubes, cubes_color = s.split(" ")
                    sampled_cubes = int(sampled_cubes)
                    if sampled_cubes > ncubes[cubes_color]:
                        ncubes[cubes_color] = sampled_cubes

            game_power = 1
            for n in ncubes.values():
                game_power *= n

            tot += game_power

    return tot


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
