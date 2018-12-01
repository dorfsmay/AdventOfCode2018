import chronalcalib

def test_add_2_positive_nums():
    assert chronalcalib.calculate_resulting_freq([2, 3]) == 5

def test_add_positive_and_negative_nums():
    assert chronalcalib.calculate_resulting_freq([2, -3]) == -1

def test_add_bunch_of_nums():
    assert chronalcalib.calculate_resulting_freq([1, -5, 7, -9, 100]) == 94

def test_dup_freq_simple():
    assert chronalcalib.frist_duplicate_freq([10, -4, 100, -50, -50])[0] == 6

def test_dup_freq_need_to_run_twice():
    assert chronalcalib.frist_duplicate_freq([3, 3, 4, -2, -4])[0] == 10
