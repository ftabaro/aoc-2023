import re


def main(path: str) -> int:
    """
    Day 2 solution to part 1
    """

    games = []

    ncubes = {"red": 12, "green": 13, "blue": 14}

    with open(path, encoding="utf-8") as file_handler:
        for i, line in enumerate(file_handler):
            line = line.strip()
            game_id, game_record = line.split(": ")

            valid_game = True
            for sampling in game_record.split("; "):
                for s in sampling.split(", "):
                    sampled_cubes, cubes_color = s.split(" ")
                    if int(sampled_cubes) > ncubes[cubes_color]:
                        valid_game = False
                        break
            # if not valid_game:
            #     break

            if valid_game:
                games.append(i + 1)

    return sum(games)


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
