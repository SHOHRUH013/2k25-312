from abc import ABC, abstractmethod


class ISecuritySystem(ABC):
    @abstractmethod
    def arm(self) -> None:
        pass

    @abstractmethod
    def disarm(self) -> None:
        pass
