import pytest

from inventory.Product import Product, InsufficientInventoryException, ProductList


def test_init():
    new_product = Product("1", "2", "South", "5 AM", "6")
    assert new_product.product_id == "1"
    assert new_product.quantity == "2"
    assert new_product.region == "South"
    assert new_product.shipping_time == "5 AM"
    assert new_product.batch_size == "6"


class MockProduct:
    def __init__(self, product_id, region):
        self.product_id = product_id
        self.region = region

@pytest.mark.parametrize("amount, expected_response", [
    pytest.param(5, False),
    pytest.param(1, True),
    pytest.param(2, True)
])
def test_check_inventory(amount, expected_response):
    new_product = Product("1", 2, "South", "5 AM", "6")
    assert new_product.check_inventory(amount) is expected_response


@pytest.mark.parametrize("amount, expected_response", [
    pytest.param(5, 5),
    pytest.param(8, 2),
    pytest.param(7, 3)
])
def test_place_order(amount, expected_response):
    new_product = Product("1", 10, "South", "5 AM", "6")
    new_product.place_order(amount)
    assert new_product.quantity == expected_response

def test_place_order_exception():
    new_product = Product("1", 10, "South", "5 AM", "6")
    #new_product.place_order(15)
    with pytest.raises(InsufficientInventoryException) as ex:
        new_product.place_order(15)

    assert "Not enough inventory to place order" == str(ex.value)

def test_product_list_init():
    new_product_list = ProductList()
    assert len(new_product_list.product_list) == 0

def test_append():
    # Review this test/assertions to make sure it makes sense
    new_product_list = ProductList()
    new_mock_product = MockProduct("prod1", "North")
    new_product_list.append(new_mock_product)
    # new_product_list.append(MockProduct("prod1", "South"))

    assert "prod1" in new_product_list.product_list.keys()
    assert "North" in new_product_list.product_list['prod1'].keys()

    added_product = new_product_list.product_list['prod1']['North']

    assert added_product.product_id == "prod1"

def test_get_product():
    new_product_list = ProductList()
    new_mock_product = MockProduct("prod1", "North")
    new_product_list.append(new_mock_product)

    var1 = new_product_list.get_product(new_mock_product.product_id, new_mock_product.region)

    # assert 1 == 1

    assert "prod1" == var1.product_id
    assert "North" == var1.region
