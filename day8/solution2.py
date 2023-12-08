import math
import re
from typing import Optional


pat = re.compile(r"(?P<name>\w{3}) = \((?P<L>\w{3}), (?P<R>\w{3})\)")


def get_node(spec: str) -> Optional[dict[str, str]]:
    match = re.match(pat, spec)

    if match is not None:
        gd = match.groupdict()
        return gd

    return None


def main(path: str) -> int:
    """
    Day 8 solution to part 2
    """

    with open(path, encoding="utf-8") as file_handler:
        directions = file_handler.readline().strip()
        nodes_spec = file_handler.read().splitlines()[1:]

    nodes = {}
    current_nodes = []
    for spec in nodes_spec:
        node = get_node(spec)
        if node is not None:
            nodes[node["name"]] = node
            if node["name"].endswith("A"):
                current_nodes.append(node)

    d = 0
    nmoves = []
    counter = 0
    while len(current_nodes) > 0:
        current_direction = directions[d]

        for i in range(len(current_nodes)):
            current_node = current_nodes[i]
            next_node_name = current_node[current_direction]
            current_nodes[i] = nodes[next_node_name]

        d = (d + 1) % len(directions)
        counter += 1

        toremove = [
            i for i, node in enumerate(current_nodes) if node["name"].endswith("Z")
        ]

        for i in toremove:
            current_nodes.pop(i)
            nmoves.append(counter)

    return math.lcm(*nmoves)


if __name__ == "__main__":
    import sys

    res = main(sys.argv[1])
    print(res)
