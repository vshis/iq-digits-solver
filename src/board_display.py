from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt

from gameboard import GameBoard
from segment import Segment

color_mapping = {
    0: '#ff0533',
    1: '#ffc105',
    2: '#fbff05',
    3: '#c9ff05',
    4: '#0a9100',
    5: '#d9fbff',
    6: '#07abf7',
    7: '#0234bf',
    8: '#4d02b0',
    9: '#f73bf4',
}

board: GameBoard = GameBoard()
board.board[0][0].set_value(5)

vertices = []
codes = []

for row_idx, row in enumerate(board.board):
    row_idx = row_idx//2 * -1
    for segment_idx, segment in enumerate(row):
        codes += [Path.MOVETO]
        codes += [Path.LINETO]
        vertices += [(segment_idx, row_idx)]
        if segment.get_direction() == 'horizontal':
            vertices += [(segment_idx + 1, row_idx)]
        else:
            vertices += [(segment_idx, row_idx - 1)]

# vertices += [(1, 1), (2, 1), (1, 2), (2, 2)]
# codes += [Path.MOVETO, Path.LINETO, Path.MOVETO, Path.LINETO]

path = Path(vertices, codes)
pathpatch = PathPatch(path, facecolor='none', edgecolor='grey', linewidth=2)

fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.autoscale_view()
plt.savefig("x.png")
