import pytest
from func_calc import Calc

calc = Calc()

@pytest.mark.div
@pytest.mark.parametrize("x1, x2, result", [(25, 5, 5), (30, 6, 5)])
def test_div(x1, x2, result):
    assert calc.div(x1, x2) == result


@pytest.mark.div
def test_div_ZeroDivisionError():
    assert calc.div(25, 0) == ZeroDivisionError

@pytest.mark.add
def test_add():
    assert calc.add(77.7, 22.3) == 100

@pytest.mark.add
@pytest.mark.parametrize("x1, x2, result", [(7, 12.3, float), (24, '24', int)])
def test_type_input(x1, x2, result):
    assert isinstance(calc.add(x1, x2), result) is True
