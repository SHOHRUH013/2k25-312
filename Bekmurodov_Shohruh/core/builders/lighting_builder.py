from dataclasses import dataclass


@dataclass
class LightingScene:
    area: str
    brightness: int
    schedule: str


class LightingSceneBuilder:

    def __init__(self) -> None:
        self._reset()

    def _reset(self) -> None:
        self._area = "default"
        self._brightness = 50
        self._schedule = "20:00-06:00"

    def set_area(self, area: str) -> "LightingSceneBuilder":
        self._area = area
        return self

    def set_brightness(self, brightness: int) -> "LightingSceneBuilder":
        self._brightness = max(0, min(100, brightness))
        return self

    def set_schedule(self, schedule: str) -> "LightingSceneBuilder":
        self._schedule = schedule
        return self

    def build(self) -> LightingScene:
        scene = LightingScene(
            area=self._area,
            brightness=self._brightness,
            schedule=self._schedule,
        )
        self._reset()
        return scene
