from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import pathlib

from gameboard.components import BoardSegment, BoardSquare
from gameboard.utils import create_grid


COLOR_MAPPING = {
    0: '#ff0533',
    1: '#ffc105',
    2: '#fbff05',
    3: '#c9ff05',
    4: '#0a9100',
    5: '#d9fbff',
    6: '#07abf7',
    7: '#0234bf',
    8: '#4d02b0',
    9: '#f73bf4',
    None: '#575c58'
    }


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
        self.board = create_grid.create_grid(width=self.width, height=self.height)

    def get_board(self):
        return self.board

    def get_square(self, row: int, col: int) -> BoardSquare:
        """Get the square at coordinates row, col.

        Args:
            row (int): row to access
            col (int): column to access

        Returns:
            Square: object instance within the board
        """
        return self.board[row][col]
    
    def draw(self, save_path: str | pathlib.Path | None = None):
        pathpatches = []

        for row_idx, row in enumerate(self.get_board()):
            row_idx *= -1
            for square_idx, square_obj in enumerate(row):
                # 4 sections: up, right, down, left
                # each section is a tuple: (two_pairs_of_coords, segment)
                # two pairs of coords is a list: [(x, y), (x, y)]
                sections = [
                    ([(square_idx - 0.5, row_idx + 0.5), (square_idx + 0.5, row_idx + 0.5)], square_obj.segment_up),
                    ([(square_idx + 0.5, row_idx + 0.5), (square_idx + 0.5, row_idx - 0.5)], square_obj.segment_right),
                    ([(square_idx + 0.5, row_idx - 0.5), (square_idx - 0.5, row_idx - 0.5)], square_obj.segment_down),
                    ([(square_idx - 0.5, row_idx - 0.5), (square_idx - 0.5, row_idx + 0.5)], square_obj.segment_left),
                ]
                codes = [Path.MOVETO, Path.LINETO]

                for vertices, segment in sections:
                    color = COLOR_MAPPING.get(segment.get_value())
                    pathpatches.append(
                        PathPatch(
                            Path(vertices, codes),
                            edgecolor=color,
                            linewidth=10
                        )
                    )

        collection = PatchCollection(pathpatches, match_original=True)

        fig, ax = plt.subplots()
        ax.add_collection(collection)
        ax.autoscale_view()
        ax.set_xticks([i for i in range(self.width)], labels=[str(i) for i in range(self.width)])
        ax.set_yticks([-1*i for i in range(self.height)], labels=[str(i) for i in range(self.height)])
        ax.xaxis.tick_top()
        ax.set_aspect('equal')

        if save_path:
            fig.savefig(pathlib.Path(save_path))
    
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
