def main(path: str) -> int:
    """
    Day 1 solution to part 2
    """

    lookup = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }

    numbers = []
    with open(path, encoding="utf-8") as file_handler:
        for line in file_handler:
            line = line.strip()

            numbers_in_line = []

            for i in range(len(line)):
                if line[i].isnumeric():
                    numbers_in_line.append(line[i])
                    continue
                for j in [2, 3, 4, 5]:
                    w = line[i : i + j]
                    if w in lookup:
                        numbers_in_line.append(str(lookup[w]))
                        break
            numbers.append(int(numbers_in_line[0] + numbers_in_line[-1]))

    return sum(numbers)


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
