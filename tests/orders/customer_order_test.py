from orders.CustomerOrder import CustomerOrder
import pytest


class MockCustomerOrderAttributes:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price


def test_init():
    new_order = CustomerOrder("test_order_id", "test_customer_id")
    assert new_order.order_id == "test_order_id"
    assert new_order.customer_id == "test_customer_id"
    assert len(new_order.order_line) == 0


def test_append():
    new_order = CustomerOrder("test_order_id", "test_customer_id")
    new_order.append("test attributes")

    assert len(new_order.order_line) == 1
    assert new_order.order_line[0] == "test attributes"


def test_calculate_order_total():
    new_order = CustomerOrder("test_order_id", "test_customer_id")
    new_customer_attr1 = MockCustomerOrderAttributes(1, 5)
    new_customer_attr2 = MockCustomerOrderAttributes(2, 10)
    new_customer_attr3 = MockCustomerOrderAttributes(3, 15)
    expected_total = 70
    new_order.append(new_customer_attr1)
    new_order.append(new_customer_attr2)
    new_order.append(new_customer_attr3)
    total = new_order.calculate_order_total()
    assert total == expected_total
