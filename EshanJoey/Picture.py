import tkinter as tk
from Hoop import Hoop
from PIL import ImageTk
import time
import math
window = tk.Tk()

canvas = tk.Canvas(window, bg="dark green", height=700, width=800)
image = ImageTk.PhotoImage(file = "EshanJoey/360_F_269004342_YF6N2N5cIfRa74IYNLADSjDMbTrPhY35.jpg")
canvas.create_image(400, 190, image = image)
canvas.create_image(400, 515, image = image)
#canvas.create_image(500, 10, image = image)

canvas.pack()

hoops = Hoop(canvas)
hoopDict ={1:[100,100], 2: [400, 200], 3:[600, 500]}

hoops.draw_hoop(hoopDict[1][0],hoopDict[1][1], "red")
hoops.draw_hoop(hoopDict[2][0],hoopDict[2][1], "blue")
hoops.draw_hoop(hoopDict[3][0],hoopDict[3][1], "purple")

ball=canvas.create_oval(300,400,325,425, fill="black")

def move_ball(power, angle):
    fullPower = 200
    x = int((canvas.coords(ball)[0]))
    y = int((canvas.coords(ball)[1]))
    xGo = x + math.cos(math.radians(angle)) * power * fullPower
    yGo = y + math.sin(math.radians(angle)) * power * fullPower
    m = (yGo - y) / (xGo - x)
    for ho in hoopDict:
        print(ho)
        # if abs(((canvas.coords(ball)[0] + canvas.coords(ball)[2]) / 2) - hoopDict[ho][0] + hoops.width / 2) < 10:
        #     if abs(((canvas.coords(ball)[1] + canvas.coords(ball)[3]) / 2) - hoopDict[ho][1] + hoops.height / 2) < 10:
        #         print("YOU HIT A HOOP")
    while (abs(xGo - x) > 1 or abs(yGo - y) > 1):
        moveX = int(((xGo - x) * .15))
        moveY = int(((yGo - y) * .15))
        if moveX == 0 and xGo > x:
            moveX = 1
        if moveY == 0 and yGo > y:
            moveY = 1
        if moveX == 0 and xGo < x:
            moveX = -1
        if moveY == 0 and yGo < y:
            moveY = -1
        
        canvas.move(ball, moveX, moveY)
        canvas.update()
        x = int((canvas.coords(ball)[0]))
        y = int((canvas.coords(ball)[1]))
        time.sleep(.05)

def task():
    while True:
        power = float(input("power:"))
        angle = float(input("angle:"))
        move_ball(power, angle)
        
        
window.after(1000, task)
window.mainloop()

