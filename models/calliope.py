from car import Car
from engines.capulet_engine import CapuletEngine
from batteries.spindler_battery import SpindlerBattery


class Calliope(Car):
    def __init__(self):
        super().__init__(CapuletEngine, SpindlerBattery)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
