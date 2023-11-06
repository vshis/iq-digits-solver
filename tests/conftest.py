import pytest
import sys

sys.path.append('./src/')

from iq_game import BoardGrid
from iq_game.digits import Zero, One, Seven, Two, Three, Four, Five, Six, Eight, Nine, Digit


@pytest.fixture
def setup_game_state():
    """Sets up initial game state. 

    Yields a tuple of (board, *digits), where digits are the digit objects zero-nine.
    """
    initial_state = {}
    initial_state['board'] = BoardGrid(width=5, height=4)
    initial_state['zero'] = Zero()
    initial_state['one'] = One()
    initial_state['two'] = Two()
    initial_state['three'] = Three()
    initial_state['four'] = Four()
    initial_state['five'] = Five() 
    initial_state['six'] = Six()
    initial_state['seven'] = Seven()
    initial_state['eight'] = Eight()
    initial_state['nine'] = Nine()
    yield initial_state