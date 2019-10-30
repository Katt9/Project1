from collections import defaultdict


class Product:
    def __init__(self, product_id, quantity, region, shipping_time, batch_size):
        # initialize above variables
        self.product_id = product_id
        self.quantity = quantity
        self.region = region
        self.shipping_time = shipping_time
        self.batch_size = batch_size

    def check_inventory(self, amount):
        # check if self.quantity >= amount, return True or False
        if self.quantity >= amount:
            return True
        return False

    def place_order(self, amount):
        # reduce self.quantity by amount
        self.quantity -= amount


class ProductList:
    def __init__(self):
        self.product_list = defaultdict(dict)

    def append(self, product):
        product_id = product.product_id
        region = product.region
        self.product_list[product_id][region] = product

    def get_product(self, product_id, region):
        return self.product_list[product_id][region]