from gameboard.components import BoardSegment, BoardSquare


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