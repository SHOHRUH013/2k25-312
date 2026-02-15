class AccessProxy:
    """
    Proxy pattern
    Purpose: controls access to subsystem methods
    """
    def __init__(self, subsystem, role="user"):
        self.subsystem = subsystem
        self.role = role

    def operate(self):
        if self.role != "admin":
            print("Access denied: admin only")
        else:
            self.subsystem.operate()
