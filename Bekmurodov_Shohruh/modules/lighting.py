import logging

from Bekmurodov_Shohruh.core.builders.lighting_builder import LightingScene

logger = logging.getLogger("Lighting")


class LightingSystem:
    def __init__(self) -> None:
        self._current_scene: LightingScene | None = None

    def apply_scene(self, scene: LightingScene) -> None:
        self._current_scene = scene
        logger.info(
            f"Lighting scene applied: area={scene.area}, "
            f"brightness={scene.brightness}, schedule={scene.schedule}"
        )

    def dim_global(self, brightness: int) -> None:
        if self._current_scene:
            logger.info(f"Global brightness adjusted to {brightness}%")
            self._current_scene.brightness = brightness
