from car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.spindler_battery import SpindlerBattery


class Glissade(Car):
    def __init__(self):
        super().__init__(WilloughbyEngine, SpindlerBattery)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
