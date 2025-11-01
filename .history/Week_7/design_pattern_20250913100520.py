import sqlite3
import threading



class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()


    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_connection'):
            self._connection = None
        

    def get_connection(self):
        if self._connection is None:
            self._connection = sqlite3.connect('app.db')
        return self._connection
    
    def close_connection(self):
        if self._connection:
            self._connection.close()
            self._connection = None




class UserService:
    def __init__(self):
        self.db = DatabaseConnection().get_connection()

    def get_user(self, user_id):
         # New connection
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()        
        return result


class OrderService:
    def __init__(self):
        self.db = DatabaseConnection().get_connection()

    def get_orders(self, user_id):
         # Another new connection
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
        result = cursor.fetchall()
        return result
    

    