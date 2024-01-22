import sys
import pytest

sys.path.append('./src/')

from iq_game import BoardGrid


class TestPlaceZero:
    def test_place_zero_up(self, setup_game_state: dict):
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


    def test_place_zero_down(self, setup_game_state: dict):
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


    def test_place_zero_left(self, setup_game_state: dict):
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


    def test_place_zero_right(self, setup_game_state: dict):
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


class TestPlaceOne:
    def test_place_one_up(self, setup_game_state: dict):
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


    def test_place_one_down(self, setup_game_state: dict):
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


    def test_place_one_left(self, setup_game_state: dict):
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


    def test_place_one_right(self, setup_game_state: dict):
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


class TestPlaceTwo:
    def test_place_two_up(self, setup_game_state: dict):
        """Tests that two can be placed facing up

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['two']

        valid, err_msg = board.place_digit(1, 1, digit, 'up')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('up').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_two_down(self, setup_game_state: dict):
        """Tests that two can be placed facing down

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['two']

        valid, err_msg = board.place_digit(1, 1, digit, 'down')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('down').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_two_left(self, setup_game_state: dict):
        """Tests that two can be placed facing left

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['two']

        valid, err_msg = board.place_digit(1, 1, digit, 'left')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('left').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_two_right(self, setup_game_state: dict):
        """Tests that two can be placed facing right

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['two']

        valid, err_msg = board.place_digit(1, 1, digit, 'right')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]    


class TestPlaceThree:
    def test_place_three_up(self, setup_game_state: dict):
        """Tests that three can be placed facing up

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['three']

        valid, err_msg = board.place_digit(1, 1, digit, 'up')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('up').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]
        

    def test_place_three_down(self, setup_game_state: dict):
        """Tests that three can be placed facing down

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['three']

        valid, err_msg = board.place_digit(1, 1, digit, 'down')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('down').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_three_left(self, setup_game_state: dict):
        """Tests that three can be placed facing left

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['three']

        valid, err_msg = board.place_digit(1, 1, digit, 'left')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('left').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_three_right(self, setup_game_state: dict):
        """Tests that three can be placed facing right

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['three']

        valid, err_msg = board.place_digit(1, 1, digit, 'right')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


class TestPlaceFour:
    def test_place_four_up(self, setup_game_state: dict):
        """Tests that four can be placed facing up

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['four']

        valid, err_msg = board.place_digit(1, 1, digit, 'up')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('left').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_four_down(self, setup_game_state: dict):
        """Tests that four can be placed facing down

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['four']

        valid, err_msg = board.place_digit(1, 1, digit, 'down')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('left').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_four_left(self, setup_game_state: dict):
        """Tests that four can be placed facing left

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['four']

        valid, err_msg = board.place_digit(1, 1, digit, 'left')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('down').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_four_right(self, setup_game_state: dict):
        """Tests that four can be placed facing right

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['four']

        valid, err_msg = board.place_digit(1, 1, digit, 'right')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('down').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


class TestPlaceFive:
    def test_place_five_up(self, setup_game_state: dict):
        """Tests that five can be placed facing up

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['five']

        valid, err_msg = board.place_digit(1, 1, digit, 'up')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('left').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_five_down(self, setup_game_state: dict):
        """Tests that five can be placed facing down

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['five']

        valid, err_msg = board.place_digit(1, 1, digit, 'down')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_five_left(self, setup_game_state: dict):
        """Tests that five can be placed facing left

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['five']

        valid, err_msg = board.place_digit(1, 1, digit, 'left')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('left').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_five_right(self, setup_game_state: dict):
        """Tests that five can be placed facing right

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['five']

        valid, err_msg = board.place_digit(1, 1, digit, 'right')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


