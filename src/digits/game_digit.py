from abc import ABC, abstractmethod

class GameDigit(ABC):
    @abstractmethod
    def _set_grid(self):
        pass

    @abstractmethod
    def get_grid(self):
        pass
    
    @abstractmethod
    def _set_value(self):
        pass

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set_direction(self):
        pass

    @abstractmethod
    def get_direction(self):
        pass
    

class Zero(GameDigit):
    def __init__(self) -> None:
        self.value = self._set_value()

    def _set_value(self):
        self.value = 0        


if __name__ == '__main__':
    zero = Zero()
