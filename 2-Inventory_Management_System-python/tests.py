from inventory import count_dupes, checksum, find_boxes, matching_ids

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

# The boxes will have IDs which differ by exactly one character at the same position in both strings.
def test_matching_same():
    assert matching_ids('fghij', 'fghij') ==  None

def test_matching_middle():
    assert matching_ids('fghij', 'fguij') ==  'fgij'

def test_matching_begining():
    assert matching_ids('xghij', 'fghij') ==  'ghij'

def test_matching_end():
    assert matching_ids('fghir', 'fghij') ==  'fghi'

def test_matching_good_2():
    assert matching_ids('fghij', 'ughij') ==  'ghij'

def test_box_2_ids():
    assert find_boxes(['fghij', 'fguij']) == set(('fgij',))

def test_negative_2_ids():
    assert find_boxes(['fghij', 'fgiuj']) == set()

def test_many_ids():
    all = ('fghij', 'abcde', 'acbde', 'fguij', 'aaecdb', 'abdde')
    assert find_boxes(all) == set(('fgij', 'abde'))

