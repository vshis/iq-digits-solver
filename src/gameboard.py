#  - - - - -
# | | | | | |
#  - - - - -
# | | | | | |
#  - - - - -
# | | | | | |
#  - - - - -
# | | | | | |
#  - - - - -
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import os
from typing import Literal, Tuple

from digits.segment import Segment


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



class GameBoard:
    def __init__(self) -> None:
        self.board: list = [[], [], [], [], [], [], [], [], []]
        for index, row in enumerate(self.board):
            if index % 2 == 0:
                for _ in range(5):
                    row.append(Segment('horizontal'))
            else:
                for _ in range(6):
                    row.append(Segment('vertical'))

    def draw(self, save_file_name: str = None):
        """Draws the current state of the game board and returns the fig, ax.

        Optionally, if a save_file_name is provided as a string, saves the 
        image to disk, in the same dir as this .py file.

        Args:
            save_file_name (str, optional): file name to save the game board image state to, 
            without extension. None to not save. Defaults to None.  

        Returns:
            Figure: instance of matplotlib Figure, containing the game board plot.
            Axes: instance of matplotlib pyplot Axes, containing the game board plot.
        """
        vertices = []
        codes = []
        colors = []

        for row_idx, row in enumerate(board.board):
            row_idx = row_idx//2 * -1
            for segment_idx, segment in enumerate(row):
                codes.append([Path.MOVETO, Path.LINETO])
                colors.append(COLOR_MAPPING[segment.get_value()])
                vert_temp = []
                vert_temp += [(segment_idx, row_idx)]
                if segment.get_direction() == 'horizontal':
                    vert_temp += [(segment_idx + 1, row_idx)]
                else:
                    vert_temp += [(segment_idx, row_idx - 1)]
                vertices.append(vert_temp)

        pathpatches = [PathPatch(Path(vertices[i], codes[i]), edgecolor=colors[i], linewidth=10) for i in range(len(vertices))]

        collection = PatchCollection(pathpatches, match_original=True)

        fig, ax = plt.subplots()

        ax.add_collection(collection)
        ax.autoscale_view()
        ax.set_xticks([i + 0.5 for i in range(5)], labels=[str(i) for i in range(5)])
        ax.set_yticks([-1 * i/2 for i in range(9)], labels=[str(i) for i in range(9)])
        ax.xaxis.tick_top()

        if save_file_name:
            save_path = os.path.abspath(os.path.dirname(__file__))
            save_file_path = os.path.join(save_path, f"{save_file_name}.png")
            fig.savefig(save_file_path)

        return fig, ax

    def __str__(self) -> str:
        output = ''
        for index, row in enumerate(board.board):
            # row of horizontal segments
            if index % 2 == 0:
                output += ' '
                for segment in row:
                    output += str(segment) + ' '
            # row of vertical segments
            else:
                for segment in row:
                    output += str(segment) + ' '
            output += '\n'
        return output
    
    def place_digit(self, digit: int, location: Tuple[int, int], direction: Literal['down', 'right', 'left', 'up']) -> None:
        
        pass
    

def place_segment(digit_segment: Segment, current_location: Tuple[int, int]):
    try:
        current_board_segment: Segment = board.board[current_location[0]][current_location[1]]
    except IndexError:
        raise IndexError(f"Cannot place digit {digit_segment.get_value()}. Selected placement is out of grid bounds: {current_location}")

    if current_board_segment.get_value() is not None and digit_segment.get_value() is not None:
        raise ValueError(f'Cannot place digit {digit_segment.get_value()}. Segment at location {current_location} is occupied by: {current_board_segment}')
    elif current_board_segment.get_direction() != digit_segment.get_direction():
        raise ValueError(f'Cannot place digit {digit_segment.get_value()}. {current_board_segment.get_direction().capitalize()} segment at location {current_location} does not match the direction of the {digit_segment.get_direction()} digit segment.')
    else:
        current_board_segment.set_value(digit_segment.get_value())


