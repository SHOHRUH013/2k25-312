class Logger:
    """
    Singleton pattern
    Purpose: ensures only one logger instance exists in the system
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message):
        print(f"[LOG]: {message}")
