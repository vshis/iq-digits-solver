from typing import List, Tuple

from gameboard.components import BoardSegment, BoardSquare
from gameboard.utils import grid_utils


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


class Zero(Digit):
    def __init__(self) -> None:
        self._value = 0

        # get a square grid
        self._grid = grid_utils.create_grid(1, 1)
        # set values of all segments to 0
        for row in self._grid:
            square_obj: BoardSquare
            for square_obj in row:
                segment: BoardSegment
                for segment in square_obj.get_all_segments().values():
                    segment.set_value(self._value)

        self._grid_up = self._grid_down = self._grid_left = self._grid_right = self._grid


class One(Digit):
    def __init__(self) -> None:
        self._value = 1

        self._grid_up = grid_utils.create_grid(1, 2)
        self._grid_up[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='right', new_value=self._value)
        
        self._grid_down = grid_utils.create_grid(1, 2)
        self._grid_down[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='left', new_value=self._value)

        self._grid_left = grid_utils.create_grid(2, 1)
        self._grid_left[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='up', new_value=self._value)

        self._grid_right = grid_utils.create_grid(2, 1)
        self._grid_right[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='down', new_value=self._value)


class Two(Digit):
    def __init__(self) -> None:
        self._value = 2

        self._grid_up = grid_utils.create_grid(1, 2)
        self._grid_up[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='down', new_value=self._value)
        
        self._grid_down = grid_utils.create_grid(1, 2)
        self._grid_down[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='down', new_value=self._value)

        self._grid_left = grid_utils.create_grid(2, 1)
        self._grid_left[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='down', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='right', new_value=self._value)

        self._grid_right = grid_utils.create_grid(2, 1)
        self._grid_right[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='right', new_value=self._value)


class Three(Digit):
    def __init__(self) -> None:
        self._value = 3

        self._grid_up = grid_utils.create_grid(1, 2)
        self._grid_up[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='down', new_value=self._value)
        
        self._grid_down = grid_utils.create_grid(1, 2)
        self._grid_down[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='down', new_value=self._value)

        self._grid_left = grid_utils.create_grid(2, 1)
        self._grid_left[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='right', new_value=self._value)

        self._grid_right = grid_utils.create_grid(2, 1)
        self._grid_right[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='right', new_value=self._value)


class Four(Digit):
    def __init__(self) -> None:
        self._value = 4

        self._grid_up = grid_utils.create_grid(1, 2)
        self._grid_up[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='right', new_value=self._value)
        
        self._grid_down = grid_utils.create_grid(1, 2)
        self._grid_down[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='right', new_value=self._value)

        self._grid_left = grid_utils.create_grid(2, 1)
        self._grid_left[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='left', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='up', new_value=self._value)

        self._grid_right = grid_utils.create_grid(2, 1)
        self._grid_right[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='up', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='down', new_value=self._value)


class Five(Digit):
    def __init__(self) -> None:
        self._value = 5

        self._grid_up = grid_utils.create_grid(1, 2)
        self._grid_up[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='down', new_value=self._value)
        
        self._grid_down = grid_utils.create_grid(1, 2)
        self._grid_down[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='down', new_value=self._value)

        self._grid_left = grid_utils.create_grid(2, 1)
        self._grid_left[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='right', new_value=self._value)

        self._grid_right = grid_utils.create_grid(2, 1)
        self._grid_right[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='up', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='right', new_value=self._value)


class Six(Digit):
    def __init__(self) -> None:
        self._value = 6

        self._grid_up = grid_utils.create_grid(1, 2)
        self._grid_up[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='down', new_value=self._value)
        
        self._grid_down = grid_utils.create_grid(1, 2)
        self._grid_down[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='down', new_value=self._value)

        self._grid_left = grid_utils.create_grid(2, 1)
        self._grid_left[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='down', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='right', new_value=self._value)

        self._grid_right = grid_utils.create_grid(2, 1)
        self._grid_right[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='up', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='right', new_value=self._value)


class Seven(Digit):
    def __init__(self) -> None:
        self._value = 7

        self._grid_up = grid_utils.create_grid(1, 2)
        self._grid_up[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='right', new_value=self._value)

        self._grid_down = grid_utils.create_grid(1, 2)
        self._grid_down[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='left', new_value=self._value)

        self._grid_left = grid_utils.create_grid(2, 1)
        self._grid_left[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='up', new_value=self._value)

        self._grid_right = grid_utils.create_grid(2, 1)
        self._grid_right[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='right', new_value=self._value)


class Eight(Digit):
    def __init__(self) -> None:
        self._value = 8

        self._grid_up = grid_utils.create_grid(1, 2)
        self._grid_up[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='left', new_value=self._value)

        self._grid_down = grid_utils.create_grid(1, 2)
        self._grid_down[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='left', new_value=self._value)

        self._grid_left = grid_utils.create_grid(2, 1)
        self._grid_left[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='right', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='down', new_value=self._value)

        self._grid_right = grid_utils.create_grid(2, 1)
        self._grid_right[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='right', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='up', new_value=self._value)


class Nine(Digit):
    def __init__(self) -> None:
        self._value = 9

        self._grid_up = grid_utils.create_grid(1, 2)
        self._grid_up[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_up[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_up[1][0].set_segment_value(segment='down', new_value=self._value)

        self._grid_down = grid_utils.create_grid(1, 2)
        self._grid_down[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_down[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_down[1][0].set_segment_value(segment='left', new_value=self._value)

        self._grid_left = grid_utils.create_grid(2, 1)
        self._grid_left[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_left[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='up', new_value=self._value)
        self._grid_left[0][1].set_segment_value(segment='right', new_value=self._value)

        self._grid_right = grid_utils.create_grid(2, 1)
        self._grid_right[0][0].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='left', new_value=self._value)
        self._grid_right[0][0].set_segment_value(segment='right', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='down', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='right', new_value=self._value)
        self._grid_right[0][1].set_segment_value(segment='up', new_value=self._value)
