


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
        self.segment_up = segment_up
        self.segment_down = segment_down
        self.segment_left = segment_left
        self.segment_right = segment_right
        self.segments = [
            self.segment_up, 
            self.segment_down,
            self.segment_left,
            self.segment_right
            ]

    def __str__(self) -> str:
        return f'Square(up={self.segment_up.get_value()}, down={self.segment_down.get_value()}, left={self.segment_left.get_value()}, right={self.segment_right.get_value()})'

    def __repr__(self) -> str:
        return f'Square(up={self.segment_up.get_value()}, down={self.segment_down.get_value()}, left={self.segment_left.get_value()}, right={self.segment_right.get_value()})'
