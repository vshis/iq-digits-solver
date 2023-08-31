from .segment import Segment
from typing import Literal

class One:
    def __init__(self) -> None:
        self._value = 1

    def get_grid(self, direction: Literal['down', 'right', 'left', 'up']) -> list[list[Segment]]:
        if direction == 'down':
            # grid is showing the shape of the digit: row by row
            grid = [
                [Segment('horizontal', value=None)],
                [Segment('vertical', value=self._value)],
                [Segment('horizontal', value=None)],
                [Segment('vertical', value=self._value)]
            ]
        elif direction == 'right':
            # column by column
            grid = [
                [Segment('vertical', value=None)],
                [Segment('horizontal', value=self._value)],
                [Segment('vertical', value=None)],
                [Segment('horizontal', value=self._value)]
            ]
        else:
            pass
        return grid

    def get_value(self):
        return self._value
