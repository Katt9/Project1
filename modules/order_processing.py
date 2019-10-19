from orders.CustomerOrder import CustomerOrder, CustomerOrderAttributes


def process_customer_order(order):
    # order => [113,	1045,	20,	4.00,	"Northeast",	"3A448"]
    product_id = order[1]
    qty = order[2]
    price = order[3]
    region = order[4]
    # fill in the rest for qty, price, region, order_id
    attributes = CustomerOrderAttributes(product_id, qty, price, region)
    # return customer orders attributes objects
    return attributes


def check_existing_order(order_id, customer_orders_list):
    index = 0
    for customer_order in customer_orders_list:
        if customer_order.order_id == order_id:
            return index
        index += 1
    return -1


def gen_list_of_customer_orders(customer_orders_table):
    customer_orders_list = []
    for line in customer_orders_table:
        # line => [113,	1045,	20,	4.00,	"Northeast",	"3A448"]
        customer_order_id = line[0]  # customer order ID
        customer_id = line[5]  # customer ID
        order_index = check_existing_order(customer_order_id, customer_orders_list)
        if order_index == -1:
            # create new customer order
            customer_order = CustomerOrder(customer_order_id, customer_id)
            customer_orders_list.append(customer_order)
            customer_order.append(process_customer_order(line))
