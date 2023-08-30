"""Seven segment display, where segments are arranged in grid:
  _a_
 |   |
 f   b
 |_g_|
 |   |
 e   c
 |_d_|

Raises:
    ValueError: when assigning an invalid segment
"""

class SevenSegmentDisplay:
    def __init__(self) -> None:
        self.segments = {}
        for segment in 'abcdefg':
            self.segments[segment] = False

    def set_segment_state(self, segment: str, state: bool):
        if segment in self.segments:
            self.segments[segment] = state
        else:
            raise ValueError(f'Invalid value for segment: {segment}')
    
    def get_segment_state(self, segment: str):
        if segment in self.segments:
            return self.segments[segment]
        else:
            raise ValueError(f'Invalid value for segment: {segment}')
            
    def clear(self):
        for segment in self.segments:
            self.segments[segment] = False

    def display(self):
        if self.segments['a']:
            print(" _ ")
        
        if self.segments['f'] and self.segments['g'] and self.segments['b']:
            print("|_|")
        elif self.segments['f'] and self.segments['g']:
            print("|_ ")
        elif self.segments['b'] and self.segments['g']:
            print(" _|")
        elif self.segments['g']:
            print(" _ ")
        elif self.segments['f']:
            print("|  ")
        elif self.segments['b']:
            print("  |")
        
        if self.segments['e'] and self.segments['d'] and self.segments['c']:
            print("|_|")
        elif self.segments['e'] and self.segments['d']:
            print("|_ ")
        elif self.segments['c'] and self.segments['d']:
            print(" _|")
        elif self.segments['d']:
            print(" _ ")
        elif self.segments['e']:
            print("|  ")
        elif self.segments['c']:
            print("  |")
    
    def __str__(self):
        output: str = ''
        if self.segments['a']:
            output += " _ " + "\n"
        
        if self.segments['f'] and self.segments['g'] and self.segments['b']:
            output += "|_|" + "\n"
        elif self.segments['f'] and self.segments['g']:
            output += "|_ " + "\n"
        elif self.segments['b'] and self.segments['g']:
            output += " _|" + "\n"
        elif self.segments['g']:
            output += " _ " + "\n"
        elif self.segments['f']:
            output += "|  " + "\n"
        elif self.segments['b']:
            output += "  |" + "\n"
        
        if self.segments['e'] and self.segments['d'] and self.segments['c']:
            output += "|_|"
        elif self.segments['e'] and self.segments['d']:
            output += "|_ "
        elif self.segments['c'] and self.segments['d']:
            output += " _|"
        elif self.segments['d']:
            output += " _ "
        elif self.segments['e']:
            output += "|  "
        elif self.segments['c']:
            output += "  |"
        
        return output

    
if __name__ == '__main__':
    display = SevenSegmentDisplay()
    display.set_segment_state('a', True)
    display.set_segment_state('b', True)
    # display.set_segment('c', True)
    display.set_segment_state('d', True)
    display.set_segment_state('e', True)
    # display.set_segment('f', True)
    display.set_segment_state('g', True)
    print(display)
            