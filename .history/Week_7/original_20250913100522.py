import sqlite3
import sys
from design_pattern import DatabaseConnection 

class UserService:
    def get_user(self, user_id):
        nano = sys.current_time_ns()
        conn = sqlite3.connect('app.db')  # New connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        period = sys.current_time_ns()-nano
        print(f"Time taken to fetch user: {period} nanoseconds")
        conn.close()
        return result
 
class OrderService:
    def get_orders(self, user_id):

        conn = sqlite3.connect('app.db')  # Another new connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        conn.close()
        return result
    



class DatabaseCreator:
    def createDbTable(self):
        conn = DatabaseConnection().get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                product_name TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        for i in  range(1,100):
            cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (f'User{i}', f'user{i}@example.com'))
            cursor.execute("INSERT INTO orders (user_id, product_name) VALUES (?, ?)", (i, f'Product{i}'))

        conn.commit()
        conn.close()

