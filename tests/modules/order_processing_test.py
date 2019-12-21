from modules.order_processing import determine_order_size
import pytest

@pytest.mark.parametrize("batch_size, qty, expected_response", [
    pytest.param(50, 30, 50),
    pytest.param(50, 110, 150),
    pytest.param(100, 110, 200),
    pytest.param(100, 300, 300)
])
def test_determine_order_size(batch_size, qty, expected_response):

    assert determine_order_size(batch_size, qty) == expected_response