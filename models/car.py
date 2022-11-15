from servicable import Servicable


class Car(Servicable):
    def __init__(self):
        super().__init__()
        self.engine = None
        self.battery = None

    def needs_service(self) -> bool:
        pass
