import re

def main(path: str) -> int:
    """
    Day 4 solution to part 1
    """
    pat = re.compile(r"^Card\s+[0-9]+:(?P<winning_numbers>[\d\s]+)\|(?P<card_numbers>[\s\d]+)$")
    tot = 0
    with open(path, encoding="utf-8") as file_handler:
        for line in file_handler:
            line = line.strip()

            match = re.match(pat, line)
            if match is not None:
                m = match.groupdict()
                
                winning_numbers = [ int(x) for x in re.findall(r"\d+", m["winning_numbers"]) ]
                my_numbers = [ int(x) for x in re.findall(r"\d+", m["card_numbers"]) ]

                card_score = 0
                for n in my_numbers:
                    if n in winning_numbers:
                        if card_score == 0:
                            card_score = 1
                        else:
                            card_score *= 2
                tot += card_score

    return tot


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
