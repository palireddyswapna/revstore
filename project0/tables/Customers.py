class CustomersTable:
    def __init__(self, cursor):
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("SHOW TABLES LIKE 'Customers'")
        if not self.cursor.fetchall():
            self.cursor.execute("""
                CREATE TABLE Customers (
                    customer_id INT PRIMARY KEY,
                    customer_name VARCHAR(100) NOT NULL,
                    country VARCHAR(100) NOT NULL,
                    city VARCHAR(50) NOT NULL
                );
            """)
            print("Table 'Customers' created successfully")
        else:
            print("Table 'Customers' already exists")

    def insert_customers(self, customers):
        for customer in customers:
            self.cursor.execute("""
                INSERT INTO Customers (customer_id, customer_name, country, city)
                VALUES (%s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    customer_name = VALUES(customer_name),
                    country = VALUES(country),
                    city = VALUES(city)
            """, (
                customer['customer_id'], customer['customer_name'],
                customer['country'], customer['city']
            )
        )
