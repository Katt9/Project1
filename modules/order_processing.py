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
    #1. Create ProductList object
    #2. Iterate through inventory_table. For each item:
        #2.1. Create Product object
        #2.2. Add Product object to list
    #3. Return list
    pass


def process_inventory(customer_orders_list, product_list):
    #1. create list of invoices, list of resupply orders
    #2. Iterate through customer_orders_list. For each order object:
        #2.1 create invoice object, calculate price
        #2.2. Iterate through each line in the attributes_list. For each item:
            #2.2.1. find correct product in product_list
            #2.2.2. check inventory of product
                #2.2.2.1. if True, place_order
                #2.2.2.2. else create or update resupply order object, update days to fulfillment
    #3. return resupply orders list, invoice list
    pass

#
#