if __name__ == '__main__':
    board = GameBoard()

    from digits.zero import Zero
    from digits.one import One
    zero = Zero()
    one = One()
    
    start_location = (1,3)  # row, col
    current_location = start_location
    direction = 'right'
    digit = zero
    
    if direction == 'down':
        for row in digit.get_grid(direction=direction):
            for digit_segment in row:
                place_segment(digit_segment, current_location)
                # try:
                #     current_board_segment: Segment = board.board[current_location[0]][current_location[1]]
                # except IndexError:
                #     raise IndexError(f"Cannot place digit {digit_segment.get_value()}. Selected placement is out of grid bounds: {current_location}")

                # if current_board_segment.get_value() is not None and digit_segment.get_value() is not None:
                #     raise ValueError(f'Cannot place digit {digit_segment.get_value()}. Segment at location {current_location} is occupied by: {current_board_segment}')
                # elif current_board_segment.get_direction() != digit_segment.get_direction():
                #     raise ValueError(f'Cannot place digit {digit_segment.get_value()}. {current_board_segment.get_direction().capitalize()} segment at location {current_location} does not match the direction of the {digit_segment.get_direction()} digit segment.')
                # else:
                #     current_board_segment.set_value(digit_segment.get_value())

                # go to next column
                current_location = (current_location[0], current_location[1] + 1)
            # go to next row, refresh column back to start
            current_location = (current_location[0] + 1, start_location[1])

    elif direction == 'right':
        for column_index, column in enumerate(digit.get_grid(direction=direction)):
            # for vertical columns 
            if column_index % 2 == 0:
                for digit_segment in column:
                    place_segment(digit_segment, current_location)
                    # try:
                    #     current_board_segment: Segment = board.board[current_location[0]][current_location[1]]
                    # except IndexError:
                    #     raise IndexError(f"Cannot place digit {digit_segment.get_value()}. Selected placement is out of grid bounds: {current_location}")

                    # if current_board_segment.get_value() is not None and digit_segment.get_value() is not None:
                    #     raise ValueError(f'Cannot place digit {digit_segment.get_value()}. Segment at location {current_location} is occupied by: {current_board_segment}')
                    # elif current_board_segment.get_direction() != digit_segment.get_direction():
                    #     raise ValueError(f'Cannot place digit {digit_segment.get_value()}. {current_board_segment.get_direction().capitalize()} segment at location {current_location} does not match the direction of the {digit_segment.get_direction()} digit segment.')
                    # else:
                    #     current_board_segment.set_value(digit_segment.get_value())

                    # go to next row
                    current_location = (current_location[0] + 1, current_location[1])
            # for horizontal columns
            else:
                current_location = (start_location[0] - 1, current_location[1])
                for digit_segment in column:
                    place_segment(digit_segment, current_location)
                    # try:
                    #     current_board_segment: Segment = board.board[current_location[0]][current_location[1]]
                    # except IndexError:
                    #     raise IndexError(f"Cannot place digit {digit_segment.get_value()}. Selected placement is out of grid bounds: {current_location}")

                    # if current_board_segment.get_value() is not None and digit_segment.get_value() is not None:
                    #     raise ValueError(f'Cannot place digit {digit_segment.get_value()}. Segment at location {current_location} is occupied by: {current_board_segment}.')
                    # elif current_board_segment.get_direction() != digit_segment.get_direction():
                    #     raise ValueError(f'Cannot place digit {digit_segment.get_value()}. {current_board_segment.get_direction().capitalize()} segment at location {current_location} does not match the direction of the {digit_segment.get_direction()} digit segment.')
                    # else:
                    #     current_board_segment.set_value(digit_segment.get_value())

                    # go to next row
                    current_location = (current_location[0] + 2, current_location[1])
                # go to next column, refresh row back to start
                current_location = (start_location[0], current_location[1] + 1)
    
    board.draw(save_file_name='output')

    # for index, row in enumerate(self.board):
    #     if index % 2 == 0:
    #         for _ in range(5):
    #             row.append(Segment('horizontal'))
    #     else:
    #         for _ in range(6):
    #             row.append(Segment('vertical'))
