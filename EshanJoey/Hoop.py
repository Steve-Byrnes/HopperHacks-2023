
class Hoop:
    def __init__(self, canvas):
        self.canvas = canvas
        self.height = 65
        self.pipeWidth = 8
        self.width = 50
        
    def draw_hoop(self, x, y, color):
        #f.canvas.create_line(x,y,x,y - self.height*.8, fill="white", width=self.pipeWidth,outline='black')
        # self.canvas.create_line(x,y - self.height*.8,x,y - self.height, fill=color, width=self.pipeWidth, outline='black')
        # self.canvas.create_line(x- self.width,y,x - self.width,y - self.height * .8, fill="white", width=self.pipeWidth, outline='black')
        # self.canvas.create_line(x- self.width,y - self.height*.8,x - self.width,y - self.height, fill=color, width=self.pipeWidth, outline='black')
        # self.canvas.create_line(x - self.width * 1.2, y- self.height, x + self.width * .2, y-self.height, fill=color, width=self.pipeWidth, outline='black')
        self.canvas.create_rectangle(x,y,x + self.pipeWidth,y - self.height*.8, fill="white",outline='black')
        self.canvas.create_rectangle(x,y - self.height*.8,x+ self.pipeWidth,y - self.height, fill=color,outline='black')
        self.canvas.create_rectangle(x- self.width,y,x - self.width + self.pipeWidth,y - self.height * .8, fill="white",outline='black')
        self.canvas.create_rectangle(x- self.width,y - self.height*.8,x - self.width + self.pipeWidth,y - self.height, fill=color,outline='black')
        self.canvas.create_rectangle(x - self.width * 1.05, y- self.height, x + self.width * .2, y-self.height + self.pipeWidth, fill=color,outline='black')

      