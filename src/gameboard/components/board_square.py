from gameboard.components.board_segment import BoardSegment


class BoardSquare:
    """This class represents one of the squares you find on the
    game board. One looks like:

     - 
    | |
     -

    So it is the middle square, with the segments around it as separate objects.

    The purpose of this class is to store the sum data and the related segments.
    """
    def __init__(self, segment_up, segment_down, segment_left, segment_right) -> None:
        self.segment_up: BoardSegment = segment_up
        self.segment_down: BoardSegment = segment_down
        self.segment_left: BoardSegment = segment_left
        self.segment_right: BoardSegment = segment_right
        
    def set_segment_value(self, segment: str, new_value: int | None) -> None:
        """Set value of a segment to 'new_value'.

        Args:
            segment (str): one of ('up', 'down', 'left', 'right')
            value (int | None): one of (None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        """
        if segment == 'up':
            self.segment_up.set_value(new_value)
        elif segment == 'down':
            self.segment_down.set_value(new_value)
        elif segment == 'left':
            self.segment_left.set_value(new_value)
        elif segment == 'right':
            self.segment_right.set_value(new_value)
        else:
            raise ValueError(f'Invalid segment value: "{segment}"')

    def get_all_segments(self):
        """Returns a tuple of all four segments, in order:
        up, down, left, right
        """
        return self.segment_up, self.segment_down, self.segment_left, self.segment_right

    def __str__(self) -> str:
        return f'Square(up={self.segment_up.get_value()}, down={self.segment_down.get_value()}, left={self.segment_left.get_value()}, right={self.segment_right.get_value()})'

    def __repr__(self) -> str:
        return f'Square(up={self.segment_up.get_value()}, down={self.segment_down.get_value()}, left={self.segment_left.get_value()}, right={self.segment_right.get_value()})'
