from cell import Cell
import time

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for i in range(self._num_cols):
            row = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                row.append(cell)
                self._draw_cell(i,j,cell)
            self._cells.append(row)
        

    def _draw_cell(self, i ,j,cell):
        if self._win is None:
            return
        x1 = (j * self._cell_size_x) + self._x1
        y1 = (i * self._cell_size_y) + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell.draw(x1,x2,y1,y2)

        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.5)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0,self._cells[0][0])
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(len(self._cells) - 1 ,len(self._cells[0]) - 1,self._cells[-1][-1])
