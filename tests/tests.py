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


# DAY 4

from day4.solution1 import main as d4s1
from day4.solution2 import main as d4s2


def test_day4_sol1():
    solution = d4s1(test_files["day4"])
    assert solution == 13


def test_day4_sol2():
    solution = d4s2(test_files["day4"])
    assert solution == 30


# DAY 5

from day5.solution1 import main as d5s1
from day5.solution2 import main as d5s2


def test_day5_sol1():
    solution = d5s1(test_files["day5"])
    assert solution == 35


def test_day5_sol2():
    solution = d5s2(test_files["day5"])
    assert solution == 46


# DAY 6

from day6.solution1 import main as d6s1
from day6.solution2 import main as d6s2


def test_day6_sol1():
    solution = d6s1(test_files["day6p1"])
    assert solution == 288


def test_day6_sol2():
    solution = d6s2(test_files["day6p2"])
    assert solution == 71503


# DAY 7

from day7.solution1 import main as d7s1
from day7.solution2 import main as d7s2


def test_day7_sol1():
    solution = d7s1(test_files["day7"])
    assert solution == 6440


def test_day7_sol2():
    solution = d7s2(test_files["day7"])
    assert solution == 5905


# DAY 8

from day8.solution1 import main as d8s1
from day8.solution2 import main as d8s2


def test_day8_sol1a():
    solution = d8s1(test_files["day8p1a"])
    assert solution == 2


def test_day8_sol1b():
    solution = d8s1(test_files["day8p1b"])
    assert solution == 6


def test_day8_sol2():
    solution = d8s2(test_files["day8p2"])
    assert solution == 6


# DAY 9

from day9.solution1 import main as d9s1
from day9.solution2 import main as d9s2


def test_day9_sol1():
    solution = d9s1(test_files["day9"])
    assert solution == 114


def test_day9_sol2():
    solution = d9s2(test_files["day9"])
    assert solution == 2


# DAY 10

from day10.solution1 import main as d10s1
from day10.solution2 import main as d10s2


def test_day10_sol1a():
    solution = d10s1(test_files["day10p1a"])
    assert solution == 4


def test_day10_sol1b():
    solution = d10s1(test_files["day10p1b"])
    assert solution == 8


def test_day10_sol1c():
    solution = d10s1(test_files["day10p1c"])
    assert solution == 4


def test_day10_sol1d():
    solution = d10s1(test_files["day10p1d"])
    assert solution == 8


def test_day10_sol2a():
    solution = d10s2(test_files["day10p2a"])
    assert solution == 4


def test_day10_sol2b():
    solution = d10s2(test_files["day10p2b"])
    assert solution == 8


def test_day10_sol2c():
    solution = d10s2(test_files["day10p2c"])
    assert solution == 10


def test_day10_sol2d():
    solution = d10s2(test_files["day10p2d"])
    assert solution == 4


# DAY 11

from day11.solution1 import main as d11s1
from day11.solution2 import main as d11s2


def test_day11_sol1():
    solution = d11s1(test_files["day11"])
    assert solution == 374


def test_day11_sol2c():
    solution = d11s2(test_files["day11"], 1)
    assert solution == 374


def test_day11_sol2a():
    solution = d11s2(test_files["day11"], 10)
    assert solution == 1030


def test_day11_sol2b():
    solution = d11s2(test_files["day11"], 100)
    assert solution == 8410
