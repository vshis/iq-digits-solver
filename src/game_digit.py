from abc import ABC, abstractmethod

class GameDigit:
    def __init__(self) -> None:
        self.value = None
        self.grid = None
        self.color = None
