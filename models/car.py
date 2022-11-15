from servicable import Servicable


class Car(Servicable):
    def __init__(self, engine, battery):
        super().__init__()
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        pass
