from inventory import count_dupes, checksum

def test_none():
    assert count_dupes("abcdef") == (False, False)

def test_one_double():
    assert count_dupes("abbcde") == (True, False)

def test_two_doubles():
    assert count_dupes("aabcdd") == (True, False)

def test_one_triple():
    assert count_dupes("abcccd") == (False, True)

def test_two_triples():
    assert count_dupes("ababab") == (False, True)

def test_both():
    assert count_dupes("bababc") == (True, True)

def test_another_single_double():
    assert count_dupes("abcdee") == (True, False)

def test_quadruples():
    assert count_dupes("aaaabc") == (False, False)

def test_checksum():
    all = ("abcdef", "abbcde", "aabcdd", "abcccd", "ababab", "bababc", "abcdee", "aaaabc")
    assert checksum(all) == 12

