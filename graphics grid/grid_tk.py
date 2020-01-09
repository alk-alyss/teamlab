from tkinter import *
from PIL import Image, ImageTk

#global variables

winsize = 800
n = 12
A = [[0 for j in range(n)] for i in range(n)]
shapes = {}
d =int( winsize / n)
temp = 0
tmp = -1
car = False
flag = False
start = False

size = (d,d)
#functions

def Images():
    sprites = {}
    my_file = open('sprite_names.txt', 'r')
    for line in my_file:
        line = line[:-1]
        a = Image.open("sprites/{}.png".format(line))
        sprites[line]=a
    return(sprites)

def draw_grid():
    global road_sprite
    c.create_line(winsize,0,winsize,winsize)
    c.create_line(0,winsize,winsize,winsize)
    for i in range(0,winsize,d):
        c.create_line(0, i, winsize, i)
    for i in range(0,winsize,d):
        c.create_line(i, 0, i, winsize)
    for i in range(0,winsize,d):
        for j in range(0,winsize,d):
            c.create_image(i+d/2,j+d/2,image = road_sprite)
        
    

def callback(event):
    #temp: 1= square ,2=house ,3=tree , 4=grease ,5=car ,6 = flag 
    global car,flag, temp,n,d,start
    
    #global a
    x = int(event.x//d)
    y = int(event.y//d)
    
    
    if x<n and y  < n:
        print ("clicked at box ({},{})".format( event.x//d, event.y//d))
    if A[x][y] == 0:
        if temp == 1:
            #check around squares and if all are 0 then build a square
            if x - 1 >= 0 and x+1 < n and y-1 >=0 and y+1 < n and  A[x-1][y-1] == 0 and A[x][y-1]==0 and A[x+1][y-1] ==0 and A[x-1][y] ==0 and A[x+1][y]==0 and A[x-1][y+1]==0 and A[x][y+1]==0 and A[x+1][y+1]==0:
                A[x-1][y-1]=A[x][y-1] =A[x+1][y-1] =A[x-1][y] =A[x+1][y]=A[x-1][y+1]=A[x][y+1]=A[x+1][y+1]= 1
                A[x][y] = 10
                print('building square')
                #here we make a square at (x-1,y-1)-->(x+1,y+1)
                shapes[(x,y)] = c.create_image((x*d+d/2),(y*d+d/2),image=gridsprites[3])
        elif temp == 2:
            A[x][y] = 2
            #here we make a house at (x,y) coordinates
            shapes[(x,y)] = c.create_image(x*d+d/2,y*d+d/2,image=gridsprites[0])
        elif temp == 3:
            A[x][y] = 3
            #here we make a tree at (x,y) coordinates
            shapes[(x,y)] = c.create_image(x*d+d/2,y*d+d/2,image=gridsprites[1])
        elif temp == 4:
            A[x][y] = 4 
            #here we make grease at (x,y) coordinates
            shapes[(x,y)] = c.create_image(x*d+d/2,y*d+d/2,image=gridsprites[2])
        elif temp == 5 and car == False:
            A[x][y] = 5
            car = True
            #here we make a car at (x,y) coordinates
            shapes[(x,y)] = c.create_rectangle(x*d,y*d,(x+1)*d,(y+1)*d,fill='red')
            if flag == True and start == False:
                shapes['start'] = c4.create_rectangle(1,101,204,204,fill='orange')
                start = True
        elif temp == 6 and flag == False:
            A[x][y] = 6
            flag = True
            #here we make flag at (x,y) coordinates
            shapes[(x,y)] = c.create_rectangle(x*d,y*d,(x+1)*d,(y+1)*d,fill='pink')
            if car == True and start == False:
                shapes['start'] = c4.create_rectangle(1,101,204,204,fill='orange')
                start = True

            
    elif A[x][y] == 10:
        if temp == 1 or temp == 0:
            A[x][y]=A[x-1][y-1]=A[x][y-1] =A[x+1][y-1] =A[x-1][y] =A[x+1][y]=A[x-1][y+1]=A[x][y+1]=A[x+1][y+1]= 0
            c.delete(shapes[(x,y)])
            shapes.pop((x,y)) 
            print('square is demolished')
    elif A[x][y] == 2:
        if temp == 2 or temp == 0:
            A[x][y] = 0
            c.delete(shapes[(x,y)])
            shapes.pop((x,y)) 
            print('house is demolished')
    elif A[x][y] == 3:
        if temp == 3 or temp == 0:
            A[x][y] = 0
            c.delete(shapes[(x,y)])
            shapes.pop((x,y)) 
            print('tree is demolished')
    elif A[x][y] == 4:
        if temp == 4 or temp == 0:
            A[x][y] = 0
            c.delete(shapes[(x,y)])
            shapes.pop((x,y)) 
            print('grease is demolished')
    elif A[x][y] == 5 :
        if temp == 5 or temp == 0 :
            A[x][y] = 0
            c.delete(shapes[(x,y)])
            shapes.pop((x,y))
            if start == True:
                start = False
                c4.delete(shapes['start'])
                flag = False
                print('flag is removed')
            car = False
            print('car is removed')
    elif A[x][y] == 6 :
        if temp == 6 or temp == 0 :
            A[x][y] = 0
            c.delete(shapes[(x,y)])
            if start == True:
                start = False
                c4.delete(shapes['start'])
                car = False
                print ('car is removed')
            shapes.pop((x,y))
            flag = False
            print('flag is removed')
            
        
def callback2(event):
    global temp
    global tmp
    if event.x >= 10 and event.x <= 190 :
        temp = int(event.y//(winsize/4))+1
        if temp != tmp:
            tmp = temp
            print ("clicked at box {}".format(temp))
        else:
            temp = 0
            tmp = -1
            print('temp is 0')
def callback3(event):
    global temp
    global tmp
    if event.x >= 2 and event.x <= 205 :
        print('clicked at ({},{})'.format(event.x,event.y))
        temp = int(event.x//(205/2))+5
        if temp != tmp:
            if temp == 1: print('car is pressed')
            elif temp == 2:print('flag is pressed')
            tmp = temp
        else:
            temp = 0
            tmp = -1
            print('temp is 0')
def callback4(event):
    global shapes, temp,car,flag,start
    y = event.y
    if y < 100 :
        tmp = temp
        temp = 0
        car = False
        flag = False
        if start == True:
            c4.delete(shapes['start'])
            start = False
        for i in shapes:
            c.delete(shapes[i])
        shapes.clear()
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = 0
        draw_grid()
    else:
        print('perform astar')


    
                
#main

win = Tk()
win.geometry('{}x{}'.format(winsize+500,winsize))
win.title('Grid')

c = Canvas(win,width =winsize,height = winsize)
c.pack(side = LEFT)


sprites = Images()
palette = [sprites['park palette'],sprites['house palette'],sprites['tree palette'],sprites['oil palette']]

road_sprite = ImageTk.PhotoImage(sprites['road'].resize(size))


gridsprites= []
a = sprites['park 2'].resize((3*d,3*d))
a= ImageTk.PhotoImage(a)

gridsprites = [sprites['house'],sprites['tree'],sprites['oil']]
for i in range(len(palette)):
    palette[i] = palette[i].resize((200,200))
    palette[i] = ImageTk.PhotoImage(palette[i])
for i in range(len(gridsprites)):
    gridsprites[i] = gridsprites[i].resize(size)
    gridsprites[i] = ImageTk.PhotoImage(gridsprites[i])
gridsprites.append(a)

draw_grid()
    
B = ['blue','green','white','yellow']
c2 = Canvas(win,width = 200,height = winsize+50)
c2.pack(side = RIGHT)
for i in range(len(palette)):
    c2.create_rectangle(2,i*winsize/4+2,200,winsize/4+i*winsize/4-3)
    c2.create_image(100,winsize/8 + i * winsize/4,image = palette[i]) 
    
c3 = Canvas(win,width = 205,height = 102)
c3.pack()
c3.create_rectangle(2,2,102,100,fill = 'red')
c3.create_rectangle(104,2,204,100,fill = 'pink')

c4 = Canvas(win,width = 205,height = 205)
c4.pack()
c4.create_rectangle(1,1,204,99,fill = 'black')



c2.bind("<Button-1>",callback2)
c.bind("<Button-1>", callback)
c3.bind("<Button-1>", callback3)
c4.bind("<Button-1>", callback4)




win.mainloop()


