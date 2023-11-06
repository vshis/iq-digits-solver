from iq_game.digits import Digit
from iq_game.utils import grid_utils


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
