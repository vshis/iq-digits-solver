from gameboard import game_board
from gameboard.digits import Zero, One, Seven
from gameboard.utils import grid_utils

board = game_board.BoardGrid(height=4, width=5)

zero = Zero()
one = One()
seven = Seven()

board.place_digit(2, 1, one, 'right')
board.place_digit(2, 2, seven, 'down')
grid_utils.draw_grid(grid=board.get_board(), save_path='src/output.png')
