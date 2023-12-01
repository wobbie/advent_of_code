from Day1.day1 import find_floor, find_basement


def test_find_floor():
    assert find_floor('(())') == 0
    assert find_floor('()()') == 0


    assert find_floor('(((') == 3
    assert find_floor('(()(()(') == 3
    assert find_floor('))(((((') == 3

    assert find_floor('())') == -1
    assert find_floor('))(') == -1

    assert find_floor(')))') == -3
    assert find_floor(')())())') == -3

def test_find_basement():
    assert find_basement(')') == 1
    assert find_basement('()())') == 5
