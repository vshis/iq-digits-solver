import sys

sys.path.append('./src/')

from iq_game import BoardGrid


def test_place_one_up(setup_game_state: dict):
    """Tests that one can be placed facing up

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    digit = state['one']

    valid, err_msg = board.place_digit(1, 1, digit, 'up')

    assert valid == True
    assert err_msg == ''
    # check that the correct segments of the board were set
    desired_value = digit.get_value()
    assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
    assert board.get_board()[0][1].get_segment('right').get_value() == desired_value
    assert len(board._placed_values) == 1
    assert board._placed_values == [desired_value]


def test_place_one_down(setup_game_state: dict):
    """Tests that one can be placed facing down

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    digit = state['one']

    valid, err_msg = board.place_digit(1, 1, digit, 'down')

    assert valid == True
    assert err_msg == ''
    # check that the correct segments of the board were set
    desired_value = digit.get_value()
    assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
    assert board.get_board()[2][1].get_segment('left').get_value() == desired_value
    assert len(board._placed_values) == 1
    assert board._placed_values == [desired_value]


def test_place_one_left(setup_game_state: dict):
    """Tests that one can be placed facing up

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    digit = state['one']

    valid, err_msg = board.place_digit(1, 1, digit, 'left')

    assert valid == True
    assert err_msg == ''
    # check that the correct segments of the board were set
    desired_value = digit.get_value()
    assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
    assert board.get_board()[1][0].get_segment('up').get_value() == desired_value
    assert len(board._placed_values) == 1
    assert board._placed_values == [desired_value]


def test_place_one_right(setup_game_state: dict):
    """Tests that one can be placed facing right

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    digit = state['one']

    valid, err_msg = board.place_digit(1, 1, digit, 'right')

    assert valid == True
    assert err_msg == ''
    # check that the correct segments of the board were set
    desired_value = digit.get_value()
    assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
    assert board.get_board()[1][2].get_segment('down').get_value() == desired_value
    assert len(board._placed_values) == 1
    assert board._placed_values == [desired_value]
