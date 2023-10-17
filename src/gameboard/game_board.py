from typing import List, Tuple

from gameboard.components import BoardSegment, BoardSquare
from gameboard.utils import grid_utils


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
    def __init__(self, width: int = 5, height: int = 4) -> None:
        self.width = width
        self.height = height
        self.board = grid_utils.create_grid(width=self.width, height=self.height)

    def get_board(self) -> List[List[object]]:
        return self.board

    def get_shape(self) -> Tuple[int, int]:
        """Returns an integer tuple (height, width).
        In other words, (number_of_rows, number_of_cols)

        Returns:
            Tuple[int, int]: tuple of height, width
        """
        return (self.height, self.width)

    def get_square(self, row: int, col: int) -> BoardSquare:
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
