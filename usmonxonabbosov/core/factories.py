"""Factory Method / Abstract Factory: создание подсистем (lighting, transport, security, energy)."""

from modules import lighting, transport, security, energy

class ModuleFactory:
    """Factory for creating modules by name."""
    def create(self, name: str):
        name = name.lower()
        if name == "lighting":
            return lighting.LightingSubsystem()
        if name == "transport":
            return transport.TransportSubsystem()
        if name == "security":
            return security.SecuritySubsystem()
        if name == "energy":
            return energy.EnergySubsystem()
        raise ValueError(f"Unknown module: {name}")
