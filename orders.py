orders = {}

def add_order(name, value):
    if name in orders:
        orders[name].append(value)
    else:
        orders[name] = [value]

def remove_order(name, value):
    if name in orders:
        orders[name].remove(value)

def remove_latest(name):
    if name in orders:
        orders[name].pop()
    else:
        print(f"{name} not in orders")

def remove_oldest(name):
    if name in orders:
        for i in range(0, len(orders[name])-2):
            orders[name][i] = orders[name][i+1]
        orders[name].pop()
    else:
        print(f"{name} not in orders")

def print_orders():
    for name, values in orders.items():
        print(f"{name}", end = " ")
        for order in values:
            print(f"{order}", end = " ")
    print()


add_order("Bread", 2)
add_order("Bread", 22)
add_order("Bread", 23)
add_order("Bread", 25)
print_orders()
remove_oldest("Bread")
print_orders()


