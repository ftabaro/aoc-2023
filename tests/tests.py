import pathlib
import sys


root = pathlib.Path(sys.path[0]).parents[0]
sys.path.append(str(root))

fp = pathlib.Path(__file__).resolve()
testdata = fp.parents[0].joinpath("testdata")
test_files = testdata.glob("*.txt")
test_files = [p.absolute() for p in test_files]
test_files = {p.name.replace(".txt", ""): str(p) for p in test_files}

# DAY 1

from day1.solution1 import main as d1s1
from day1.solution2 import main as d1s2


def test_day1_sol1():
    solution = d1s1(test_files["day1p1"])
    assert solution == 142

def test_day1_sol2():
    solution = d1s2(test_files["day1p2"])
    assert solution == 281