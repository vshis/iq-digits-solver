import sys

sys.path.append('./src/')

from iq_game import BoardGrid


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
    assert board.is_terminal()


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


def test_remove_digit_from_board(setup_game_state: dict):
    """Tests that a digit is removed from board.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    digit = state['eight']
    board.place_digit(1, 1, digit, 'up')
    board.remove_digit(digit)
    desired_value = None
    assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
    assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
    assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
    assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
    assert board.get_board()[0][1].get_segment('up').get_value() == desired_value
    assert board.get_board()[0][1].get_segment('left').get_value() == desired_value
    assert board.get_board()[0][1].get_segment('right').get_value() == desired_value
    assert len(board._placed_values) == 0   


def test_remove_digit_from_board_with_multiple_digits(setup_game_state: dict):
    """Tests that a digit is removed from board where multiple digits are present.

    Args:
        setup_game_state (dict): pytest fixture
    """
    state = setup_game_state
    board: BoardGrid = state['board']
    digit = state['zero']
    board.place_digit(3, 3, state['one'], 'up')
    board.place_digit(1, 1, digit, 'up')
    board.remove_digit(digit)

    assert board.get_board()[1][1].get_segment('up').get_value() == None
    assert board.get_board()[1][1].get_segment('left').get_value() == None
    assert board.get_board()[1][1].get_segment('right').get_value() == None
    assert board.get_board()[1][1].get_segment('down').get_value() == None

    assert board.get_board()[3][3].get_segment('right').get_value() == 1
    assert board.get_board()[2][3].get_segment('right').get_value() == 1

    assert len(board._placed_values) == 1
    assert board._placed_values == [1]
