#Libs and modules

from tkinter import *
from PIL import Image, ImageTk
import astar
import time
import menu

#global variables
road_sprite = c5=timer_label = timer_sprite = start_time =timer =  start_sprite =erase_sprite = sprites =start_program = win=speed=prev_angle =car_box=flag_box=start_box=erase_box =C= c=c2=c3=car=flag=temp=car_sprite=flag_sprite=n=d=start=A=erase_box=c4=tmp =gridsprites = 0
B = [0,0,0,0]

shapes = {}

def Images():
    
    sprites = {}
    my_file = open('sprite_names.txt', 'r')
    for line in my_file:
        try:
            line = line[:-1]
            a = Image.open("sprites/{}.png".format(line))
            sprites[line]=a
        except:
            break
    return(sprites)

def draw_grid():
    global road_sprite,c,winsize,d
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
    global c,car,flag,start_sprite, temp,n,d,start,A,shapes,gridsprites,car_sprite,flag_sprite,car_box,flag_box
    
    #global  
    x = int(event.x//d)
    y = int(event.y//d)
    
    
    # if x<n and y  < n:
        # print ("clicked at box ({},{})".format( event.x//d, event.y//d))
    if A[x][y] == 0:
        if temp == 1:
            #check around squares and if all are 0 then build a square
            if x - 1 >= 0 and x+1 < n and y-1 >=0 and y+1 < n and  A[x-1][y-1] == 0 and A[x][y-1]==0 and A[x+1][y-1] ==0 and A[x-1][y] ==0 and A[x+1][y]==0 and A[x-1][y+1]==0 and A[x][y+1]==0 and A[x+1][y+1]==0:
                A[x-1][y-1]=A[x][y-1] =A[x+1][y-1] =A[x-1][y] =A[x+1][y]=A[x-1][y+1]=A[x][y+1]=A[x+1][y+1]= 1
                A[x][y] = 10
                # print('building square')
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
            shapes['car'] = c.create_image(x*d+d/2,y*d+d/2,image = car_sprite)
            if flag == True and start == False:
                start_box  = c4.create_rectangle(1,101,204,204,fill='orange')
                shapes['start_sprite'] = c4.create_image(100,150,image = start_sprite)
                shapes['start'] = start_box
                start = True
        elif temp == 6 and flag == False:
            A[x][y] = 6
            flag = True
            #here we make flag at (x,y) coordinates
            shapes['flag'] = c.create_image(x*d+d/2,y*d+d/2,image = flag_sprite)
            if car == True and start == False:
                start_box  = c4.create_rectangle(1,101,204,204,fill='orange')
                shapes['start_sprite'] = c4.create_image(100,150,image = start_sprite)
                shapes['start'] = start_box
                start = True

            
    elif A[x][y] == 10:
        if temp == 1 or temp == 0:
            A[x][y]=A[x-1][y-1]=A[x][y-1] =A[x+1][y-1] =A[x-1][y] =A[x+1][y]=A[x-1][y+1]=A[x][y+1]=A[x+1][y+1]= 0
            c.delete(shapes[(x,y)])
            shapes.pop((x,y)) 
            # print('square is demolished')
    elif A[x][y] == 2:
        if temp == 2 or temp == 0:
            A[x][y] = 0
            c.delete(shapes[(x,y)])
            shapes.pop((x,y)) 
            # print('house is demolished')
    elif A[x][y] == 3:
        if temp == 3 or temp == 0:
            A[x][y] = 0
            c.delete(shapes[(x,y)])
            shapes.pop((x,y)) 
            # print('tree is demolished')
    elif A[x][y] == 4:
        if temp == 4 or temp == 0:
            A[x][y] = 0
            c.delete(shapes[(x,y)])
            shapes.pop((x,y)) 
            # print('grease is demolished')
    elif A[x][y] == 5 :
        if temp == 5 or temp == 0 :
            A[x][y] = 0
            c.delete(shapes['car'])
            shapes.pop('car')
            if start == True:
                start = False
                c4.delete(shapes['start'])
                c4.delete(shapes['start_sprite'])
                shapes.pop('start')
                # print('flag is removed')
            car = False
            # print('car is removed')
    elif A[x][y] == 6 :
        if temp == 6 or temp == 0 :
            A[x][y] = 0
            c.delete(shapes['flag'])
            if start == True:
                start = False
                c4.delete(shapes['start'])
                c4.delete(shapes['start_sprite'])
                shapes.pop('start')
                # print ('car is removed')
            shapes.pop('flag')
            flag = False
            # print('flag is removed')
            
def callback2(event):
    global temp,tmp,c4,c2,erase_box,B

    if event.x >= 10 and event.x <= 190 :
        temp = int(event.y//(winsize/4))+1
        config(tmp,temp)
        if temp != tmp:
           tmp = temp
        #    print ("clicked at box {}".format(temp))

        else:
            c2.itemconfig(B[temp-1],outline = 'black',width = 1)
            temp = 0
            tmp = -1
            # print('temp is 0')
            
def callback3(event):
    global temp,tmp

    if event.x >= 2 and event.x <= 205 :
        # print('clicked at ({},{})'.format(event.x,event.y))
        temp = int(event.x//(205/2))+5
        config(tmp,temp)
        if temp != tmp:
            # if temp == 5: print('car is pressed')
            # elif temp == 6:print('flag is pressed')
            tmp = temp
        else:
            temp = 0
            tmp = -1
            # print('temp is 0')

def callback4(event):
    global shapes,c5,timer_sprite,timer,timer_label,sprites,start_program,start_sprite,erase_sprite,start_time, temp,win,car,flag,start,speed,tmp,erase_box,B,c2,c4,A,C,sprites,prev_angle
    y = event.y
    if y < 100 :
        temp = 7
        config(tmp,temp)
        tmp = temp
##        time.sleep(0.5)
##        
        car = False
        flag = False
        if start == True:
            c4.delete(shapes['start'])
            c4.delete(shapes['start_sprite'])
            shapes.pop('start')
            start = False
        for i in shapes:
            c.delete(shapes[i])
        shapes.clear()
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = 0
        draw_grid()
    else:
        temp = 8
        config(tmp,temp)
        tmp = temp
        # print('perform astar')

        
        # prwta metatrepoume ton pinaka se pinaka pou tha dwthei ston astar
        C=A[::]
        for i in range(len(C)):
            for j in range(len(C[i])):
                if C[i][j]==0: C[i][j]=1
                elif C[i][j]==1 or C[i][j]==2 or C[i][j]==3 or C[i][j] == 10: C[i][j] = 0
                elif C[i][j]==5:
                    C[i][j]=1
                    start= (i,j)
                elif C[i][j]==6:
                    C[i][j]=1
                    end = (i,j)
##        for i in range(len(C)):
##            for j in range(len(C[i])):
##                print(C[i][j],end=' ')
##            print("")
##        print(start,end)
        path = astar.astar(C,start,end)
        start_time = time.time()
        # print(path)
        if path != 'No path found':
            timer_label = Label(c5,text =timer,fg = 'black',font = 'Arial 30')
            c5.create_image(50,50,image = timer_sprite)
            timer_label.pack()
            prevx = path[0][0]
            prevy = path[0][1]        
            for i in range(1,len(path)):
                x = path[i][0]
                y= path[i][1]
                if C[x][y] == 4: car_move(prevx,prevy,path[i][0],path[i][1],int(speed-speed/3))
                else:car_move(prevx,prevy,path[i][0],path[i][1],speed)
                prevx = path[i][0]
                prevy = path[i][1]
        else:
            timer_label = Label(c5,text = 'No path found',font = 'Arial 30').pack()
        
        try:    
            # print(timer)
            timer_label.config(fg = 'red')
        except:
            pass
        c5.update()
        time.sleep(2)
        win.destroy()
        car = flag = start = False
        
    start_program = True

def config(tmp,temp):
    global B,erase_box,flag_box,start_box,car_box,c2,c3,c4
    if temp > 0 and temp < 5:
        c2.itemconfig(B[temp-1],outline = 'red',width = 5)
    elif temp >= 5 and temp <= 6:
        if temp == 5: c3.itemconfig(car_box,outline = 'yellow',width = 5)
        if temp == 6: c3.itemconfig(flag_box,outline = 'yellow',width = 5)
    elif temp >= 7 and temp <=8:
        if temp == 7: c4.itemconfig(erase_box,outline = 'yellow',width = 5)
        if temp == 8: c4.itemconfig(start_box,outline = 'yellow',width = 5)

    if tmp > 0 and tmp < 5:
        c2.itemconfig(B[tmp-1],outline = 'black',width=1)
    elif tmp >= 5 and tmp <= 6:
        if tmp == 5: c3.itemconfig(car_box,outline = 'black',width =1 )
        if tmp == 6: c3.itemconfig(flag_box ,outline = 'black',width = 1)
    elif tmp >= 7 and tmp <=8:
        if tmp == 7: c4.itemconfig(erase_box,outline = 'black',width = 1)
        if tmp == 8: c4.itemconfig(start_box,outline = 'black',width = 1)

def rotate_(im,old_dir,new_dir):
    if new_dir == "down" : new_dir = 180
    if new_dir == 'left' : new_dir = -90
    if new_dir == 'right' : new_dir = 90
    if new_dir == 'up' : new_dir = 0
    if old_dir == "down" : old_dir = 180
    if old_dir == 'left' : old_dir = -90
    if old_dir == 'right' : old_dir = 90
    if old_dir == 'up' : old_dir = 0
    im = im.rotate(old_dir - new_dir)
    # print(old_dir - new_dir)
##    im = ImageTk.PhotoImage(im)
    return(im)
              
def car_move(x0,y0,x,y,sp = speed):
    global d,prev_angle,c,shapes,speed,sprites,size,timer,timer_label
    dx =  0
    # print(x0,y0,x,y)
    if x - x0 == 1 :
        #move right
        a = sprites['car'].rotate(0)
        a = a.resize((d,d))
        a = ImageTk.PhotoImage(a)
 
        while dx <d :
            timer = time.time()-start_time
            timer_label.config(text = '{:.2f}'.format(timer))
            c.delete(shapes['car'])
            time.sleep(0.01)
            shapes['car'] = c.create_image(x0*d+d/2+dx,d*y0+d/2,image = a)
            dx += sp
            c.update()
           
            
            
    elif x - x0 == -1 :
        #move left
        a = sprites['car'].rotate(180)
        a = a.resize((d,d))
        a = ImageTk.PhotoImage(a)


        while dx < d :
            timer = time.time()-start_time
            timer_label.config(text = '{:.2f}'.format(timer))
            c.delete(shapes['car']) 
            time.sleep(0.01)
            shapes['car'] = c.create_image(x0*d+d/2-dx,d*y0+d/2,image = a)
            dx += sp
            c.update()
            
    elif y - y0 == 1:        
        #move down
        a = sprites['car'].rotate(270)
        a = a.resize((d,d))
        a = ImageTk.PhotoImage(a)

        while dx < d :
            timer = time.time()-start_time
            timer_label.config(text = '{:.2f}'.format(timer))
            c.delete(shapes['car'])
            time.sleep(0.01)
            shapes['car'] = c.create_image(x0*d+d/2,d*y0+d/2+dx,image = a)
##            c.move(shapes['car'],0,sp)
            dx += sp
            c.update()

    elif y - y0 == -1:


        #move up
        a = sprites['car'].rotate(90)
        a = a.resize((d,d))
        a = ImageTk.PhotoImage(a)
                 
        while dx < d :
            timer = time.time()-start_time
            timer_label.config(text = '{:.2f}'.format(timer))
            c.delete(shapes['car'])
            time.sleep(0.01)
            shapes['car'] = c.create_image(x0*d+d/2,d*y0+d/2-dx,image = a)

            c.update() 
               
            dx += sp
                       





def main():
    global road_sprite,c5,timer_label,timer_sprite,timer ,erase_sprite,prev_angle,start_sprite,start_program,win,C,erase_box,sprites,car_box,erase_box,flag_box,car_sprite,flag_sprite,c,winsize,d,B,c2,c3,c4,car,flag,speed, temp,tmp ,n,d,start,A,shapes,erase_box,gridsprites
    winsize = 800
    prev_angle = 'right'
    start_program =False
    n = menu.Menu().mazeSize
    A = [[0 for j in range(n)] for i in range(n)]
    d =int( winsize / n)
    size = (d,d)
    speed = d/20
    timer =  0
    win = Tk()
    win.geometry('{}x{}'.format(winsize+500,winsize))
    win.title('Virtual Car Navigation')

    c = Canvas(win,width =winsize,height = winsize)
    c.pack(side = LEFT)
    sprites = Images()
    palette = [sprites['park palette'],sprites['house palette'],sprites['tree palette'],sprites['oil palette']]

    road_sprite = ImageTk.PhotoImage(sprites['road'].resize(size))
    start_sprite=ImageTk.PhotoImage(sprites['start'].resize((100,100)))
    
    car_sprite = ImageTk.PhotoImage(sprites['car'].resize(size))
    car_palette = ImageTk.PhotoImage(sprites['car'].resize((80,80)))
    flag_sprite = ImageTk.PhotoImage(sprites['flag'].resize(size))
    flag_palette = ImageTk.PhotoImage(sprites['flag'].resize((80,80)))
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
    
    c2 = Canvas(win,width = 200,height = winsize+50)
    c2.pack(side = RIGHT)
    for i in range(len(palette)):
        B[i]=c2.create_rectangle(2,i*winsize/4+2,200,winsize/4+i*winsize/4-3,fill = 'white')
        c2.create_image(100,winsize/8 + i * winsize/4,image = palette[i])
    c3 = Canvas(win,width = 205,height = 102)
    c3.pack()
    car_box = c3.create_rectangle(2,2,102,100,fill = 'green')
    c3.create_image(50,50,image = car_palette)
    flag_box = c3.create_rectangle(104,2,204,100,fill = 'red')
    c3.create_image(150,50,image = flag_palette)

    c4 = Canvas(win,width = 205,height = 205)
    c4.pack()
    erase_box = c4.create_rectangle(1,1,204,99,fill = 'white')
    er = ImageTk.PhotoImage(sprites['reset'].resize((100,100)))
    erase_sprite = c4.create_image(100,50,image = er)
    
    #timer
    c5 = Canvas(win,width = 205,height = 205)
    c5.pack()
    timer_sprite = sprites['timer']
    timer_sprite = ImageTk.PhotoImage(timer_sprite.resize((75,75)))
    c5.create_image(50,50,image = timer_sprite)


    c.bind("<Button-1>", callback)
    c2.bind("<Button-1>",callback2)
    c3.bind("<Button-1>", callback3)
    c4.bind("<Button-1>", callback4)
##    if start_program == True:
##        start_program = False
##        main()
    
    win.mainloop()


#main
while True:
    main()
    if start_program == True:
        main()
