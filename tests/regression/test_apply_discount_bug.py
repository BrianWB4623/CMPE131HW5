from src.pricing import apply_discount

def test_apply_discount_regression():
    result=apply_discount(20.0,10)
    assert result==18.0