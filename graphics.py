from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self,width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white",height=height,width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_window_running = True

        while self.is_window_running:
            self.redraw()
    
    def close(self):
        self.is_window_running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas,fill_color)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.first_point.x,self.first_point.y,self.second_point.x,self.second_point.y, fill=fill_color,width=2)