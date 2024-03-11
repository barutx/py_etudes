from greetings_bank import greetings

def test_greetings():
    assert greetings('hello') == '$0'
    assert greetings('hey') == '$20'
    assert greetings('fine') == '$100'