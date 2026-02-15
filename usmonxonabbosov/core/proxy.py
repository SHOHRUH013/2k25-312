"""Proxy pattern: контроль доступа к подсистемам (например, проверка роли пользователя)."""

class ModuleProxy:
    def __init__(self, module, user_role="guest"):
        self._module = module
        self._role = user_role

    def perform(self, action: str, *args, **kwargs):
        # простая модель прав: guest -> read-only, admin -> all
        if self._role != "admin" and action == "configure":
            raise PermissionError("Требуются права администратора для конфигурации.")
        method = getattr(self._module, action, None)
        if method is None:
            raise AttributeError(f"Action {action} not supported by module.")
        return method(*args, **kwargs)
