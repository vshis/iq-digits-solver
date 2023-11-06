from iq_game.digits import Digit
from iq_game.utils import grid_utils
from iq_game.components import BoardSegment, BoardSquare


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
