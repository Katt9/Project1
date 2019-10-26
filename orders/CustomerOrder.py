class CustomerOrder:
    def __init__(self, order_id, customer_id):
        # initialize self.order_id, self.customer_id, and self.attributes_list
        self.order_id = order_id
        self.customer_id = customer_id
        self.attributes_list = []
    
    def append(self, attributes):
        self.attributes_list.append(attributes)
    
    def calculate_order_total(self):
        subtotal = 0
        for attribute in self.attributes_list:
            subtotal += attribute.quantity * attribute.price
        return subtotal
    
    
class CustomerOrderAttributes:
    def __init__(self, product_id, quantity, price, region):
        # initialize self.product_id, self.quantity, self.price, self.region
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.region = region


class OrderInvoice:
    def __init__(self, customer_id, order_id, total_price=0, fulfillment_days=2):
        # initialize above, plus self.fulfillment_days
        pass

    def calculate_price(self, order_attributes):
        # sum total of items in order_attributes
        pass
