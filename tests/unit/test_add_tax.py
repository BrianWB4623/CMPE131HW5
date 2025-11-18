import pytest
from src.pricing import add_tax

@pytest.mark.parametrize(
    "price,rate,expected",
    [
        (12.35,0.07,13.2145),
        (12.35,None,13.2145),
        (10.2,0.05,10.71),
    ],
)
def test_add_tax_valid(price,rate,expected):
    if rate is None:
        result=add_tax(price)
    else:
        result=add_tax(price,rate)
    assert result==pytest.approx(expected)
@pytest.mark.parametrize(
    "price,rate",
    [
        (12.35,-0.07),
    ],
)
def test_add_tax_invalid(price,rate):
    with pytest.raises(ValueError):
        add_tax(price,rate)



    