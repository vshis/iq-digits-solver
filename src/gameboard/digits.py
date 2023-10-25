from typing import List, Tuple

from gameboard.components import BoardSegment, BoardSquare
from gameboard.utils import grid_utils


class Digit:
    def __init__(self) -> None:
        self.grid_up = self.grid_down = self.grid_left = self.grid_right = None
    
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
            return (len(self.grid_up), len(self.grid_up[0]))
        elif orientation == 'down':
            return (len(self.grid_down), len(self.grid_down[0]))
        elif orientation == 'left':
            return (len(self.grid_left), len(self.grid_left[0]))
        elif orientation == 'right':
            return (len(self.grid_right), len(self.grid_right[0]))
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
            return self.grid_up
        elif orientation == 'down':
            return self.grid_down
        elif orientation == 'left':
            return self.grid_left
        elif orientation == 'right':
            return self.grid_right
        else:
            raise ValueError(f'Invalid orientation chosen: "{orientation}".')


class Zero(Digit):
    def __init__(self) -> None:
        # get a square grid
        self._grid = grid_utils.create_grid(1, 1)
        # set values of all segments to 0
        for row in self._grid:
            square_obj: BoardSquare
            for square_obj in row:
                segment: BoardSegment
                for segment in square_obj.get_all_segments():
                    segment.set_value(0)

        self.grid_up = self.grid_down = self.grid_left = self.grid_right = self._grid


class One(Digit):
    def __init__(self) -> None:
        self.grid_up = grid_utils.create_grid(1, 2)
        self.grid_up[0][0].set_segment_value(segment='left', new_value=1)
        self.grid_up[1][0].set_segment_value(segment='left', new_value=1)
        
        self.grid_down = grid_utils.create_grid(1, 2)
        self.grid_down[0][0].set_segment_value(segment='right', new_value=1)
        self.grid_down[1][0].set_segment_value(segment='right', new_value=1)

        self.grid_left = grid_utils.create_grid(2, 1)
        self.grid_left[0][0].set_segment_value(segment='down', new_value=1)
        self.grid_left[0][1].set_segment_value(segment='down', new_value=1)

        self.grid_right = grid_utils.create_grid(2, 1)
        self.grid_right[0][0].set_segment_value(segment='up', new_value=1)
        self.grid_right[0][1].set_segment_value(segment='up', new_value=1)
