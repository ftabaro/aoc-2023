def main(path: str) -> int:
    """
    Day 1 solution to part 1
    """
    numbers = []
    with open(path, encoding="utf-8") as file_handler:
        for line in file_handler:
            line = line.strip()
            n = ""

            for char in line:
                if char.isnumeric():
                    n += char
                    break

            for char in line[::-1]:
                if char.isnumeric():
                    n += char
                    break

            numbers.append(int(n))
    return sum(numbers)


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
