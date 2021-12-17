

from tkinter import *
import math
WIDTH1 = 900;HEIGHT1 = 900
WIDTH = 800; HEIGHT = 800
DOTS = []
xoff = 50; yoff=50
PR = [(265, 77), (218, 155), (177, 276), (360, 284), (597, 270), (804, 326), (623, 394), (672, 485), (691, 549), (496, 581), (245, 580), (261, 687), (407, 722), (609, 708), (758, 647), (821, 749)]
SELECTION=[]
A8=[(302, 54), (292, 66), (276, 77), (254, 86), (241, 94), (225, 102), (218, 114), (211, 128), (220, 144), (221, 158), (209, 173), (198, 182), (188, 193), (173, 204), (164, 211), (160, 226), (160, 237), (164, 252), (170, 263), (180, 281), (199, 287), (212, 289), (224, 288), (242, 285), (265, 285), (286, 287), (301, 284), (317, 284), (341, 284), (362, 284), (380, 284), (395, 282), (414, 282), (434, 283), (459, 282), (477, 279), (494, 279), (511, 280), (533, 281), (551, 276), (572, 276), (596, 276), (616, 273), (623, 259), (632, 249), (641, 243), (658, 239), (677, 238), (701, 236), (724, 239), (748, 252), (773, 264), (779, 271), (795, 288), (802, 306), (804, 325), (806, 344), (802, 359), (791, 381), (783, 391), (768, 402), (746, 417), (731, 421), (717, 426), (694, 425), (676, 419), (656, 414), (645, 403), (628, 397), (618, 399), (610, 406), (604, 419), (604, 435), (607, 449), (615, 470), (626, 479), (651, 486), (665, 488), (683, 487), (701, 490), (717, 497), (725, 510), (726, 532), (714, 545), (693, 550), (682, 557), (671, 560), (656, 565), (645, 571), (628, 577), (610, 583), (588, 587), (564, 587), (543, 586), (525, 585), (507, 583), (488, 579), (468, 578), (447, 578), (428, 578), (413, 578), (396, 576), (378, 579), (358, 579), (338, 580), (319, 580), (300, 580), (276, 579), (249, 580), (237, 588), (226, 603), (223, 616), (220, 629), (224, 646), (234, 659), (246, 671), (281, 699), (312, 715), (326, 718), (343, 718), (359, 719), (373, 719), (388, 719), (406, 724), (419, 728), (432, 734), (452, 733), (473, 734), (490, 730), (512, 722), (536, 722), (553, 725), (573, 727), (588, 722), (606, 710), (630, 706), (645, 700), (667, 692), (683, 685), (698, 678), (723, 664), (738, 656), (766, 648), (785, 648), (799, 656), (806, 674), (808, 687), (809, 701), (810, 711), (814, 725), (817, 742), (826, 758), (845, 765),]
DRAW = False

def troncon(pkdeb,pkfin):
    pka=PR[pkdeb];pkax=pka[0];pkay=pka[1]
    pkb=PR[pkfin];pkbx=pkb[0];pkby=pkb[1]
    a=closest(pkax,pkay);b=closest(pkbx,pkby)
    print("{},{}".format(a,b))
    SELECTION=A8

def draw_road(event):
    canvas.create_oval(event.x-10,event.y-10,event.x+10,event.y+10,fill="pink")
    print("Mouse position: ({},{},{})".format(len(PR),event.x, event.y))
    PR.append((event.x,event.y))
def print_road():
    global PR
    print(PR)
def draw():
    global draw
    DRAW = False
def closest(x, y):
    global DOTS
    canvas.create_oval(x-10,y-10,x+10,y+10,fill="pink")
    min_distance = 100000
    closest = 0
    for i in A8:
        if math.dist((x,y),i)<min_distance:
            min_distance=math.dist((x,y),i)
            closest = i
    canvas.create_oval(closest[0]-10,closest[1]-10,closest[0]+10,closest[1]+10,fill='red',tag='closest')
    return i
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
            dot =canvas.create_oval(i[0]-5,i[1]-5,i[0]+5,i[1]+5, fill="blue", tag = "dot")
            DOTS.append(dot)
def drawlines():
    for i in range (0, len(A8)):
        if i+1 < len(A8):
            coorda=A8[i]
            coordb=A8[i+1]
            canvas.create_line(coorda[0],coorda[1],coordb[0],coordb[1], fill="yellow",width=3,tag='line')
def drawselect():
    pass 
def draw_pr():
    for i in range(0,len(PR)):
        coordinates=PR[i]
        canvas.create_oval(coordinates[0]+5,coordinates[1]+5,coordinates[0]-5,coordinates[1]-5,fill='red')

window = Tk()
window.geometry('{}x{}'.format((WIDTH1*2)+100,HEIGHT1))
canvas = Canvas(window,width=WIDTH1,height=HEIGHT1,bg="black")
canvas2 = Canvas(window,width=WIDTH1,height=HEIGHT1,bg="green")
canvas2.place(x=0,y=0)
canvas.place(x=WIDTH1+100,y=0)
drawgrid()
drawlines()
drawdots()
draw_pr()
troncon(0,5)

#window.bind("<Button-1>", draw_road)
but1=Button(window,text='print road',)
but1.place(x=WIDTH1+10,y=50)

window.mainloop()
