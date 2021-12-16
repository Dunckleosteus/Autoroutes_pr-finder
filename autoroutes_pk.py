from tkinter import *
import math
WIDTH1 = 900;HEIGHT1 = 900
WIDTH = 800; HEIGHT = 800
A8 = [(80, 80), (160, 160), (240, 240), (300, 240), (600,400)]
xoff = 50; yoff=50
DOTS=[]
def closest(x, y):
    global DOTS
    canvas.create_oval(x-10+xoff,y-10+yoff,x+10+xoff,y+10+yoff,fill="pink")
    min_distance = 100000
    closest = 0
    for i in A8:
        if math.dist((x,y),i)<min_distance:
            min_distance=math.dist((x,y),i)
            closest = i
    canvas.create_oval(closest[0]-10+xoff,closest[1]-10+yoff,closest[0]+10+xoff,closest[1]+10+yoff,fill='red',tag='closest')
    print(min_distance)
def drawgrid():
    for i in range (0, 10+1):
        canvas.create_line((i*WIDTH/10)+xoff, yoff, (i*WIDTH/10)+xoff, HEIGHT+yoff, fill="white")
        canvas.create_line(xoff, (i*HEIGHT/10)+yoff, WIDTH+xoff, (i*HEIGHT/10)+yoff, fill="white")
        canvas.create_text((i*WIDTH/10)+xoff,20,text=i,fill="white",font=('consolas',20))
        canvas.create_text((i*WIDTH/10)+xoff,HEIGHT+1.5*yoff,text=int(i*WIDTH/10),fill="white",font=('consolas',10))
        canvas.create_text(20,(i*HEIGHT/10)+yoff,text=i,fill="white",font=('consolas',20))
        canvas.create_text(WIDTH+1.5*xoff,(i*HEIGHT/10)+yoff,text=int(i*HEIGHT/10),fill="white",font=('consolas',10))
def drawdots():
    for i in A8:
            dot =canvas.create_oval(i[0]-5+xoff,i[1]-5+yoff,i[0]+5+xoff,i[1]+5+yoff, fill="blue", tag = "dot")
            DOTS.append(dot)
def drawlines():
    for i in range (0, len(A8)):
        if i+1 < len(A8):
            coorda=A8[i]
            coordb=A8[i+1]
            canvas.create_line(coorda[0]+xoff,coorda[1]+yoff,coordb[0]+xoff,coordb[1]+yoff, fill="yellow",width=3)


window = Tk()
canvas = Canvas(window,width=WIDTH1,height=HEIGHT1,bg="black")
canvas.pack()
drawgrid()
drawlines()
drawdots()
closest(32,240)
window.mainloop()
