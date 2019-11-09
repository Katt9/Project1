from orders.CustomerOrder import CustomerOrder
import pytest


def test_init():
    new_order = CustomerOrder("test_order_id", "test_customer_id")
    assert new_order.order_id == "test_order_id"
    assert new_order.customer_id == "test_customer_id"
    assert len(new_order.attributes_list) == 0
