from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def needs_service():
        pass
