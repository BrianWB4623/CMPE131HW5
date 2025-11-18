import pytest
from src.pricing import format_currency

@pytest.mark.parametrize(
    "value,expected",
    [
        (1512.27,"$1512.27"),
        (23.56789,"$23.57"),
        (1.284,"$1.28"),
        (3,"$3.00"),
     ],
)
def test_format_currency(value,expected):
    assert format_currency(value)==expected
