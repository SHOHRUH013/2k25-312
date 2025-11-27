from ..interfaces.i_security import ISecuritySystem
import logging

logger = logging.getLogger("SecurityProxy")


class SecuritySystemProxy(ISecuritySystem):
    def __init__(self, real_system: ISecuritySystem):
        self._real = real_system
        self._authorized = False

    def authorize(self, token: str) -> None:
        if token == "ADMIN":
            self._authorized = True
            logger.info("User authorized successfully.")
        else:
            logger.warning("Authorization failed.")

    def _check_access(self) -> None:
        if not self._authorized:
            raise PermissionError("Access denied: unauthorized user.")

    def arm(self) -> None:
        self._check_access()
        logger.info("Arming security system...")
        self._real.arm()

    def disarm(self) -> None:
        self._check_access()
        logger.info("Disarming security system...")
        self._real.disarm()
