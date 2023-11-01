from gameboard import BoardGrid
from gameboard.digits import Zero, One, Seven, Two, Three, Four, Five, Six, Eight, Nine
from gameboard.utils import grid_utils

board = BoardGrid(height=4, width=5)

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

board.place_digit(1, 1, seven, 'left')
board.place_digit(1, 0, one, 'up')

grid_utils.draw_grid(grid=board.get_board(), save_path='src/output.png')
