import pytest
from charge import calc_power, populate_grid, calc_3_3_square_max_power, highest_3_3, calc_power_n_square, calc_abs_max_power

@pytest.fixture
def grid_18():
    grid = dict()
    populate_grid(grid, 18)
    return grid

@pytest.fixture
def square_18(grid_18):
    return calc_3_3_square_max_power(grid_18)

@pytest.fixture
def grid_42():
    grid = dict()
    populate_grid(grid, 42)
    return grid

@pytest.fixture
def square_42(grid_42):
    return calc_3_3_square_max_power(grid_42)

def test_cp_01():
    assert calc_power((3,5), 8 ) == 4

def test_cp_02():
    assert calc_power((122,79), 57) == -5

def test_cp_03():
    assert calc_power((217,196), 39) == 0

def test_cp_04():
    assert calc_power((101,153), 71) == 4 

def test_grid_111(grid_18):
    assert grid_18[(33,45)] == 4

def test_grid_112(grid_18):
    assert grid_18[(34,45)] == 4

def test_grid_113(grid_18):
    assert grid_18[(35,45)] == 4

def test_grid_121(grid_18):
    assert grid_18[(33,46)] == 3

def test_grid_122(grid_18):
    assert grid_18[(34,46)] == 3

def test_grid_123(grid_18):
    assert grid_18[(35,46)] == 4

def test_grid_131(grid_18):
    assert grid_18[(33,47)] == 1

def test_grid_132(grid_18):
    assert grid_18[(34,47)] == 2

def test_grid_133(grid_18):
    assert grid_18[(35,47)] == 4

def test_grid_21(grid_42):
    assert grid_42[(21,61)] == 4

def test_grid_22(grid_42):
    assert grid_42[(22,63)] == 3

def test_square_1(square_18):
    assert square_18[0][(33,45)] == 29

def test_square_2(square_42):
    assert square_42[0][(21,61)] == 30

def test_highest_1(square_18):
    assert highest_3_3(square_18[1]) == (33, 45)

def test_highest_2(square_42):
    assert highest_3_3(square_42[1]) == (21, 61)

def test_power_n_square_1(grid_18):
    assert calc_power_n_square(grid_18, 33, 45, 3) == 29

def test_max_power_18(grid_18):
    assert calc_abs_max_power(grid_18) == (90, 269, 16)

def test_max_power_42(grid_42):
    assert calc_abs_max_power(grid_42) == (232, 251, 12)

