import pytest
from src.pricing import parse_price

@pytest.mark.parametrize(
    "text,expected",
    [
        ("$1,512.37",1512.37),
        ("3,212.43",3212.43),
        ("3.12",3.12),
        ("$0.56",0.56),

    ],
)
def test_parse_price_valid(text,expected):
    assert parse_price(text)==pytest.approx(expected)
@pytest.mark.parametrize(
    "text",
    [
        "food"
        "",
        "$543,12,384"
        "$$$"

    ],
)
def test_parse_price_invalid(text):
    with pytest.raises(ValueError):
        parse_price(text)
