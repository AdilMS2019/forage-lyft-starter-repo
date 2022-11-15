import datetime
from models.car import Car
from models.calliope import Calliope
from models.glissade import Glissade
from models.palindrome import Palindrome
from models.rorschach import Rorschach
from models.thovex import Thovex


class CarFactory(Car):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        car = Calliope()
        car.engine.last_service_mileage = last_service_mileage
        car.engine.current_mileage = current_mileage
        car.battery.last_service_date = last_service_date
        car.battery.current_date = current_date
        return car

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        car = Glissade()
        car.engine.last_service_mileage = last_service_mileage
        car.engine.current_mileage = current_mileage
        car.battery.last_service_date = last_service_date
        car.battery.current_date = current_date
        return car

    def create_palindrome(self, current_date, last_service_date, warning_light_on) -> Car:
        car = Palindrome()
        car.engine.warning_light_on = warning_light_on
        car.battery.last_service_date = last_service_date
        car.battery.current_date = current_date
        return car

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        car = Rorschach()
        car.engine.last_service_mileage = last_service_mileage
        car.engine.current_mileage = current_mileage
        car.battery.last_service_date = last_service_date
        car.battery.current_date = current_date
        return car

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        car = Thovex()
        car.engine.last_service_mileage = last_service_mileage
        car.engine.current_mileage = current_mileage
        car.battery.last_service_date = last_service_date
        car.battery.current_date = current_date
        return car
