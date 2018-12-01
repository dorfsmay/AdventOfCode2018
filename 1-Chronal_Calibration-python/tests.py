import chronalcalib

def test_add_2_positive_nums():
    assert chronalcalib.calculate([2, 3]) == 5

def test_add_positive_and_negative_nums():
    assert chronalcalib.calculate([2, -3]) == -1

def test_bunch_of_nums():
    assert chronalcalib.calculate([1, -5, 7, -9, 100]) == 94
