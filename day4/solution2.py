import re


def main(path: str) -> int:
    """
    Day 4 solution to part 1
    """
    pat = re.compile(
        r"^Card\s+(?P<card_id>\d+):(?P<winning_numbers>[\d\s]+)\|(?P<card_numbers>[\s\d]+)$"
    )

    card_copies = {}
    with open(path, encoding="utf-8") as file_handler:
        for line in file_handler:
            line = line.strip()

            match = re.match(pat, line)
            if match is not None:
                m = match.groupdict()

                card_id = int(m["card_id"])
                winning_numbers = [
                    int(x) for x in re.findall(r"\d+", m["winning_numbers"])
                ]
                my_numbers = [int(x) for x in re.findall(r"\d+", m["card_numbers"])]

                if card_id not in card_copies:
                    card_copies[card_id] = copies = 1
                else:
                    card_copies[card_id] += 1
                    copies = card_copies[card_id]

                for i in range(copies, 0, -1):
                    next_card = card_id + 1
                    for n in my_numbers:
                        if n in winning_numbers:
                            if not next_card in card_copies:
                                card_copies[next_card] = 0
                            card_copies[next_card] += 1
                            next_card = next_card + 1

    tot = sum(list(card_copies.values()))
    return tot


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
