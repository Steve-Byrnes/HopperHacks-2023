
class Hoop:
    def __init__(self, canvas):
        self.canvas = canvas
        self.height = 50
        self.pipeWidth = 5
        self.width = 35
        
    def draw_hoop(self, x, y, color):
        self.canvas.create_line(x,y,x,y - self.height*.8, fill="white", width=self.pipeWidth)
        self.canvas.create_line(x,y - self.height*.8,x,y - self.height, fill=color, width=self.pipeWidth)
        self.canvas.create_line(x- self.width,y,x - self.width,y - self.height * .8, fill="white", width=self.pipeWidth)
        self.canvas.create_line(x- self.width,y - self.height*.8,x - self.width,y - self.height, fill=color, width=self.pipeWidth)
        self.canvas.create_line(x - self.width * 1.2, y- self.height, x + self.width * .2, y-self.height, fill=color, width=self.pipeWidth)
    