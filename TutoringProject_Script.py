class Process_Customer_Order():

    def __init__(self):

        self.list_of_customer_orders = []

        self.attributes_list = []

        self.customer_orders_table = read_customer_orders_table()
        
        self.customer_orders_table_file.close()

    def read_customer_orders_table(self):

        return open("C:\\Users\\kylie\\Documents\\Customer Orders Table.txt", "r")

    def gen_list_of_customer_orders(self):

        for line in self.customer_orders_table:

            customer_order = [line.split()[0], line.split()[5]]
            
            if customer_order not in self.list_of_customer_orders:

                self.list_of_customer_orders.append(customer_order)

            else:

                pass
            
class Customer_Order_Attributes():

    def __init__(self, product_id, qty, price_per_order, region):

        self.product_id = product_id

        self.qty = qty

        self.price_per_order = price_per_order

        self.region = region
