from tkinter import *
import math
import numpy as np
WIDTH1 = 900;HEIGHT1 = 900
WIDTH = 800; HEIGHT = 800
DOTS = []
xoff = 50; yoff=50
PR = [(265, 77), (218, 155), (177, 276), (360, 284), (597, 270), (804, 326), (623, 394), (672, 485), (691, 549), (496, 581), (245, 580), (261, 687), (407, 722), (609, 708), (758, 647), (821, 749)]
SELECTION=[]
A8=[(302, 54), (292, 66), (276, 77), (254, 86), (241, 94), (225, 102), (218, 114), (211, 128), (220, 144), (221, 158), (209, 173), (198, 182), (188, 193), (173, 204), (164, 211), (160, 226), (160, 237), (164, 252), (170, 263), (180, 281), (199, 287), (212, 289), (224, 288), (242, 285), (265, 285), (286, 287), (301, 284), (317, 284), (341, 284), (362, 284), (380, 284), (395, 282), (414, 282), (434, 283), (459, 282), (477, 279), (494, 279), (511, 280), (533, 281), (551, 276), (572, 276), (596, 276), (616, 273), (623, 259), (632, 249), (641, 243), (658, 239), (677, 238), (701, 236), (724, 239), (748, 252), (773, 264), (779, 271), (795, 288), (802, 306), (804, 325), (806, 344), (802, 359), (791, 381), (783, 391), (768, 402), (746, 417), (731, 421), (717, 426), (694, 425), (676, 419), (656, 414), (645, 403), (628, 397), (618, 399), (610, 406), (604, 419), (604, 435), (607, 449), (615, 470), (626, 479), (651, 486), (665, 488), (683, 487), (701, 490), (717, 497), (725, 510), (726, 532), (714, 545), (693, 550), (682, 557), (671, 560), (656, 565), (645, 571), (628, 577), (610, 583), (588, 587), (564, 587), (543, 586), (525, 585), (507, 583), (488, 579), (468, 578), (447, 578), (428, 578), (413, 578), (396, 576), (378, 579), (358, 579), (338, 580), (319, 580), (300, 580), (276, 579), (249, 580), (237, 588), (226, 603), (223, 616), (220, 629), (224, 646), (234, 659), (246, 671), (281, 699), (312, 715), (326, 718), (343, 718), (359, 719), (373, 719), (388, 719), (406, 724), (419, 728), (432, 734), (452, 733), (473, 734), (490, 730), (512, 722), (536, 722), (553, 725), (573, 727), (588, 722), (606, 710), (630, 706), (645, 700), (667, 692), (683, 685), (698, 678), (723, 664), (738, 656), (766, 648), (785, 648), (799, 656), (806, 674), (808, 687), (809, 701), (810, 711), (814, 725), (817, 742), (826, 758), (845, 765),]
A7=[(52, 396), (83, 392), (100, 396), (142, 403), (176, 400), (219, 385), (257, 372), (297, 370), (342, 378), (387, 374), (450, 373), (482, 362), (501, 343), (520, 313), (540, 277), (555, 248), (572, 216), (592, 185), (612, 159), (641, 130), (682, 115), (726, 107), (753, 91), (797, 85), (802, 113), (800, 146), (809, 182), (810, 215), (834, 241), (849, 248)]
PRA7=[(72, 393), (190, 395), (342, 376), (470, 365), (529, 290), (573, 207), (648, 128), (737, 98), (802, 139), (828, 230)]
LISTE_RTE = [A8,A7]
def troncon(route,prdeb,prfin):
    global PR
    global A8;global LISTE_RTE
    select=route
    print("pr deb = "+str(prdeb))
    print("pr fin = "+str(prfin))
    pr1=PR[prdeb];pr1x=pr1[0];pr1y=pr1[1];print("pr1y: {}, pr1x: {}".format(pr1y,pr1x))# x & y coordinates of start pr
    pr2=PR[prfin];pr2x=pr2[0];pr2y=pr2[1];print("pr2y: {}, pr2x: {}".format(pr2y,pr2x))# x & y coordinates of end pr
    start_index=closest(pr1x,pr1y);print("closest1: {}".format(start_index))# index of the dot closest to the start pr
    end_index=closest(pr2x,pr2y);print("closest2: {}".format(end_index))# index of the dot closest to the further pr
    select=(select[start_index:end_index]);print(select)# create selection of all the values in between start and and pr
    drawlines(select,2)# draw this selection on second canvas
def draw_road(event):
    canvas.create_oval(event.x-10,event.y-10,event.x+10,event.y+10,fill="pink")
    print("Mouse position: ({},{},{})".format(len(PR),event.x, event.y))
    PRA7.append((event.x,event.y))
    print(PRA7)
def print_road():
    global PR
    print(PR)
def draw():
    global draw
    DRAW = False
def closest(x1,y1):
    global A8
    listx = (x[0] for x in A8)# list of all the x values
    listy = (x[1] for x in A8)# list of all the y values
    distance = list(math.dist((x[0],x[1]),(x1,y1)) for x in A8)# creates list of all the distcance values
    min_value = min(distance)# find the smallest distance value
    return distance.index(min_value)# find the index of the smallest distance

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
def drawlines(ar,canv):
    if canv==2:
        canvas2.delete('line')
    for i in range (0, len(ar)):
        if i+1 < len(ar):
            coorda=ar[i]
            coordb=ar[i+1]
            if canv == 1:
                canvas.create_line(coorda[0],coorda[1],coordb[0],coordb[1], fill="yellow",width=3,tag='line')
            elif canv ==2:
                canvas2.create_line(coorda[0],coorda[1],coordb[0],coordb[1], fill="yellow",width=3,tag='line')
def draw_pr():
    for i in range(0,len(PR)):
        coordinates=PR[i]
        canvas.create_oval(coordinates[0]+5,coordinates[1]+5,coordinates[0]-5,coordinates[1]-5,fill='red')
def test():
    canvas2.create_line(0,0,500,500,fill='red',width='5')
def userinput():
    global SELECTION
    entry_deb=Entry()
    entry_fin=Entry()
    entry_fin.pack()
    entry_deb.pack()
    def validate():
        
        troncon(A8,int(entry_fin.get()),int(entry_deb.get()))
        butt2.destroy();entry_deb.destroy();entry_fin.destroy()
    butt2=Button(text='validate',command=validate);butt2.pack()

window = Tk()
window.geometry('{}x{}'.format((WIDTH1*2)+100,HEIGHT1))
canvas = Canvas(window,width=WIDTH1,height=HEIGHT1,bg="black")
canvas2 = Canvas(window,width=WIDTH1,height=HEIGHT1,bg="green")
canvas2.place(x=0,y=0)
canvas.place(x=WIDTH1+100,y=0)
drawgrid()
drawlines(A8,1)
drawlines(A7,1)
drawdots()
draw_pr()
#window.bind("<Button-1>", draw_road)# uncomnent to draw a new road
but1=Button(window,text='choose PR',command=userinput)
but1.pack()
but3=Button(window,text='choose road')
but3.pack()
window.mainloop()
