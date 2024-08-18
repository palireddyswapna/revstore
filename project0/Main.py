import mysql.connector
import json

from .tables.Customers import CustomersTable 
from .tables.OrdersTable import OrdersTable
from .tables.ProductsTable import ProductsTable
from .tables.OrdersTableItems import OrderItemsTable
from .tables.Payments import PaymentsTable

def Conn():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sql@2024',
        database='revature_database'
    )

def ExecuteTables():
    T1 = CustomersTable(cursor)
    T1.create_table()
    T1.insert_customers(customers)

    T2 = OrdersTable(cursor)
    T2.create_table()
    T2.insert_order(transactions)
    
    T3 = ProductsTable(cursor)
    T3.create_table()
    T3.insert_product(transactions)

    T4 = OrderItemsTable(cursor)
    T4.create_table()
    T4.insert_order_items(transactions)

    T5 = PaymentsTable(cursor)
    T5.create_table()
    T5.insert_payment(transactions)


with open('customers.json', 'r') as json_file1:
    customers = json.load(json_file1)

with open('transaction_logs.json', 'r') as json_file2:
    transactions = json.load(json_file2)

try:
    MYDB = Conn()
    cursor = MYDB.cursor()

    ExecuteTables()  # Ensure tables are created and data is inserted

    MYDB.commit()  # Ensure changes are committed

    query = input("Enter SQL query:")
    cursor.execute(query)

    # Fetch and display results
    results = cursor.fetchall()
    x = 0
    for row in results:
        if x < 10:
            print(row)  # Adjust this based on the structure of your results
        else:
            break
        x += 1

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    MYDB.close()