class TestPlaceSix:
    def test_place_six_up(self, setup_game_state: dict):
        """Tests that six can be placed facing up

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['six']

        valid, err_msg = board.place_digit(1, 1, digit, 'up')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('left').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_six_down(self, setup_game_state: dict):
        """Tests that six can be placed facing down

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['six']

        valid, err_msg = board.place_digit(1, 1, digit, 'down')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('down').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_six_left(self, setup_game_state: dict):
        """Tests that six can be placed facing left

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['six']

        valid, err_msg = board.place_digit(1, 1, digit, 'left')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('down').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_six_right(self, setup_game_state: dict):
        """Tests that six can be placed facing right

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['six']

        valid, err_msg = board.place_digit(1, 1, digit, 'right')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


class TestPlaceSeven:
    def test_place_seven_up(self, setup_game_state: dict):
        """Tests that seven can be placed facing up

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['seven']

        valid, err_msg = board.place_digit(1, 1, digit, 'up')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_seven_down(self, setup_game_state: dict):
        """Tests that seven can be placed facing down

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['seven']

        valid, err_msg = board.place_digit(1, 1, digit, 'down')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('down').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_seven_left(self, setup_game_state: dict):
        """Tests that seven can be placed facing left

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['seven']

        valid, err_msg = board.place_digit(1, 1, digit, 'left')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('up').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_seven_right(self, setup_game_state: dict):
        """Tests that seven can be placed facing right

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['seven']

        valid, err_msg = board.place_digit(1, 1, digit, 'right')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


class TestPlaceEight:
    def test_place_eight_up(self, setup_game_state: dict):
        """Tests that eight can be placed facing up

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['eight']

        valid, err_msg = board.place_digit(1, 1, digit, 'up')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_eight_down(self, setup_game_state: dict):
        """Tests that eight can be placed facing down

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['eight']

        valid, err_msg = board.place_digit(1, 1, digit, 'down')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_eight_left(self, setup_game_state: dict):
        """Tests that eight can be placed facing left

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['eight']

        valid, err_msg = board.place_digit(1, 1, digit, 'left')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('down').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_eight_right(self, setup_game_state: dict):
        """Tests that eight can be placed facing right

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['eight']

        valid, err_msg = board.place_digit(1, 1, digit, 'right')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('up').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


class TestPlaceNine:
    def test_place_nine_up(self, setup_game_state: dict):
        """Tests that nine can be placed facing up

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['nine']

        valid, err_msg = board.place_digit(1, 1, digit, 'up')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[0][1].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_nine_down(self, setup_game_state: dict):
        """Tests that nine can be placed facing down

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['nine']

        valid, err_msg = board.place_digit(1, 1, digit, 'down')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[2][1].get_segment('right').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_nine_left(self, setup_game_state: dict):
        """Tests that nine can be placed facing left

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['nine']

        valid, err_msg = board.place_digit(1, 1, digit, 'left')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('up').get_value() == desired_value
        assert board.get_board()[1][0].get_segment('down').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


    def test_place_nine_right(self, setup_game_state: dict):
        """Tests that nine can be placed facing right

        Args:
            setup_game_state (dict): pytest fixture
        """
        state = setup_game_state
        board: BoardGrid = state['board']
        digit = state['nine']

        valid, err_msg = board.place_digit(1, 1, digit, 'right')

        assert valid == True
        assert err_msg == ''
        # check that the correct segments of the board were set
        desired_value = digit.get_value()
        assert board.get_board()[1][1].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('left').get_value() == desired_value
        assert board.get_board()[1][1].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('down').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('right').get_value() == desired_value
        assert board.get_board()[1][2].get_segment('up').get_value() == desired_value
        assert len(board._placed_values) == 1
        assert board._placed_values == [desired_value]


class TestCrossovers:
    """Testing for possible crossing digits (1 and 7).
    """
    def test_place_seven_over_one_up(self, setup_game_state: dict):
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


    def test_place_seven_over_one_down(self, setup_game_state: dict):
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


    def test_place_seven_over_one_left(self, setup_game_state: dict):
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


    def test_place_seven_over_one_right(self, setup_game_state: dict):
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

    def test_place_one_over_seven_up(self, setup_game_state: dict):
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


    def test_place_one_over_seven_down(self, setup_game_state: dict):
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


    def test_place_one_over_seven_left(self, setup_game_state: dict):
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


    def test_place_one_over_seven_right(self, setup_game_state: dict):
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

