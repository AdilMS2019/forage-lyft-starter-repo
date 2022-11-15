from car import Car
from engines.sternman_engine import SternmanEngine
from batteries.spindler_battery import SpindlerBattery


class Palindrome(Car):
    def __init__(self):
        super().__init__(SternmanEngine, SpindlerBattery)

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
