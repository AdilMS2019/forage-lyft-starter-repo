from models.car import Car
from engines.capulet_engine import CapuletEngine
from batteries.nubbin_battery import NubbinBattery


class Thovex(Car):
    def __init__(self):
        super().__init__(CapuletEngine, NubbinBattery)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
