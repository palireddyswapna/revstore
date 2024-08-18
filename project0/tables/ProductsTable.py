class ProductsTable:
    def __init__(self, cursor):
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("SHOW TABLES LIKE 'Products'")
        if not self.cursor.fetchall():
            self.cursor.execute("""
                CREATE TABLE Products (
                    product_id INT PRIMARY KEY,
                    product_name VARCHAR(100) NOT NULL,
                    product_category VARCHAR(50) NOT NULL,
                    price DECIMAL(10, 2) NOT NULL
                );
            """)
            print("Table 'Products' created successfully")
        else:
            print("Table 'Products' already exists")

    def insert_product(self, transactions):
        query = """
            INSERT INTO Products (product_id, product_name, product_category, price)
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                product_name = VALUES(product_name),
                product_category = VALUES(product_category),
                price = VALUES(price)
        """
        for transaction in transactions:
            self.cursor.execute(
                query,
                (
                    transaction['product_id'], transaction['product_name'],
                    transaction['product_category'], transaction['price']
                )
            )
