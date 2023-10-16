from gameboard.components import BoardSegment, BoardSquare
from gameboard.utils import create_grid


class Zero:
    def __init__(self) -> None:
        # get a square grid
        self._grid = create_grid.create_grid(1, 1)
        # set values of all segments to 0
        for row in self._grid:
            square_obj: BoardSquare
            for square_obj in row:
                segment: BoardSegment
                for segment in square_obj.get_all_segments():
                    segment.set_value(0)

        self.grid_up = self.grid_down = self.grid_left = self.grid_right = self._grid

class One:
    def __init__(self) -> None:
        pass
