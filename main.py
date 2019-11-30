from data.input import read_customer_order_table, read_inventory_table
from modules.order_processing import gen_list_of_customer_orders, gen_product_list, process_inventory


def read_input_tables():
    customer_order_table = read_customer_order_table()  # return list of lists
    inventory_table = read_inventory_table()  # return list of lists
    return customer_order_table, inventory_table


def main():
    customer_order_table, inventory_table = read_input_tables()
    customer_orders = gen_list_of_customer_orders(customer_order_table)
    product_list = gen_product_list(inventory_table)
    dummy = 'blah'
    inventory = process_inventory(customer_orders, product_list)

if __name__ == "__main__":
    main()
