import sys

sys.path.append('./src/')

from gameboard import BoardGrid


def test_place_all_digits(setup_game_state: dict):
    """Tests that all digits can be placed on the board, given valid placements

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valids = []
    valids.append(board.place_digit(0, 0, state['eight'], 'down')[0])
    valids.append(board.place_digit(2, 0, state['five'], 'right')[0])
    valids.append(board.place_digit(3, 1, state['six'], 'left')[0])
    valids.append(board.place_digit(0, 2, state['four'], 'left')[0])
    valids.append(board.place_digit(2, 2, state['nine'], 'up')[0])
    valids.append(board.place_digit(3, 2, state['one'], 'right')[0])
    valids.append(board.place_digit(1, 3, state['three'], 'up')[0])
    valids.append(board.place_digit(1, 4, state['seven'], 'up')[0])
    valids.append(board.place_digit(2, 4, state['zero'], 'left')[0])
    valids.append(board.place_digit(3, 4, state['two'], 'left')[0])
    
    assert len(valids) == 10
    assert all(valids)


def test_place_digit_out_of_grid_bounds(setup_game_state: dict):
    """Tests that invalid placement is returned if digit is placed outside of board bounds.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid, _ = board.place_digit(0, 0, state['five'], 'up')
    assert valid == False
    valid, _ = board.place_digit(10, 543, state['four'], 'up')
    assert valid == False
    assert len(board._placed_values) == 0


def test_place_digit_on_top_of_another(setup_game_state: dict):
    """Tests that invalid placement is returned if digit is placed on top of another

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    board.place_digit(1, 1, state['five'], 'up')
    valid, _ = board.place_digit(3, 1, state['two'], 'up')

    assert valid == False
    assert len(board._placed_values) == 1


def test_place_seven_over_one_up(setup_game_state: dict):
    """Tests that invalid placement is returned if seven is placed over one, 
    such that they cross over, with one oriented up.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid_one, _ = board.place_digit(1, 0, state['one'], 'up')
    valid_seven, _ = board.place_digit(1, 1, state['seven'], 'left')

    assert valid_one == True
    assert valid_seven == False


def test_place_seven_over_one_down(setup_game_state: dict):
    """Tests that invalid placement is returned if seven is placed over one, 
    such that they cross over, with one oriented down.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid_one, _ = board.place_digit(1, 1, state['one'], 'down')
    valid_seven, _ = board.place_digit(2, 1, state['seven'], 'left')

    assert valid_one == True
    assert valid_seven == False


def test_place_one_over_seven(setup_game_state: dict):
    """Tests that invalid placement is returned if seven is placed over one, 
    such that they cross over.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']

    valid_seven, _ = board.place_digit(1, 1, state['seven'], 'left')
    valid_one, _ = board.place_digit(1, 0, state['one'], 'up')

    assert valid_seven == True
    assert valid_one == False
