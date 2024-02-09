from abc import ABC,abstractmethod

class UIInterface(ABC):
    def add_task(self):
        pass

class MediatorInterface(ABC):
    def getMoney(self):
        pass