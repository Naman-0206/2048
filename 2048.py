import numpy

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

grid=numpy.zeros((4,4),dtype=numpy.int16)

while 2048 not in grid:
    print(grid)
    inp=input()
    if inp.lower()=="d":     #right
        for i in range (4):
            addr(grid[i])

    elif inp.lower()=="a":   #left
        for i in range (4):
            addl(grid[i])

    elif inp.lower()=="w":   #up using left
        for i in range(4):
            list=[]
            for j in range(4):
                list.append(grid[j][i])
            addl(list)
            for j in range(4):
                grid[j][i]=list[j]
    
    elif inp.lower()=="s":   #down using right
        for i in range(4):
            list=[]
            for j in range(4):
                list.append(grid[j][i])
            addr(list)
            for j in range(4):
                grid[j][i]=list[j]

    else:
        print("Invalid input")
        
print(grid,"\nYOU WON!")
