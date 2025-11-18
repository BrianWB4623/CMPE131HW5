import pytest
from src.pricing import apply_discount

@pytest.mark.parametrize(
    "price,percent,expected",
    [
        (12.35,10,11.12),
        (10.00,100,0),
        (12.43,50.33,6.17),
    ],
)
def test_apply_discount_valid(price,percent,expected):
    assert apply_discount(price,percent)==pytest.approx(expected)

@pytest.mark.parametrize(
    "price,percent",
    [
        (12.35,-10),
    ],
)
def test_apply_discount_invalid(price,percent):
    with pytest.raises(ValueError):
        apply_discount(price,percent)