from vanity_plate import is_valid


def test_vanity_plate():
    assert is_valid('ab555')
    assert is_valid('0bb6b')
    assert is_valid('bbbb6')


def test_vanity_plate2():
    assert is_valid('bbbb6')
