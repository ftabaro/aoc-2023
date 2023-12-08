import re

pat = re.compile(r"(?P<name>[A-Z]{3}) = \((?P<left>[A-Z]{3}), (?P<right>[A-Z]{3})\)")


class Node:
    def __init__(self, spec: str) -> None:
        match = re.match(pat, spec)
        if match is not None:
            gd = match.groupdict()
            self.name = gd["name"]
            self.left = gd["left"]
            self.right = gd["right"]

    def __repr__(self) -> str:
        return f"Node<name={self.name}; left={self.left}; right={self.right}>"


def main(path: str) -> int:
    """
    Day 8 solution to part 1
    """

    with open(path, encoding="utf-8") as file_handler:
        directions = file_handler.readline().strip()
        nodes_spec = file_handler.read().splitlines()[1:]

    nodes = {}
    for spec in nodes_spec:
        node = Node(spec)
        nodes[node.name] = node

    current_node = nodes["AAA"]
    d = 0
    nmoves = 0
    while current_node.name != "ZZZ":
        current_direction = directions[d]
        if current_direction == "L":
            next_node_name = current_node.left
        else:
            next_node_name = current_node.right

        current_node = nodes[next_node_name]
        d = (d + 1) % len(directions)
        nmoves += 1

    return nmoves


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
