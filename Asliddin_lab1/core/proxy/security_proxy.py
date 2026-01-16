class SecurityProxy:
    def __init__(self, real_security, auth_checker=None):
        self._real = real_security
        self._auth_checker = auth_checker or (lambda user: user.get("role") == "admin")

    def view_cameras(self, user):
        if not self._auth_checker(user):
            raise PermissionError("Access denied: user is not admin")
        return self._real.view_cameras()

    def activate(self, user=None):
        if user and not self._auth_checker(user):
            raise PermissionError("Access denied: cannot activate security")
        return self._real.activate()

