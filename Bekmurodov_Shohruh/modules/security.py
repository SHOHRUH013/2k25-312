import logging

from Bekmurodov_Shohruh.core.interfaces.i_security import ISecuritySystem

logger = logging.getLogger("Security")


class SecuritySystem(ISecuritySystem):
    def __init__(self):
        self._armed = False

    def arm(self) -> None:
        self._armed = True
        logger.info("Security system armed.")

    def disarm(self) -> None:
        self._armed = False
        logger.info("Security system disarmed.")
