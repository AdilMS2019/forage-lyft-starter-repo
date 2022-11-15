from models.car import Car
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery


class Rorschach(Car):
    def __init__(self):
        super().__init__(WilloughbyEngine, NubbinBattery)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
