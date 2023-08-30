from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import os

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
    None: '#575c58'
}

board: GameBoard = GameBoard()
board.board[0][0].set_value(5)

vertices = []
codes = []
colors = []

for row_idx, row in enumerate(board.board):
    row_idx = row_idx//2 * -1
    for segment_idx, segment in enumerate(row):
        codes.append([Path.MOVETO, Path.LINETO])
        colors.append(color_mapping[segment.get_value()])
        vert_temp = []
        vert_temp += [(segment_idx, row_idx)]
        if segment.get_direction() == 'horizontal':
            vert_temp += [(segment_idx + 1, row_idx)]
        else:
            vert_temp += [(segment_idx, row_idx - 1)]
        vertices.append(vert_temp)

# vertices += [[(1, 1), (2, 1)], [(1, 2), (2, 2)]]
# codes += [[Path.MOVETO, Path.LINETO], [Path.MOVETO, Path.LINETO]]
# colors = ['red', 'orange']
pathpatches = [PathPatch(Path(vertices[i], codes[i]), edgecolor=colors[i], linewidth=5) for i in range(len(vertices))]

collection = PatchCollection(pathpatches, match_original=True)

fig, ax = plt.subplots()
ax.add_collection(collection)
ax.autoscale_view()

save_path = os.path.abspath(os.path.dirname(__file__))
plt.savefig(os.path.join(save_path, "output.png"))


