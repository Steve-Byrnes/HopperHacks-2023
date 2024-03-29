import tkinter as tk
from Hoop import Hoop
from PIL import ImageTk
import time
import math
from datetime import datetime

from tracking.tracking import tracking
window = tk.Tk()

canvas = tk.Canvas(window, bg="dark green", height=700, width=800)
image = ImageTk.PhotoImage(file = "EshanJoey/IMG_1686.JPG")
canvas.create_image(400, 350, image = image)
#canvas.create_image(400, 190, image = image)
#canvas.create_image(500, 10, image = image)

canvas.pack()

hoops = Hoop(canvas)
hoopDict ={1:[100,600], 2: [400, 350], 3:[600, 500]}

shadow=canvas.create_oval(295,432,330,437, fill="#222")
ball=canvas.create_oval(300,400,335,435, fill="white", stipple='gray25', outline='black', width='3')

hoops.draw_hoop(hoopDict[1][0],hoopDict[1][1], "red")
hoops.draw_hoop(hoopDict[2][0],hoopDict[2][1], "blue")
hoops.draw_hoop(hoopDict[3][0],hoopDict[3][1], "purple")
ballColor = True

score = 0
scoreText = canvas.create_text(700, 650, text="Score: 0", fill="black", font=('Helvetica 30 bold'))

hits = 0
hitsText = canvas.create_text(700, 600, text="Hits: 0", fill="black", font=('Helvetica 30 bold'))


def move_ball(power:float, angle:int) -> None: 
    gotPoint = False
    global ballColor
    global score
    fullPower = 200
    #print("hello")
    #print(power)
    x = int((canvas.coords(ball)[0]))
    y = int((canvas.coords(ball)[1]))
    
    xGo = round(x + math.cos(math.radians(angle)) * power * fullPower, 0)
    yGo = round(y + math.sin(math.radians(angle)) * power * fullPower, 0)
    sum = abs(x - xGo) + abs(y - yGo)
    
    if xGo < 50: 
        xGo = 50
    elif xGo > 750:
        xGo = 750
    if yGo < 185:
        yGo = 185
    elif yGo > 650:
        yGo = 650
    vert = False
    # print("x:" + str(x))
    # print("xGo:" + str(xGo))
    if xGo == x:
        vert = True
    else:
        m = (yGo - y) / (xGo - x)
        b = y - (m * x)
        #print("y=" + str(m) + "x + " + str(b))

    for ho in hoopDict:
        if vert:
            xball = x
            # print(xball)
            # print(hoopDict[ho][0])
            # print(hoopDict[ho][0] - hoops.width)
            if xball > hoopDict[ho][0] - hoops.width and xball < hoopDict[ho][0]:
                #print(hoopDict[ho][1])
                if angle == 270 and hoopDict[ho][1] > yGo and hoopDict[ho][1] < y:
                    gotPoint = True
                elif angle == 90 and hoopDict[ho][1] < yGo and hoopDict[ho][1] > y:
                    gotPoint = True

        else:   
            if m != 0:
                xball = abs((hoopDict[ho][1] - b) / m)
                # print(xball)
                # print(hoopDict[ho][0])
                # print(hoopDict[ho][0] + hoops.width)
                if xball > hoopDict[ho][0] - hoops.width and xball < hoopDict[ho][0]:
                    gotPoint = True
        # if abs(((canvas.coords(ball)[0] + canvas.coords(ball)[2]) / 2) - hoopDict[ho][0] + hoops.width / 2) < 10:
        #     if abs(((canvas.coords(ball)[1] + canvas.coords(ball)[3]) / 2) - hoopDict[ho][1] + hoops.height / 2) < 10:
        #         print("YOU HIT A HOOP")
    time_delta = 0.00025 
    if sum != 0:
        time_delta_delta = 0.0001 / sum
    else:
        time_delta_delta = 0.0000001
    colorI = 0
    while (abs(xGo - x) > 1 or abs(yGo - y) > 1):
        if ballColor:
            canvas.itemconfig(ball, fill='white')
        else:
            canvas.itemconfig(ball, fill='#ccc')
        if colorI % 50 == 0:
            ballColor = not ballColor
        colorI +=1
        moveX = ((xGo - x) * .005)
        moveY = ((yGo - y) * .005)
        if moveX == 0 and xGo > x:
            moveX = 1
        if moveY == 0 and yGo > y:
            moveY = 1
        if moveX == 0 and xGo < x:
            moveX = -1
        if moveY == 0 and yGo < y:
            moveY = -1
        
        canvas.move(ball, moveX, moveY)
        canvas.move(shadow, moveX, moveY)
        canvas.update()
        x = int((canvas.coords(ball)[0]))
        y = int((canvas.coords(ball)[1]))
        #if (angle >= 0 and angle < 40) or (angle > 140 and angle < 220) or (angle > 320 and angle <= 360):
        for ho in hoopDict:
            # if ho == 3:
            #     print("x1 dif", x - hoopDict[ho][0])
            #     print("x2 dif", x - hoopDict[ho][0] + hoops.width)
            if abs(x - hoopDict[ho][0]) < 1 or abs(int((canvas.coords(ball)[2])) - hoopDict[ho][0] + hoops.width) < 1:
                if y < hoopDict[ho][1] and y > hoopDict[ho][1] - hoops.height:
                    newAngle = (-1 * angle + 360 + 180) % 360
                    #print("newAngel: " + str(newAngle))
                    canvas.coords(ball)
                    print("BUMP!")
                    move_ball(power * 0.25, newAngle)
                    #print(canvas.coords(ball))
                    return
                    


        time_delta += time_delta_delta
        time.sleep(.0005 + time_delta)
    if gotPoint:
        score += 1
        canvas.itemconfig(scoreText, text= f"Score: {score}")

def getAngle(data, width):
    value = abs(data[1]['x']-data[0]['x'])
    print("startX:", data[0]['x'])
    print("endX:", data[1]['x'])
    
    print("width:", width)
    print("val:", value)
    
        
    if value > (width*.65):
        value = width*.65
    if (data[1]['x'] > data[0]['x']):
        value *= -1
    # if data[0]['time'] > data[1]['time']:
    #     value *= -1
    angle = (math.acos(value/(width*.65)) * 180) / 3.1415
    return angle

def getPower(path):
    power = (abs(path[0]['tri'] - path[1]['tri']) / abs(int(datetime.strptime(path[0]['time'], '%H:%M:%S.%f').microsecond) - int(datetime.strptime(path[1]['time'], '%H:%M:%S.%f').microsecond))) * 10000
    return power

def task():
    global hits
    while True:
        width, track_data = tracking.trackHit()
        path = tracking.get_duration(track_data)
        if path[0]['x'] == 0 or path[1]['x'] ==0:
            continue
        #print(path)
        if abs(path[0]['tri'] - path[1]['tri']) < 4:
            continue
        myAngle = getAngle(path, width)
        print("traingle Ratio: ", abs(path[0]['tri'] - path[1]['tri']))
        print("t1",path[0]['time'])
        print("t2",path[1]['time'])
        power = getPower(path)
        print("power:", power)
        hits += 1
        canvas.itemconfig(hitsText, text= f"Hits: {hits}")
        if path[0]['time'] < path[1]['time']:
            myAngle += 180
        move_ball(power, myAngle)
        tracking.store_swing('steve', path[0]['x'], path[0]['y'], path[1]['x'], 
            path[1]['y'],tracking.get_time_change(path[0], path[1]), myAngle, power)
        
        
window.after(1000, task)
window.mainloop()

