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
    