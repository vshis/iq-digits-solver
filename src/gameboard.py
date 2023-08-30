#  - - - - -
# | | | | | |
#  - - - - -
# | | | | | |
#  - - - - -
# | | | | | |
#  - - - - -
# | | | | | |
#  - - - - -
from segment import Segment


class GameBoard:
    def __init__(self) -> None:
        self.board: list = [[], [], [], [], [], [], [], [], []]
        for index, row in enumerate(self.board):
            if index % 2 == 0:
                for _ in range(5):
                    row.append(Segment('horizontal'))
            else:
                for _ in range(6):
                    row.append(Segment('vertical'))

    # def __str__(self) -> str:
    #     return self.board
    

if __name__ == '__main__':
    board = GameBoard()
    board.board[0][0]

    for index, row in enumerate(board.board):
        if index % 2 == 0:
            print(' ', end='')
            for segment in row:
                print(segment, end=' ')
        else:
            for segment in row:
                print(segment, end=' ')
        print()
