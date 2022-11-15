from models.car import Car
from engines.capulet_engine import CapuletEngine
from batteries.nubbin_battery import NubbinBattery


class Thovex(Car):
    def __init__(self):
        super().__init__()
        self.engine = CapuletEngine
        self.battery = NubbinBattery

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
