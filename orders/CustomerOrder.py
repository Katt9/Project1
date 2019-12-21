class CustomerOrder:
    def __init__(self, order_id, customer_id):
        # initialize self.order_id, self.customer_id, and self.attributes_list
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_line = []
    
    def append(self, attributes):
        self.order_line.append(attributes)
    
    def calculate_order_total(self):
        subtotal = 0
        for attribute in self.order_line:
            subtotal += attribute.quantity * attribute.price
        return subtotal
    
    
class CustomerOrderLine:
    def __init__(self, product_id, quantity, price, region):
        # initialize self.product_id, self.quantity, self.price, self.region
        self.product_id = product_id
        self.quantity = int(quantity)
        self.price = float(price)
        self.region = region


class OrderInvoice:
    def __init__(self, customer_id, order_id, total_price=0, fulfillment_days=2):
        # initialize above, plus self.fulfillment_days
        self.customer_id = customer_id
        self.order_id = order_id
        self.total_price = total_price
        self.fulfillment_days = fulfillment_days
