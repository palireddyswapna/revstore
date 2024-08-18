class OrderItemsTable:
    def __init__(self, cursor):
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("SHOW TABLES LIKE 'Order_Items'")
        if not self.cursor.fetchall():
            self.cursor.execute("""
                CREATE TABLE Order_Items (
                    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
                    order_id INT NOT NULL,
                    product_id INT NOT NULL,
                    qty INT NOT NULL,
                    price DECIMAL(10, 2) NOT NULL,
                    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                    FOREIGN KEY (product_id) REFERENCES Products(product_id)
                );
            """)
            print("Table 'Order_Items' created successfully")
        else:
            print("Table 'Order_Items' already exists")

    def insert_order_items(self, transactions):
        query = """
            INSERT INTO Order_Items (order_id, product_id, qty, price)
            VALUES (%s, %s, %s, %s)
        """
        for transaction in transactions:
            self.cursor.execute(
                query,
                (
                    transaction['order_id'], transaction['product_id'],
                    transaction['qty'], transaction['price']
                )
            )
