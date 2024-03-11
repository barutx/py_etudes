from numb3rs import validate

def test_validate():
    assert validate("122.34.54.76")
    assert validate("1.1.1.1")
    assert validate("0.0.0.0")
    assert validate("99.99.99.999")