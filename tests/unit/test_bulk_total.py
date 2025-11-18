import pytest
from src.pricing import bulk_total

@pytest.mark.parametrize(
    "price,discount_percent,tax_rate,expected",
    [
        ([1.25,1.00,2.45],25,0.05,3.70125),
        ([1.25,1.00,2.45],None,0.05,4.935),
        ([1.25,1.00,2.45],25,None,3.77175),
        ([1.25,1.00,2.45],None,None,5.029),
        ([],25.0,0.05,0),
    ],
)
def test_bulk_total(price,discount_percent,tax_rate,expected):
    if discount_percent is None and tax_rate is not None:
        result = bulk_total(price,tax_rate=tax_rate)
    elif tax_rate is None and discount_percent is not None :
        result=bulk_total(price,discount_percent=discount_percent)
    elif tax_rate is None and discount_percent is None:
        result=bulk_total(price)
    else:
        result=bulk_total(price,discount_percent,tax_rate)
    assert result==pytest.approx(expected)
