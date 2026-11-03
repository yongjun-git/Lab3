import price_info
import pytest

def test_cost_of_fruits_apple():
    result = price_info.cost_of_fruits('apple', 10)
    assert result == pytest.approx(12.0)       # 1.20 × 10

def test_cost_of_fruits_pear():
    result = price_info.cost_of_fruits('pear', 10)
    assert result == pytest.approx(9.0)        # 0.90 × 10

def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    assert result == pytest.approx(46.75)      # whole shopping list