class BoardSegment:
    """This class defines a segment as an object that either has 
    a value associated with it or is None. It is used to construct
    the spaces on the board where numbers can go, assigning to 
    board squares.
    """
    def __init__(self, value: int | None = None) -> None:
        """Construct a segment object with no value by default.
        Value can take any of the following: 
        [None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        Args:
            value (int | None, optional): Value of this segment. 
            Defaults to None.
        """
        self._valid_values = (None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self._value = value

    def occupied(self) -> bool:
        """Returns whether this segment is occupied (has a value).

        Returns:
            bool: True if occupied, else, False.
        """
        if self._value:
            return True
        return False
    
    def get_value(self) -> int | None:
        return self._value
    
    def set_value(self, new_value: int | None) -> None:
        if new_value in self._valid_values:
            self._value = new_value
        else:
            raise ValueError(
                f'New value {new_value} not in valid values: {self._valid_values}'
                )
