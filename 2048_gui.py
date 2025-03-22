from tkinter import *
import numpy
import random

def newelement():
    if 0 in grid:    
        x,y=random.randint(0,3),random.randint(0,3)
        while grid[x][y]!=0:
            x,y=random.randint(0,3),random.randint(0,3)
        grid[x][y]=random.choice([2,2,2,2,2,2,2,4,2,2,16,8,2,2,2,2,2,2,2,2,2,2,2,2,2])

def sortr(list):

    for i in  range(len(list)-1,-1,-1):
        if list[i]==0:
            for j in range(i-1,-1,-1):
                if list[j] !=0:
                    list[i]=list[j]
                    list[j]=0
                    break
    return list

def addr(list):
    list=sortr(list)
    if list[3]==list[2]:
        list[3]=list[3]*2
        list[2]=0
    if list[2]==list[1]:
        list[2]=list[2]*2
        list[1]=0
    if list[0]==list[1]:
        list[1]=list[0]*2
        list[0]=0
    return sortr(list)

def sortl(list):
    for i in  range(len(list)):
        
        if list[i]==0:
            for j in range(i+1,len(list)):
                
                if list[j] !=0:
                    list[i]=list[j]
                    list[j]=0
                    break

    return list

def addl(list):
    list=sortl(list)
    if list[0]==list[1]:
        list[0]=list[0]*2
        list[1]=0
    if list[1]==list[2]:
        list[1]=list[1]*2
        list[2]=0
    if list[2]==list[3]:
        list[2]=list[3]*2
        list[3]=0
    return sortl(list)

def update():
    newelement() 
    for i in range(4):
        for j in range(4):
            l=Label(f1,text=" " if grid[j][i] == 0 else grid[j][i],padx=10,pady=10,width=5,height=2,fg="green",borderwidth=3,font="comicsans 30",relief="solid").grid(column=i,row=j)
def right(x):
    for i in range (4):
            addr(grid[i])
    update() 
def left(x):
    for i in range (4):
        addl(grid[i])
    update()          
def up(x):
    for i in range(4):
        list=[]
        for j in range(4):
            list.append(grid[j][i])
        addl(list)
        for j in range(4):
            grid[j][i]=list[j]
    update()
def down(x):
    for i in range(4):
        list=[]
        for j in range(4):
            list.append(grid[j][i])
        addr(list)
        for j in range(4):
            grid[j][i]=list[j] 
    update()


root=Tk(baseName="2048")
root.geometry("600x600")
root.title = "2048"
root.wm_title("2048")
score=Frame(root)
l1=Label(score,text="2048",fg="orange",font="comicsans 40 bold").grid(column=0,row=0)
score.pack()

f1=Frame(root,bg="brown",pady=10,padx=10)

grid=numpy.zeros((4,4),dtype=numpy.int16)
newelement()
update()

f1.pack()

root.bind("<Right>",right)
root.bind("<Left>",left)
root.bind("<Up>",up)
root.bind("<Down>",down)


root.mainloop()