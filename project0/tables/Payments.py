class PaymentsTable:
    def __init__(self, cursor):
        self.cursor = cursor

    def create_table(self):
        self.cursor.execute("SHOW TABLES LIKE 'Payments'")
        if not self.cursor.fetchall():
            self.cursor.execute("""
                CREATE TABLE Payments (
                    payment_txn_id VARCHAR(50) PRIMARY KEY,
                    order_id INT NOT NULL,
                    payment_type VARCHAR(20) NOT NULL,
                    payment_txn_success CHAR(1) NOT NULL,
                    failure_reason VARCHAR(100),
                    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
                );
            """)
            print("Table 'Payments' created successfully")
        else:
            print("Table 'Payments' already exists")

    def insert_payment(self, transactions):
        query = """
            INSERT INTO Payments (payment_txn_id, order_id, payment_type, payment_txn_success, failure_reason) 
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                order_id = VALUES(order_id),
                payment_type = VALUES(payment_type),
                payment_txn_success = VALUES(payment_txn_success),
                failure_reason = VALUES(failure_reason)
        """
        for transaction in transactions:
            self.cursor.execute(
                query,
                (
                    transaction['payment_txn_id'], transaction['order_id'],
                    transaction['payment_type'], transaction['payment_txn_success'],
                    transaction.get('failure_reason', None)
                )
            )
