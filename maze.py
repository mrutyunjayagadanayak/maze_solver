from math import trunc

from cell import Cell
import time
import random

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
            seed =None ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

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
        #time.sleep(0.5)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0,self._cells[0][0])
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(len(self._cells) - 1 ,len(self._cells[0]) - 1,self._cells[-1][-1])

    def _break_walls_r(self, i , j):
        self._cells[i][j].visited = True

        while True:
            next_val_list = []

            if i > 0 and not self._cells[i - 1][j].visited:
                next_val_list.append((i - 1,j))

            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_val_list.append((i + 1,j))

            if j > 0 and not self._cells[i][j - 1].visited:
                next_val_list.append((i, j - 1))

            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_val_list.append((i, j + 1))

            if len(next_val_list) == 0:
                self._draw_cell(i,j, self._cells[i][j])
                return

            direction_index = random.randrange(len(next_val_list))
            next_index = next_val_list[direction_index]

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self,i,j):
        self._animate()

        self._cells[i][j].visited = True
        end_cell = self._cells[-1][-1]


        if end_cell == self._cells[i][j]:
            return True
            # move left if there is no wall and it hasn't been visited
        if (
                i > 0
                and not self._cells[i][j].has_left_wall
                and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
                i < self._num_cols - 1
                and not self._cells[i][j].has_right_wall
                and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
                j > 0
                and not self._cells[i][j].has_top_wall
                and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
                j < self._num_rows - 1
                and not self._cells[i][j].has_bottom_wall
                and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False
