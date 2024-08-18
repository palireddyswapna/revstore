import json

# Load JSON data
with open('customers.json', 'r') as file:
    customer_data = json.load(file)

with open('transaction_logs.json', 'r') as file:
    transaction_data = json.load(file)

# Save data to Python files
with open('customers_data.py', 'w') as file:
    file.write(f"customer_data = {json.dumps(customer_data, indent=4)}\n")

with open('transaction_data.py', 'w') as file:
    file.write(f"transaction_data = {json.dumps(transaction_data, indent=4)}\n")
