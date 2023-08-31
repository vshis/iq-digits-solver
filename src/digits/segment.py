from typing import Literal

class Segment:
    def __init__(
            self, 
            direction: Literal['vertical', 'horizontal'] = 'vertical',
            value: None | Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] = None
            ) -> None:
        self._values = [i for i in range(10)] + [None]
        self._directions = ['vertical', 'horizontal']
        self._direction: str
        self._value: int | None
        self.set_direction(direction)
        self.set_value(value)

    def set_direction(self, new_direction):
        if new_direction in self._directions:
            self._direction = new_direction
        else:
            raise AttributeError(f'Direction {new_direction} is not an acceptable direction: {self._directions}.')
    
    def get_direction(self):
        return self._direction

    def set_value(self, new_value):
        if new_value in self._values:
            self._value = new_value
        else:
            raise AttributeError(f'Value {new_value} is not an acceptable value: {self._values}.')

    def get_value(self):
        return self._value
    
    def __str__(self) -> str:
        return f"{'|' if self._direction == 'vertical' else '_'}{self._value}"
        # return f"{('|' if self._direction == 'vertical' else '_') if self._value else '.'}"
    
    def __repr__(self) -> str:
        # return f"{('|' if self._direction == 'vertical' else '_') if self._value else '.'}"
        return f"{'|' if self._direction == 'vertical' else '_'}{self._value}"


if __name__ == '__main__':
    s = Segment()
    print(s)
