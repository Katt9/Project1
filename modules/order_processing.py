def gen_list_of_customer_orders(customer_orders_table):
    customer_order_ids_list = []
    customer_order_objects_list = []
    for line in customer_orders_table:
        process_order_line(line, customer_order_ids_list, customer_order_objects_list)

        customer_order = [line.split()[0], line.split()[5]]
        
        if customer_order not in self.list_of_customer_orders:

            self.list_of_customer_orders.append(customer_order)

        else:

            pass
            # append the Customer_Orders_Attributes



    
"""
input: list of six elements representing one line of customer_orders_table
order_line => [113,	1045,	20,	4.00,	"Northeast",	"3A448"]
"""
def process_order_line(order_line, customer_order_ids_list, customer_order_objects_list):
    product_id = order_line[1]
    # fill in the rest for qty, price, region, order_id
    attribues = CustomerOrderAttributes(product_id, qty, price, region)
    # need function to determine existing order
    existing_order_flag = check_existing_order(order_id, customer_order_ids_list)
    if existing_order_flag:
        # add to existing order
        for customer_order_object in customer_order_objects_list:
        
            if customer_order_object.order_id == order_id:

                customer_order_object.append(attributes)
    else:
        # create new order

def check_existing_order(order_id, customer_order_ids_list):

    return True if order_id in customer_order_ids_list else False

