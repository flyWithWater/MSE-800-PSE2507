import threading



class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self, connection_string=None):
        if not hasattr(self, 'initialized'):  # Prevent re-initialization
            self.connection_string = connection_string
            self.initialized = True

    def connect(self):
        if self.connection_string:
            print(f"Connecting to database with {self.connection_string}")
        else:
            print("No connection string provided.")