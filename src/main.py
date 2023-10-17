from gameboard import game_board
from gameboard.digits import Zero, One
from gameboard.utils import grid_utils


board = game_board.BoardGrid(height=4, width=5)

grid_utils.draw_grid(grid=board.get_board(), save_path='src/output.png')

zero = Zero()
one = One()

grid_utils.draw_grid(one.get_oriented_grid(orientation='right'), save_path='src/one.png')
