from typing import List, Tuple


class Digit:
    def __init__(self) -> None:
        self._value = None
        self._grid_up = self._grid_down = self._grid_left = self._grid_right = None
    
    def get_shape_oriented(self, orientation: str) -> Tuple[int, int]:
        """Returns an integer tuple (height, width)

        Args:
            orientation (str): one of ('up', 'down', 'left', 'right')

        Raises:
            ValueError: when invalid orientation is given
            
        Returns:
            Tuple[int, int]: tuple of height, width
        """
        if orientation == 'up':
            return (len(self._grid_up), len(self._grid_up[0]))
        elif orientation == 'down':
            return (len(self._grid_down), len(self._grid_down[0]))
        elif orientation == 'left':
            return (len(self._grid_left), len(self._grid_left[0]))
        elif orientation == 'right':
            return (len(self._grid_right), len(self._grid_right[0]))
        else:
            raise ValueError(f'Invalid orientation chosen: "{orientation}".')

    def get_grid_oriented(self, orientation: str) -> List[List[object]]:
        """Returns the grid of the digit, as a list of lists of Squares.

        Args:
            orientation (str): one of ('up', 'down', 'left', 'right')

        Raises:
            ValueError: when invalid orientation is given

        Returns:
            List[List[object]]: Square objects in given layout
        """
        if orientation == 'up':
            return self._grid_up
        elif orientation == 'down':
            return self._grid_down
        elif orientation == 'left':
            return self._grid_left
        elif orientation == 'right':
            return self._grid_right
        else:
            raise ValueError(f'Invalid orientation chosen: "{orientation}".')
        
    def get_value(self) -> int | None:
        return self._value
    
    def __str__(self) -> str:
        return f'{self.__class__.__name__}(shape={self.get_shape_oriented("up")})'

