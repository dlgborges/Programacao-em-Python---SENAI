from my_functions import somar

def test_somar():
    assert somar(2, 3) == 5
    assert somar(5, 7) == 12
    assert somar(10, -3) == 7
