"""Adapter pattern: интеграция внешних сервисов (например, внешний мониторинг API).
Здесь дается простой адаптер, который нормализует интерфейс внешнего логгера."""

class ExternalLogger:
    # внешний сервис с другим интерфейсом
    def send_log(self, msg: str, severity: int):
        print(f"[ExternalLogger severity={severity}] {msg}")

class LoggerAdapter:
    """Adapter: нормализует вызовы system.log("msg") -> external.send_log"""
    def __init__(self, external_logger: ExternalLogger):
        self._ext = external_logger

    def log(self, message: str, level: str = "info"):
        severity = {"debug": 10, "info": 20, "warn": 30, "error": 40}.get(level, 20)
        self._ext.send_log(message, severity)
