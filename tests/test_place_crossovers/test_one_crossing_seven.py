import sys

sys.path.append('./src/')

from iq_game import BoardGrid


def test_place_one_over_seven_up(setup_game_state: dict):
    """Tests that invalid placement is returned if one is placed over seven, 
    such that when they cross over, one is facing up.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    valid_seven, _ = board.place_digit(1, 1, state['seven'], 'left')
    valid_one, _ = board.place_digit(1, 0, state['one'], 'up')

    assert valid_seven == True
    assert valid_one == False


def test_place_one_over_seven_down(setup_game_state: dict):
    """Tests that invalid placement is returned if one is placed over seven, 
    such that they cross over, with one oriented down.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid_seven, _ = board.place_digit(1, 1, state['seven'], 'right')
    valid_one, _ = board.place_digit(1, 2, state['one'], 'down')

    assert valid_seven == True
    assert valid_one == False


def test_place_one_over_seven_left(setup_game_state: dict):
    """Tests that invalid placement is returned if one is placed over seven, 
    such that they cross over, with one oriented left.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid_seven, _ = board.place_digit(1, 1, state['seven'], 'up')
    valid_one, _ = board.place_digit(1, 2, state['one'], 'left')
    
    assert valid_seven == True
    assert valid_one == False


def test_place_one_over_seven_right(setup_game_state: dict):
    """Tests that invalid placement is returned if one is placed over seven, 
    such that they cross over, with one oriented right.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid_seven, _ = board.place_digit(1, 1, state['seven'], 'down')
    valid_one, _ = board.place_digit(1, 0, state['one'], 'right')

    assert valid_seven == True
    assert valid_one == False
