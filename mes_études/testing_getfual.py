from getfuel import get_fuel

def testing_get_fuel():
    assert get_fuel('1/5') == '20%'
    assert get_fuel('1/1') == 'F'
