from gameboard import game_board
from gameboard.digits import Zero, One, Seven, Two, Three, Four, Five, Six, Eight, Nine
from gameboard.utils import grid_utils

board = game_board.BoardGrid(height=4, width=5)

zero = Zero()
one = One()
two = Two()
three = Three()
four = Four()
five = Five()
six = Six()
seven = Seven()
eight = Eight()
nine = Nine()

# grid_utils.draw_grid(two.get_grid_oriented('up'), save_path='src/two.png')
# grid_utils.draw_grid(two.get_grid_oriented('up'), save_path='src/two.png')
# grid_utils.draw_grid(two.get_grid_oriented('up'), save_path='src/two.png')
# grid_utils.draw_grid(two.get_grid_oriented('up'), save_path='src/two.png')
# exit()

board.place_digit(1, 0, nine, 'up')
board.place_digit(3, 0, nine, 'right')
board.place_digit(0, 2, nine, 'down')
board.place_digit(3, 4, nine, 'left')
board.place_digit(0, 4, seven, 'down')

grid_utils.draw_grid(grid=board.get_board(), save_path='src/output.png')
