# IQ Digits Solver

This is a solver for the IQ Digits game by Smart Games.

Ref: <https://www.smartgames.eu/uk/one-player-games/iq-digits>

## Requirements

- Python >= 3.10.6

For running tests:

- Pytest >= 7.4.3

Install all Python requirements with:

```bash
pip install -r requirements.txt
```

## Reinforcement Learning Solution

### State Space

Initially tackling the challenge without sums in squares.

Board is made up in a 7-segment-style grid and can have different digits placed on it. There are 10 digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) and each can be placed in one of four orientations: up, down, left, right.
Challenge is considered complete when board has all 10 digits placed on it according to the rules, such as:

- Digits cannot overlap.
- Digits cannot cross-over (for example one and seven crossing over in the middle).
- Digits have to fit on the board.

With the different combinations of digits, their orientations and placement on the board, there are countless number of state spaces.

### Action space

Following 810 actions are possible:

- Place digit, given digit, location and orientation.
    - Here, there are 20 board locations, 4 digit orientations and 10 digits.
    - Therefore, we have 20 * 4 * 10 = 800 different actions. 
    - Note that some of these actions will not be useful in practice (like trying to place a digit over another digit).
- Remove digit from board, given digit.
    - Here, there are 10 different digits that can be on the board.
    - So 10 different actions.
- In total there are 810 possible actions.

### Rewards

- Digit placed on board = -1
- Digit removed from board = -1
- Failed attempt to place a digit = -10
- Terminal state reached = +100
