class OrdersTable:
    def __init__(self, cursor):
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("SHOW TABLES LIKE 'Orders'")
        if not self.cursor.fetchall():
            self.cursor.execute("""
                CREATE TABLE Orders (
                    order_id INT PRIMARY KEY,
                    customer_id INT NOT NULL,
                    datetime DATETIME NOT NULL,
                    ecommerce_website_name VARCHAR(100) NOT NULL,
                    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                );
            """)
            print("Table 'Orders' created successfully")
        else:
            print("Table 'Orders' already exists")

    def insert_order(self, transactions):
        query = """
            INSERT INTO Orders (order_id, customer_id, datetime, ecommerce_website_name) 
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                customer_id = VALUES(customer_id),
                datetime = VALUES(datetime),
                ecommerce_website_name = VALUES(ecommerce_website_name)
        """
        for transaction in transactions:
            self.cursor.execute(
                query,
                (
                    transaction['order_id'], transaction['customer_id'], 
                    transaction['datetime'], transaction['ecommerce_website_name']
                )
            )
