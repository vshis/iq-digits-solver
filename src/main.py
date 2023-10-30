from gameboard import game_board
from gameboard.digits import Zero, One
from gameboard.utils import grid_utils

board = game_board.BoardGrid(height=4, width=5)

zero = Zero()
one = One()

board.place_digit(1, 1, zero, 'up')
board.place_digit(1, 2, one, 'down')
grid_utils.draw_grid(grid=board.get_board(), save_path='src/output.png')
