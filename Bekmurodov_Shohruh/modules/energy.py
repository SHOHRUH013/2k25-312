import logging
from typing import List

from Bekmurodov_Shohruh.core.builders.lighting_builder import LightingScene
from Bekmurodov_Shohruh.modules.transport import Vehicle

logger = logging.getLogger("Energy")


class EnergySystem:
    def __init__(self):
        self._lighting_log: List[LightingScene] = []
        self._transport_log: List[Vehicle] = []

    def register_lighting(self, scene: LightingScene) -> None:
        self._lighting_log.append(scene)
        logger.info(f"Energy log: lighting scene added for {scene.area}")

    def register_transport(self, vehicle: Vehicle) -> None:
        self._transport_log.append(vehicle)
        logger.info(f"Energy log: transport departure recorded: {vehicle.name}")

    def report(self) -> None:
        logger.info(
            f"Energy stats — lighting: {len(self._lighting_log)}, "
            f"transport: {len(self._transport_log)}"
        )
