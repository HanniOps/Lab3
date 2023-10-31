import price_info


def test_total_cost_shopping():
    total_cost = 46.75

    result = price_info.total_cost_shopping()
    assert result == total_cost


def test_cost_of_fruits():
    fruit = 'pineapple'
    quantity = 2

    result = price_info.cost_of_fruits(fruit, quantity)
    assert result == 5.40