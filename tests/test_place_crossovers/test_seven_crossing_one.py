import sys

sys.path.append('./src/')

from iq_game import BoardGrid


def test_place_seven_over_one_up(setup_game_state: dict):
    """Tests that invalid placement is returned if seven is placed over one, 
    such that when they cross over, seven is facing up.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid_one, _ = board.place_digit(1, 1, state['one'], 'left')
    valid_seven, _ = board.place_digit(1, 0, state['seven'], 'up')

    assert valid_one == True
    assert valid_seven == False


def test_place_seven_over_one_down(setup_game_state: dict):
    """Tests that invalid placement is returned if seven is placed over one, 
    such that they cross over, with seven oriented down.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid_one, _ = board.place_digit(1, 1, state['one'], 'left')
    valid_seven, _ = board.place_digit(0, 1, state['seven'], 'down')

    assert valid_one == True
    assert valid_seven == False


def test_place_seven_over_one_left(setup_game_state: dict):
    """Tests that invalid placement is returned if seven is placed over one, 
    such that they cross over, with seven oriented left.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid_one, _ = board.place_digit(1, 1, state['one'], 'up')
    valid_seven, _ = board.place_digit(1, 2, state['seven'], 'left')

    assert valid_one == True
    assert valid_seven == False


def test_place_seven_over_one_right(setup_game_state: dict):
    """Tests that invalid placement is returned if seven is placed over one, 
    such that they cross over, with seven oriented right.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid_one, _ = board.place_digit(1, 1, state['one'], 'up')
    valid_seven, _ = board.place_digit(0, 1, state['seven'], 'right')

    assert valid_one == True
    assert valid_seven == False
