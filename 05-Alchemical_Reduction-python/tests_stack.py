from reduction_stack import one_pass, multi_passes

def test_aa():
    assert one_pass("aa") == 'aa'

def test_ab():
    assert one_pass("ab") == 'ab'

def test_aA():
    assert one_pass("aA") == ''

def test_Aa():
    assert one_pass("Aa") == ''

#def test_A():
#    assert one_pass("dabAcCaCBAcCcaDA") == 'dabAaCBAcaDA'

#def test_B():
#    assert one_pass("dabAaCBAcaDA") == 'dabCBAcaDA'

#def test_C():
#    assert one_pass("dabCBAcaDA") == 'dabCBAcaDA'

def test_multi_A():
    assert multi_passes("dabAcCaCBAcCcaDA") == 'dabCBAcaDA'

