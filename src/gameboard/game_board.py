from typing import Any
from gameboard.components.board_square import BoardSquare
from gameboard.components.board_segment import BoardSegment

# the game board is layed out with squares like so
#   -   -   -   -   - 
# | x | x | x | x | x |
#   -   -   -   -   - 
# | x | x | x | x | x |
#   -   -   -   -   - 
# | x | x | x | x | x |
#   -   -   -   -   - 
# | x | x | x | x | x |
#   -   -   -   -   - 
# where each x corresponds to coordinates, starting from top left:
#     -       -       -       -       - 
# | (0,0) | (0,1) | (0,2) | (0,3) | (0,4) |
#     -       -       -       -       - 
# | (1,0) | (1,1) | (1,2) | (1,3) | (1,4) |
#     -       -       -       -       - 
# | (2,0) | (2,1) | (2,2) | (2,3) | (2,4) |
#     -       -       -       -       - 
# | (3,0) | (3,1) | (3,2) | (3,3) | (3,4) |
#     -       -       -       -       - 


class BoardGrid:
    def __init__(self, width: int = 5, height: int = 4) -> None:
        self.width = width
        self.height = height
        self.board = self._create_board(width=width, height=height)

    def get_square(self, row: int, col: int):
        """Get the square at coordinates row, col.

        Args:
            row (int): row to access
            col (int): column to access

        Returns:
            Square: object instance within the board
        """
        return self.board[row][col]
    
    def __str__(self) -> str:
        out = f'BoardGrid(width={self.width}, height={self.height}, grid=[\n'
        for row in self.board:
            out += '['
            for square in row:
                out += str(square) + ', '
            out = out[:-2]
            out += '],\n'
        out += ')'
        return out


    @staticmethod
    def _create_board(width: int, height: int):
        """Creates a game board with Square objects of given width and height.

        By default, there are 4 rows (height = 4) and 5 columns (width = 5), as follows:

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

        Each Square is surrounded by segments on four sides. Some segments are shared by some squares.
        For example, (0,0) shares right segment with (0,1) left segment.

        Args:
            width (int): number of columns of the game board
            height (int): number of rows of the game board

        Returns:
            list of lists: the return object is a list of lists, such that to access the square (0,0): board[0][0]
        """
        # create board of correct shape with None values
        board = [[None for _ in range(width)] for _ in range(height)]

        # populate empty board with Square objects
        for row in range(height):
            for col in range(width):
                # link left segment to the right segment of the square on the left
                if col > 0:
                    segment_left = board[row][col-1].segment_right
                else:
                    segment_left = BoardSegment()
                # link top segment to the bottom segment of the square above
                if row > 0:
                    segment_up = board[row-1][col].segment_down
                else:
                    segment_up = BoardSegment()
                segment_down = BoardSegment()
                segment_right = BoardSegment()
                square = BoardSquare(
                    segment_up,
                    segment_down,
                    segment_left,
                    segment_right,
                )
                board[row][col] = square
        
        return board
