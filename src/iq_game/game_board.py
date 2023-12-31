from typing import List, Tuple
from copy import deepcopy

from iq_game.components import BoardSquare
from iq_game.utils import grid_utils
from iq_game.digits import Digit


class BoardGrid:
    """Default grid of Square objects (row, col):
    
    ```python
        -       -       -       -       - 
    | (0,0) | (0,1) | (0,2) | (0,3) | (0,4) |
        -       -       -       -       - 
    | (1,0) | (1,1) | (1,2) | (1,3) | (1,4) |
        -       -       -       -       - 
    | (2,0) | (2,1) | (2,2) | (2,3) | (2,4) |
        -       -       -       -       - 
    | (3,0) | (3,1) | (3,2) | (3,3) | (3,4) |
        -       -       -       -       - 
    ```
    """    
    def __init__(self, width: int = 5, height: int = 4, initial_state = []) -> None:
        self._width = width
        self._height = height
        self._board = grid_utils.create_grid(width=self._width, height=self._height)
        self._placed_values = []
        self._initial_values = []
        # initial state is a dict of initially placed values, which cannot be removed
        # self._initial_state = [(1, 1, 'one', 'up'), (2, 2, 'zero', 'up')]
        # for placement in initial_state:
        #     self.place_digit(*placement)

    def is_terminal(self):
        """Returns True if the game reached a terminal state.
        Terminal state is when all digits have been placed in allowed positions on the board.

        Returns:
            bool: True if all ten digits were placed in allowed positions and game is technically
            "won". False otherwise.
        """
        if len(self._placed_values) == 10:
            return True
        return False
    
    def reset(self):
        self.set_board(grid_utils.create_grid(width=self._width, height=self._height))
        self._placed_values = []

    def get_board(self) -> List[List[BoardSquare]]:
        return self._board
    
    def set_board(self, new_board: List[List[BoardSquare]]) -> None:
        """Set the board list of lists to a new list of lists.

        Args:
            new_board (List[List[object]]): list of lists of Square objects, defining the new board.
        """
        self._board = new_board
        self._height = len(self._board)
        self._width = len(self._board[0])

    def get_shape(self) -> Tuple[int, int]:
        """Returns an integer tuple (height, width).
        In other words, (number_of_rows, number_of_cols)

        Returns:
            Tuple[int, int]: tuple of height, width
        """
        return (self._height, self._width)

    def get_square(self, row: int, col: int) -> BoardSquare:
        """Get the square at coordinates row, col.

        Args:
            row (int): row to access
            col (int): column to access

        Returns:
            Square: object instance within the board
        """
        return self._board[row][col]
    
    def get_placed_digits(self) -> List:
        """Returns list of values of digits already on board.

        Returns:
            List: list of values of digits currently placed on board.
        """
        return self._placed_values
    
    def remove_digit(self, digit: Digit) -> None:
        """Method removes given digit from board.

        Args:
            digit (Digit): instance of a Digit object.
        """
        digit_value = digit.get_value()
        if digit_value not in self._placed_values:
            return
        for row in self.get_board():
            for square in row:
                for key in square.get_all_segments().keys():
                    if square.get_segment(key).get_value() == digit_value:
                        square.set_segment_value(key, None)
        self._placed_values.remove(digit_value)
    
    def place_digit(self, row_coord: int, col_coord: int, digit: Digit, orientation: str) -> Tuple[bool, str]:
        """Method takes in row, col, digit and orientation and attempts to place it.

        Args:
            row_coord (int): value of row on the board grid where to place the digit
            col_coord (int): value of column on the board grid where to place the digit
            digit (Digit): instance of Digit object
            orientation (str): 'up', 'down', 'left' or 'right' - direction in which we want to place the chosen digit

        Raises:
            ValueError: if invalid orientation provided
        
        Returns: 
            Tuple of (bool, str), boolean whether digit placement is valid, if it is valid, the digit is placed. 
            Str error message if placement is invalid, otherwise empty string.
        """
        current_value = digit.get_value()
        if current_value in self._placed_values:
            return False, f'Digit {digit} has already been placed on the board.'

        temp_board = deepcopy(self.get_board())

        # list of lists of squares
        digit_grid = digit.get_grid_oriented(orientation)
        digit_shape = digit.get_shape_oriented(orientation)
        digit_shape_norm = (digit_shape[0] - 1, digit_shape[1] - 1)
        placements = digit_shape[0] * digit_shape[1]

        for placement_number in range(placements):
            if orientation == 'up':
                board_row = row_coord - placement_number
                board_col = col_coord
                digit_square = digit_grid[digit_shape_norm[0] - placement_number][digit_shape_norm[1]]
            elif orientation == 'down':
                board_row = row_coord + placement_number
                board_col = col_coord
                digit_square = digit_grid[placement_number][digit_shape_norm[1]]
            elif orientation == 'left':
                board_row = row_coord
                board_col = col_coord - placement_number
                digit_square = digit_grid[digit_shape_norm[0]][digit_shape_norm[1] - placement_number]
            elif orientation == 'right':
                board_row = row_coord
                board_col = col_coord + placement_number
                digit_square = digit_grid[digit_shape_norm[0]][placement_number]
            else:
                raise ValueError(f'Unrecognized value for orientation: {orientation}')
            
            # check that the target row and col are within board
            if not (board_row >= 0 and board_row < self._height and board_col >= 0 and board_col < self._width):
                return False, f'Chosen coordinates "row={board_row}, col={board_col}" are outside the board of shape {self.get_shape()}.'
            
            board_square: BoardSquare
            board_square = temp_board[board_row][board_col]

            # check if the digit square grid can fit on the board grid
            for key in digit_square.get_all_segments().keys():
                digit_segment_val = digit_square.get_segment(key).get_value()
                board_segment = board_square.get_segment(key)
                board_segment_val = board_segment.get_value()

                # check if current board segment is None, or if it is not None, then whether the new segment is None
                # or whether the digit segment is the same as board segment (both equal a value that's not None)
                # which happens when placing digits where 2 squares share a middle segment (like 2, 3, 4, 5, 6, 8, 9)
                # otherwise we are trying to place a value in occupied segment - thus throw error
                if not (
                    board_segment_val is None or (
                        board_segment_val is not None and (
                            digit_segment_val is None or digit_segment_val == board_segment_val
                            ))):
                    return False, f'Cannot place {digit} oriented {orientation} at row={board_row}, col={board_col}, as segment at {key} is already occupied by {board_segment_val}.'

                if digit_segment_val is not None:
                    board_square.set_segment_value(key, digit_segment_val)
            
        # check if seven and one are crossing over, if applicable
        if current_value == 1 or current_value == 7:
            other_value = 1 if current_value == 7 else 7
            if orientation == 'up' and col_coord + 1 < self._width:
                left_square: BoardSquare = temp_board[row_coord][col_coord]
                right_square: BoardSquare = temp_board[row_coord][col_coord + 1]
                if left_square.get_segment('up').get_value() == other_value and right_square.get_segment('up').get_value() == other_value:
                    return False, f'Chosen coordinates "row={board_row}, col={board_col}" result in {current_value} crossing over {other_value}.'
            elif orientation == 'down' and col_coord - 1 >= 0:
                left_square: BoardSquare = temp_board[row_coord][col_coord - 1]
                right_square: BoardSquare = temp_board[row_coord][col_coord]
                if left_square.get_segment('down').get_value() == other_value and right_square.get_segment('down').get_value() == other_value:
                    return False, f'Chosen coordinates "row={board_row}, col={board_col}" result in {current_value} crossing over {other_value}.'
            elif orientation == 'left' and row_coord - 1 >= 0:
                top_square: BoardSquare = temp_board[row_coord - 1][col_coord]
                bottom_square: BoardSquare = temp_board[row_coord][col_coord]
                if top_square.get_segment('left').get_value() == other_value and bottom_square.get_segment('left').get_value() == other_value:
                    return False, f'Chosen coordinates "row={board_row}, col={board_col}" result in {current_value} crossing over {other_value}.'
            elif orientation == 'right' and row_coord + 1 < self._height:
                top_square: BoardSquare = temp_board[row_coord][col_coord]
                bottom_square: BoardSquare = temp_board[row_coord + 1][col_coord]
                if top_square.get_segment('right').get_value() == other_value and bottom_square.get_segment('right').get_value() == other_value:
                    return False, f'Chosen coordinates "row={board_row}, col={board_col}" result in {current_value} crossing over {other_value}.'
                
        self.set_board(temp_board)
        del temp_board
        self._placed_values.append(digit.get_value())
        return True, ''
    
    def __str__(self) -> str:
        out = f'BoardGrid(width={self._width}, height={self._height}, grid=[\n'
        for row in self._board:
            out += '['
            for square in row:
                out += str(square) + ', '
            out = out[:-2]
            out += '],\n'
        out += ')'
        return out
