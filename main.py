from graphics import Window
from maze import Maze

def main():
    win = Window(800,600)
    
    """ c1 = Cell(win)
    c1.draw(50, 60, 100, 200)

    c2 = Cell(win)
    c2.draw(500,700,210,350)

    c1.draw_move(c2,True) """

    maze = Maze(0,0,10,12,10,10,win)

    win.wait_for_close()

main()