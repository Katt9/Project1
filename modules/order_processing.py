from orders.CustomerOrder import CustomerOrder, CustomerOrderLine, OrderInvoice
from inventory.Product import ProductList, Product


def process_customer_order(order):
    # order => [113,	1045,	20,	4.00,	"Northeast",	"3A448"]
    product_id = order[1]
    qty = order[2]
    price = order[3]
    region = order[4]
    # fill in the rest for qty, price, region, order_id
    attributes = CustomerOrderLine(product_id, qty, price, region)
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
    # iterate through list of customer orders to create CustomerOrder objects
    for line in customer_orders_table:
        # line => [113,	1045,	20,	4.00,	"Northeast",	"3A448"]
        customer_order_id = line[0]  # customer order ID
        customer_id = line[5]  # customer ID

        # check if order ID already exists
        order_index = check_existing_order(customer_order_id, customer_orders_list)
        if order_index == -1:  # order does not currently exist
            # create new customer order
            customer_order = CustomerOrder(customer_order_id, customer_id)
            customer_orders_list.append(customer_order)
            customer_order.append(process_customer_order(line))

        # # add to existing order
        # for customer_order_object in customer_orders_list:
        #
        #     if customer_order_object.order_id == customer_order.order_id:
        #         customer_order_object.append(attributes)

        else:
            add_to_existing_order(line, customer_orders_list)
        # create new order
    return customer_orders_list

def add_to_existing_order(line, customer_orders_list):

    order_id = line[0]

    for customer_order_object in customer_orders_list:

        if customer_order_object.order_id == order_id:
            customer_order_object.append(process_customer_order(line))

def gen_product_list(inventory_table):

    product_list = ProductList()
    # line -> [1045, 50 ,Northeast, 5, 100]

    for line in inventory_table:
        product_list.append(create_product(line))
    return product_list

def create_product(line):

    product_id = line[0]
    quantity = line[1]
    region = line[2]
    shipping_time = line[3]
    batch_size = line[4]
    product = Product(product_id, quantity, region, shipping_time, batch_size)

    return product


def process_inventory(customer_orders_list, product_list):

    #1. create list of invoices, list of resupply orders
    invoices_list = []
    #2. Iterate through customer_orders_list. For each order object:
    for customer_order in customer_orders_list:
        order_total = customer_order.calculate_order_total()
        invoice = OrderInvoice(customer_order.customer_id, customer_order.order_id, order_total)
        for order_line in customer_order.order_line:
            correct_product = product_list.get_product(order_line.product_id, order_line.region)
            is_sufficient = correct_product.check_inventory(order_line.quantity)
            if is_sufficient:
                correct_product.place_order(order_line.quantity)
            else:
                pass

    return

        #2.1 create invoice object, calculate price
        #2.2. Iterate through each line in the attributes_list. For each item:
            #2.2.1. find correct product in product_list
            #2.2.2. check inventory of product
                #2.2.2.1. if True, place_order
                #2.2.2.2. else create or update resupply order object, update days to fulfillment
    #3. return resupply orders list, invoice list

def get_correct_product():

    pass
#
#