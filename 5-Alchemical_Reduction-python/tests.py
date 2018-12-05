from reduction import one_pass, multi_passes

def test_aa():
    assert one_pass("aa") == (0, 'aa')

def test_ab():
    assert one_pass("ab") == (0, 'ab')

def test_aA():
    assert one_pass("aA") == (1, '')

def test_Aa():
    assert one_pass("Aa") == (1, '')

def test_A():
    assert one_pass("dabAcCaCBAcCcaDA") == (2, 'dabAaCBAcaDA')

def test_B():
    assert one_pass("dabAaCBAcaDA") == (1, 'dabCBAcaDA')

def test_C():
    assert one_pass("dabCBAcaDA") == (0, 'dabCBAcaDA')

def test_multi_A():
    assert multi_passes("dabAcCaCBAcCcaDA")[1] == 'dabCBAcaDA'

