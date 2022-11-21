import unittest
from datetime import datetime
from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery


class TestNubbin(unittest.TestCase):
    def should_be_serviced(self):
        current_date = datetime.today().date()
        battery = NubbinBattery(current_date.replace(
            year=current_date.year - 5), current_date)
        self.assertEqual(battery.needs_service(), True, "Should be true.")

    def should_not_be_serviced(self):
        current_date = datetime.today().date()
        battery = NubbinBattery(current_date.replace(
            year=current_date.year - 3), current_date)
        self.assertEqual(battery.needs_service(), False, "Should be false.")

    def should_be_serviced_edge_false(self):
        current_date = datetime.today().date()
        battery = NubbinBattery(current_date.replace(
            year=current_date.year - 4), current_date)
        self.assertEqual(battery.needs_service(), False, "Should be false.")


class TestSpindler(unittest.TestCase):
    def should_be_serviced(self):
        current_date = datetime.today().date()
        battery = SpindlerBattery(current_date.replace(
            year=current_date.year - 3), current_date)
        self.assertEqual(battery.needs_service(), True, "Should be true.")

    def should_not_be_serviced(self):
        current_date = datetime.today().date()
        battery = SpindlerBattery(current_date.replace(
            year=current_date.year - 1), current_date)
        self.assertEqual(battery.needs_service(), False, "Should be false.")

    def should_be_serviced_edge_false(self):
        current_date = datetime.today().date()
        battery = SpindlerBattery(current_date.replace(
            year=current_date.year - 2), current_date)
        self.assertEqual(battery.needs_service(), False, "Should be false.")


class TestCapulet(unittest.TestCase):
    def should_be_serviced(self):
        engine = CapuletEngine(0, 40000)
        self.assertEqual(engine.needs_service(), True, "Should be true")

    def should_not_be_serviced(self):
        engine = CapuletEngine(0, 20000)
        self.assertEqual(engine.needs_service(), False, "Should be false")

    def should_be_serviced_edge_false(self):
        engine = CapuletEngine(0, 30000)
        self.assertEqual(engine.needs_service(), False, "Should be false")


class TestSternman(unittest.TestCase):
    def should_be_serviced(self):
        engine = SternmanEngine(True)
        self.assertEqual(engine.needs_service(), True, "Should be true")
        

    def should_not_be_serviced(self):
        engine = SternmanEngine(False)
        self.assertEqual(engine.needs_service(), False, "Should be false")


class TestWilloughby(unittest.TestCase):
    def should_be_serviced(self):
        engine = WilloughbyEngine(0, 70000)
        self.assertEqual(engine.needs_service(), True, "Should be true")

    def should_not_be_serviced(self):
        engine = WilloughbyEngine(0, 20000)
        self.assertEqual(engine.needs_service(), False, "Should be false")

    def should_be_serviced_edge_false(self):
        engine = WilloughbyEngine(0, 60000)
        self.assertEqual(engine.needs_service(), False, "Should be false")


if __name__ == '__main__':
    unittest.main()
