from data.input import read_customer_order_table, read_inventory_table


def main():
    customer_order_table = read_customer_order_table()  # return list of lists
    inventory_table = read_inventory_table()  # return list of lists


if __name__ == "__main__":
    main()
