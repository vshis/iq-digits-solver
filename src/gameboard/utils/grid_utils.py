from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import pathlib
from typing import List

from gameboard.components import BoardSegment, BoardSquare


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


def create_grid(width: int, height: int):
    """Creates a grid with Square objects of given width and height as a list of lists.

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


def draw_grid(grid: List[List[object]], save_path: str | pathlib.Path | None = None):
    pathpatches = []

    for row_idx, row in enumerate(grid):
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
    board_height = len(grid)
    board_width = len(grid[0])
    ax.set_xticks([i for i in range(board_width)], labels=[str(i) for i in range(board_width)])
    ax.set_yticks([-1*i for i in range(board_height)], labels=[str(i) for i in range(board_height)])
    ax.xaxis.tick_top()
    ax.set_aspect('equal')

    if save_path:
        fig.savefig(pathlib.Path(save_path))
