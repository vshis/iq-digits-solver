from copy import deepcopy

from gameboard import game_board
from gameboard.digits import Zero, One
from gameboard.utils import grid_utils
from gameboard.components import BoardSegment, BoardSquare


board = game_board.BoardGrid(height=4, width=5)

# grid_utils.draw_grid(grid=board.get_board(), save_path='src/output.png')

zero = Zero()
one = One()


# we want a function that:
# board.place_digit(x, y, digit, orientation='up')
# takes in the coordinates of where on the board to place, the digit object and the orientation
row_coord, col_coord = 1, 2
digit = zero
orientation = 'up'

valid = True  # keeps track of whether the placement is valid

# list of lists of squares
temp_board = deepcopy(board.get_board())
board_shape = board.get_shape()

# check that the chosen row and col are within board
if row_coord >= 0 and row_coord < board.height and col_coord >= 0 and col_coord < board.width:
    valid = True
else:
    raise ValueError(f'Chosen coordinates "{row_coord}, {col_coord}" are outside the board of shape {board_shape}.')

# list of lists of squares
digit_grid = digit.get_grid_oriented(orientation)
digit_grid_shape = digit.get_shape_oriented(orientation)

board_squares_to_check = []
for row_idx, row in enumerate(digit_grid):
    digit_square: BoardSquare
    for square_idx, digit_square in enumerate(row):
        board_square: BoardSquare
        board_square = temp_board[row_idx+row_coord][square_idx+col_coord]

        # check if the digit grid can fit on the board
        
