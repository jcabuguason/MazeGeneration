import pygame
import random


WIDTH = 800
HEIGHT = 800
FPS = 30

#initialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Grid")
clock = pygame.time.Clock();
white = [255,255,255]
black = [0,0,0]
screen.fill(white)
pygame.display.update()

#number of blocks on x and y axis
n = 7
blockLength= (int) (WIDTH/n)

#grid matrix to store values in 
grid = [[0 for x in range(n)] for y in range(n)]


#creates grid base
for i in range(blockLength):
    pygame.draw.line(screen,black,(0,i*blockLength),(WIDTH,i*blockLength),1)
    pygame.draw.line(screen,black,(i*blockLength,HEIGHT),(i*blockLength,0),1)





#implementing recursive backtracker algorithim
def moveBlock(row,col,direction):
    
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end ='')
        print(" ")
    print("_______________")  

    #store direction in matrix
    grid[row][col] = direction;
    print(str(direction)+"")
    

    #if next block is empty call moveBlock in next block

    #if next direction is up
    if direction == 1:
        if (row-1>= 0) and (grid[row-1][col] == 0):
            moveBlock(row-1,col,random.randint(1,4))

    
    #if next direction is down
    if direction == 2:
        if row+1 < n and grid[row+1][col] == 0:
            moveBlock(row+1,col,random.randint(1,4))
        
    #if next direction is right
    if direction == 3 and (col+1 < n and grid[row][col+1] == 0):
        if (col+1 < n and grid[row][col+1] == 0):
            moveBlock(row,col+1,random.randint(1,4))

    #if next direction is left 
    if direction == 4:
        if col-1 >= 0 and grid[row][col-1]== 0:
            moveBlock(row,col-1,random.randint(1,4))



    #if next block is full (out of bounds/has value) check for any other empty directions

    if row-1 >= 0:
        emptyTop = (grid[row-1][col] == 0)
    else: 
        emptyTop = False
    if row+1 < n:
        emptyBottom = (grid[row+1][col] == 0 )
    else:
        emptyBottom = False
    if col+1 < n:
        emptyRight = (grid[row][col+1] == 0)
    else: 
        emptyRight = False
    if col-1 < n:
        emptyLeft = (grid[row][col-1] == 0)
    else:
        emptyLeft = False
        
    #while there are empty reachable blocks 
    while(emptyTop or emptyBottom or emptyRight or emptyLeft):
        moveBlock(row,col,random.randint(1,4))

        if row-1 >= 0:
            emptyTop = (grid[row-1][col] == 0)
        else: 
            emptyTop = False
        if row+1 < n:
            emptyBottom = (grid[row+1][col] == 0 )
        else:
            emptyBottom = False
        if col+1 < n:
            emptyRight = (grid[row][col+1] == 0)
        else: 
            emptyRight = False
        if col-1 < n:
            emptyLeft = (grid[row][col-1] == 0)
        else:
            emptyLeft = False
    

#choose a starting block at random 
r = random.randint(0,n-1)
c = random.randint(0,n-1)
d = random.randint(1,4)

#display starting coordinate
print(str(r)+" "+str(c))

moveBlock(r,c,d)
    

#erase lines that connect the maze routes corresponding to the matrix values
for i in range(n):
    for j in range(n):
        print(grid[i][j], end ='')

        if grid[i][j] == 1:
            pygame.draw.line(screen,white,( blockLength*j,blockLength*(i) ),( blockLength*(j+1),blockLength*(i)),1)
        elif grid[i][j] == 2:
            pygame.draw.line(screen,white,( blockLength*(j),blockLength*(i+1) ),( blockLength*(j+1),blockLength*(i+1)),1)
        elif grid[i][j] == 3:
            pygame.draw.line(screen,white,( blockLength*(j+1),blockLength*(i) ),(blockLength*(j+1),blockLength*(i+1) ),1 )
        elif grid[i][j] == 4:
            pygame.draw.line(screen,white,(blockLength*(j),blockLength*(i) ),(blockLength*(j),blockLength*(i+1)),1 )  
    print(" ")


running = True
while running:

    #keep running at the right speed
    clock.tick(FPS)

    #process input(events)
    for event in pygame.event.get():
        #check for closing the window
        if event.type == pygame.QUIT:
            running = False

    #update the screen every loop
    pygame.display.update()



