# Task 1

def unpack_orders():
    for order in orders:
        customer_name, product_ordered, quantity_ordered = order
        print(f"\nCustomer Name: {customer_name} \nProduct Ordered: {product_ordered}\nQuantity Ordered: {quantity_ordered}")

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2)
]

unpack_orders()