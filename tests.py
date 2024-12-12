import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(100,100, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False
        )

    def test_random_seed(self):
        """Test that the maze generation produces the same result with the same seed."""
        num_cols = 4
        num_rows = 4
        maze1 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=42)
        maze2 = Maze(0, 0, num_rows, num_cols, 10, 10, seed=42)

        # Check that both mazes are identical by comparing their cell wall states
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertEqual(maze1._cells[i][j].has_left_wall, maze2._cells[i][j].has_left_wall)
                self.assertEqual(maze1._cells[i][j].has_right_wall, maze2._cells[i][j].has_right_wall)
                self.assertEqual(maze1._cells[i][j].has_top_wall, maze2._cells[i][j].has_top_wall)
                self.assertEqual(maze1._cells[i][j].has_bottom_wall, maze2._cells[i][j].has_bottom_wall)

    def test_no_redundant_walls(self):
        """Test that no redundant walls are present (walls between visited cells should be removed)."""
        num_cols = 3
        num_rows = 3
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Verify that for each pair of adjacent cells, their shared wall has been removed
        for i in range(num_cols):
            for j in range(num_rows):
                if i < num_cols - 1:
                    self.assertTrue(maze._cells[i][j].has_right_wall == maze._cells[i + 1][j].has_left_wall)
                if j < num_rows - 1:
                    self.assertTrue(maze._cells[i][j].has_bottom_wall == maze._cells[i][j + 1].has_top_wall)

    def test_maze_reset_cells_visited(self):
        num_cols = 10
        num_rows = 12
        maze = Maze(0,0,num_rows,num_cols,10,10)

        for row in maze._cells:
            for cell in row:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()