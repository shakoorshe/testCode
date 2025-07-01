def total_purchases(customers):
    return sum(customer[3] for customer in customers)
# returns the sum of all the money spent for each customer in the list,
# considering that the third note in the tuple is the value


def top_customers(total_value, customers):
    # Loop through each customer record in the list and include only those
    # whose total purchase amount (4th element, index 3) is greater than or
    # equal to the given total_value. Return the filtered list.
    return [customer for customer in customers if customer[3] >= total_value]

customers = [
    ("Smith", "Mary", "413-555-1234", 107.95),
    ("Johnson", "John", "413-555-5678", 250.50),
    ("Lee", "Anna", "413-555-9999", 89.40)
]

print("Total purchases:", total_purchases(customers))  # ➜ 447.85

print("Top customers:", top_customers(100, customers))
# ➜ [('Smith', 'Mary', '413-555-1234', 107.95), ('Johnson', 'John', '413-555-5678', 250.50)]
