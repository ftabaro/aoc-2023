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


# DAY 2

from day2.solution1 import main as d2s1
from day2.solution2 import main as d2s2


def test_day2_sol1():
    solution = d2s1(test_files["day2"])
    assert solution == 8


def test_day2_sol2():
    solution = d2s2(test_files["day2"])
    assert solution == 2286


# DAY 3

from day3.solution1 import main as d3s1
from day3.solution2 import main as d3s2


def test_day3_sol1():
    solution = d3s1(test_files["day3"])
    assert solution == 4361

def test_day3_sol2():
    solution = d3s2(test_files["day3"])
    assert solution == 467835
