import sys

sys.path.append('./src/')

from gameboard import BoardGrid


def test_place_zero_up(setup_game_state: dict):
    """Tests that zero can be placed facing up

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    digit = state['zero']

    valid, err_msg = board.place_digit(0, 0, digit, 'up')

    assert valid == True
    assert err_msg == ''
    # check that the correct segments of the board were set to 0
    desired_value = digit.get_value()
    assert board.get_board()[0][0].get_segment('up').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('down').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('left').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('right').get_value() == desired_value
    assert len(board._placed_values) == 1
    assert board._placed_values == [desired_value]


def test_place_zero_down(setup_game_state: dict):
    """Tests that zero can be placed facing down

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    digit = state['zero']

    valid, err_msg = board.place_digit(0, 0, digit, 'down')

    assert valid == True
    assert err_msg == ''
    # check that the correct segments of the board were set to 0
    desired_value = digit.get_value()
    assert board.get_board()[0][0].get_segment('up').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('down').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('left').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('right').get_value() == desired_value
    assert len(board._placed_values) == 1
    assert board._placed_values == [desired_value]


def test_place_zero_left(setup_game_state: dict):
    """Tests that zero can be placed facing left

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    digit = state['zero']

    valid, err_msg = board.place_digit(0, 0, digit, 'left')

    assert valid == True
    assert err_msg == ''
    # check that the correct segments of the board were set to 0
    desired_value = digit.get_value()
    assert board.get_board()[0][0].get_segment('up').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('down').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('left').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('right').get_value() == desired_value
    assert len(board._placed_values) == 1
    assert board._placed_values == [desired_value]


def test_place_zero_right(setup_game_state: dict):
    """Tests that zero can be placed facing right

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    digit = state['zero']

    valid, err_msg = board.place_digit(0, 0, digit, 'right')

    assert valid == True
    assert err_msg == ''
    # check that the correct segments of the board were set to 0
    desired_value = digit.get_value()
    assert board.get_board()[0][0].get_segment('up').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('down').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('left').get_value() == desired_value
    assert board.get_board()[0][0].get_segment('right').get_value() == desired_value
    assert len(board._placed_values) == 1
    assert board._placed_values == [desired_value]
