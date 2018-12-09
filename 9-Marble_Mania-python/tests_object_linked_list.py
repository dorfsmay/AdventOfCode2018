from mania_object_linked_list import high_score


def test_full_1():
    assert high_score(9, 25) == 32

def test_full_2():
    assert high_score(10, 1618) == 8317

def test_full_3():
    assert high_score(13, 7999) == 146373

def test_full_4():
    assert high_score(17, 1104) == 2764

def test_full_5():
    assert high_score(21, 6111) == 54718

def test_full_6():
    assert high_score(30, 5807) == 37305


