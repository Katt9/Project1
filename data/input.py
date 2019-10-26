def read_customer_order_table(filename='db/customer_order_table.csv'):
    return read_table(filename)
    

def read_inventory_table(filename='db/inventory_table.csv'):
    return read_table(filename)


def read_table(filename):
    table_file = open(filename, 'r', encoding='utf-8-sig')
    lines = table_file.readlines()
    return [line.rstrip().split(',') for line in lines]
