from orders.CustomerOrder import CustomerOrder, CustomerOrderAttributes

# def gen_list_of_customer_orders(customer_orders_table):
#     customer_order_ids_list = []
#     customer_order_objects_list = []
#     for line in customer_orders_table:
#         process_order_line(line, customer_order_ids_list, customer_order_objects_list)
#
#         customer_order = [line.split()[0], line.split()[5]]
#
#         if customer_order not in self.list_of_customer_orders:
#
#             self.list_of_customer_orders.append(customer_order)
#
#         else:
#
#             pass
#             # append the Customer_Orders_Attributes
#
#
#
#
# """
# input: list of six elements representing one line of customer_orders_table
# order_line => [113,	1045,	20,	4.00,	"Northeast",	"3A448"]
# """
# process_customer_order = line in customer_orders_table
def process_customer_order(order):
    #order => [113,	1045,	20,	4.00,	"Northeast",	"3A448"]
    product_id = order_line[1]
    # qty =
    # fill in the rest for qty, price, region, order_id
    attributes = CustomerOrderAttributes(product_id, qty, price, region)
    # return customer orders attributes objects

def check_existing_order(order_id, customer_orders_list):
    index = 0
    for customer_order in customer_orders_list:
        if order_id in customer_order.order_id:
            return index
        index += 1

    return -1

def gen_list_of_customer_orders(customer_orders_table):

    customer_orders_list = []
    for line in customer_orders_table:
        # line => [113,	1045,	20,	4.00,	"Northeast",	"3A448"]
        customer_order_id = line[0] # customer order ID
        customer_id = line[5] # customer ID
        order_index = check_existing_order(customer_order_id, customer_orders_list)
        if order_index == -1:
            # create new customer order
            customer_order = CustomerOrder(customer_order_id, customer_id)
            customer_orders_list.append(customer_order)
            process_customer_order(line)


        # add to existing order
        for customer_order_object in customer_order_objects_list:

            if customer_order_object.order_id == order_id:
                customer_order_object.append(attributes)

        else:
        # create new order
