"""Seven segment display, where segments are arranged in grid:
x (columns): 0 1 2
y (rows): 0 1 2 3 4
    0 1 2
    _____
0|  . a .
1|  f . b
2|  . g .
3|  e . c
4|  . d .

Raises:
    ValueError: when assigning an invalid segment
"""

class SevenSegmentDisplay:
    def __init__(self) -> None:
        self.segments = {
            'a': {'state': False, 'col': 1, 'row': 0},
            'b': {'state': False, 'col': 2, 'row': 1},
            'c': {'state': False, 'col': 2, 'row': 3},
            'd': {'state': False, 'col': 1, 'row': 4},
            'e': {'state': False, 'col': 0, 'row': 3},
            'f': {'state': False, 'col': 0, 'row': 1},
            'g': {'state': False, 'col': 1, 'row': 2},
            }
        self.grid = []
        

    def set_segment(self, segment: str, state: bool):
        if segment in self.segments:
            self.segments[segment]['state'] = state
        else:
            raise ValueError(f'Invalid value for segment: {segment}')
    
    def display(self):
        ...
            
    def clear(self):
        for segment in self.segments:
            self.segments[segment] = False

    
if __name__ == '__main__':
    display = SevenSegmentDisplay()
    display.set_segment('a', True)
    display.set_segment('b', True)
    # display.set_segment('c', True)
    display.set_segment('d', True)
    display.set_segment('e', True)
    # display.set_segment('f', True)
    display.set_segment('g', True)
    display.display()
    print(display.segments)
            