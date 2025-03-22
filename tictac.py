from tkinter import *
import numpy
grid=numpy.zeros((3,3),dtype=numpy.int0)

def check(grid):
    for i in grid:
        if len(set(i))==1:
            if i[0]!=0:
                return(i[0])
                break
    for i in grid.transpose():
        if len(set(i))==1:
            if i[0]!=0:
                return(i[0])
                break
    if grid[0,0]==grid[1,1]==grid[2][2]:
        if grid[0][0]!=0:
            return(grid[0][0])
    elif grid[0,2]==grid[1,1]==grid[2][0]:
        if grid[1,1]!=0:
            return(grid[1][1])

root=Tk()
root.geometry("600x600")
score=Frame(root)
l1=Label(score,text="TicTacToe",fg="orange",font="comicsans 40 bold").grid(column=0,row=0)
score.pack()
f1=Frame(root,bg="brown",pady=10,padx=10)

class button:
    
    def __init__(self,i,j,frame,grid) -> None:
        self.i=i
        self.j=j
        but=Button(frame,text='' if grid[0,0] ==0 else grid[0,0],padx=10,pady=10,width=5,height=2,fg="green",borderwidth=3,font="comicsans 30",relief="solid",command=self.onclick)
        but.grid(column=self.i,row=self.j)
        self.but=but

    def onclick(self):
        global turn
        self.but.config(text='O' if turn%2==0 else 'X',state=DISABLED)
        grid[self.j,self.i]=2 if turn%2==0 else turn%2
        turn+=1
        print(grid)
        w=check(grid)
        if w!= None:

            f1.destroy()
            tex="Player "+str(w)+" "+("O"if w==2 else "X")+" Won"
            l=Label(root,text=tex,font="comicsans 40 bold").pack()

turn=1
for i in range(3):
    for j in range(3):
        but=button(i,j,f1,grid)
        
f1.pack()

root.mainloop()
