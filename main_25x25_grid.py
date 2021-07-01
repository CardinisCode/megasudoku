import pygame



# initialise the pygame font
pygame.font.init()
 
# Total window
screen = pygame.display.set_mode((750, 900))

# Title and Icon
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
img = pygame.image.load('icon2.png')
pygame.display.set_icon(img)
 
x = 0
y = 0
dif = 750 / 25
val = 0
input_number = ""
original_problem = "5x5_default.csv"
# Default Sudoku Board (9x9).


def load_grid(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [[int(i) for i in x.split(',')] for x in lines]

def save_grid(filename, local_grid):
    with open("%s_%s" % (filename, "save"), 'w') as f:
        for line in local_grid:
            csv = ','.join([str(s) for s in line])
            f.write("%s\n" % csv)

grid = load_grid(original_problem)

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 20)
font2 = pygame.font.SysFont("comicsans", 20)
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif

# Highlight the cell selected
def draw_box():
    #7 = block thickness
    

    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 3)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 3)  

# Function to draw required lines for making Sudoku grid        
def draw():
    # Draw the lines
        
    for j in range (25): #rows across
        for i in range (25): # Columns down
            if grid[j][i]!= 0:
 
                # Fill blue color in already numbered grid
                pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))
 
                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[j][i]), 1, (0, 0, 0))
                screen.blit(text1, (i * dif + 3, j * dif + 3))

    # Draw lines horizontally and vertically to form grid          
    for i in range(26):
        if i % 5 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (750, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 750), thick)     

# Fill value entered in cell     
def draw_val(val):
    
    text1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(text1, (x * dif + 3, y * dif + 3))   
 
# Raise error when wrong value entered
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
    screen.blit(text1, (20, 820)) 
def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 820)) 
 
# Check if the value entered in board is valid
def valid(m, i, j, val):
    for it in range(25):
        if m[i][it]== val:
            return False
        if m[it][j]== val:
            return False
    it = i//5
    jt = j//5
    for i in range(it * 5, it * 5 + 5):
        for j in range (jt * 5, jt * 5 + 5):
            if m[i][j]== val:
                return False
    
    return True


# Solves the sudoku board using Backtracking Algorithm
def solve(grid, i, j):
     
    while grid[i][j]!= 0:
        if i<24:
            i+= 1
        elif i == 24 and j<24:
            i = 0
            j+= 1
        elif i == 24 and j == 24:
            return True
    pygame.event.pump()   
    for it in range(1, 26):
        if valid(grid, i, j, it)== True:
            grid[i][j]= it
            global x, y
            x = i
            y = j
            # white color background\
            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j)== 1:
                return True
            else:
                grid[i][j]= 0
            # white color background\
            screen.fill((255, 255, 255))
         
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(50)   
    return False 

# Display instruction for the game
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    text3 = font2.render("PRESS S TO SAVE AND PRESS L TO LOAD", 1, (0, 0, 0))
    screen.blit(text1, (20, 780))       
    screen.blit(text2, (20, 800))
    screen.blit(text3, (20, 820))

# Display options when solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    screen.blit(text1, (20, 820))
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0
# The loop thats keep the window running
while run:
     
    # White color background
    screen.fill((255, 255, 255))
    # Loop through the events stored in event.get()
    for event in pygame.event.get():
        # Quit the game window
        if event.type == pygame.QUIT:
            run = False 
        # Get the mouse position to insert number   
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        # Get the number to be inserted if key pressed   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1 
            if event.key == pygame.K_0:
                input_number += "0" 
            if event.key == pygame.K_1:
                input_number += "1"
            if event.key == pygame.K_2:
                input_number += "2"   
            if event.key == pygame.K_3:
                input_number += "3"
            if event.key == pygame.K_4:
                input_number += "4"
            if event.key == pygame.K_5:
                input_number += "5"
            if event.key == pygame.K_6:
                input_number += "6"
            if event.key == pygame.K_7:
                input_number += "7"
            if event.key == pygame.K_8:
                input_number += "8"
            if event.key == pygame.K_9:
                input_number += "9" 

            if event.key == pygame.K_s:
                save_grid(original_problem, grid)

            if event.key == pygame.K_l:
                grid = load_grid("%s_%s" % (original_problem, "save"))

            if event.key == pygame.K_RETURN: # auto solve
                flag2 = 1  
            # If R pressed clear the sudoku board
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid =[
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #3
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #4
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #8
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #9
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #10
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #11
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #12
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #13
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #14
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #15
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #16
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #17
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #18
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #19
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #20
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #21
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #22
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #23
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #24
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #25
                ]
            # If D is pressed reset the board to default
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                flag2 = 0
                grid =[
                    [0, 19, 24, 7, 0, 0, 18, 1, 16, 0, 0, 25, 22, 10, 0, 0, 6, 21, 13, 0, 0, 8, 5, 9, 0],
                    [9, 0, 0, 0, 20, 23, 0, 0, 13, 0, 1, 0, 0, 0, 4, 0, 22, 0, 0, 7, 14, 0, 0, 0, 6],
                    [6, 0, 17, 0, 21, 10, 0, 0, 0, 8, 0, 0, 5, 0, 0, 3, 0, 0, 0, 4, 20, 0, 18, 0, 25],
                    [10, 0, 0, 0, 23, 0, 24, 0, 0, 25, 8, 16, 0, 17, 18, 9, 0, 0, 19, 0, 22, 0, 0, 0, 2],
                    [0, 22, 25, 8, 0, 0, 6, 4, 14, 0, 0, 9, 0, 13, 0, 0, 1, 10, 12, 0, 0, 24, 23, 19, 0],
                    [0, 12, 5, 25, 0, 0, 8, 6, 4, 0, 0, 15, 21, 18, 0, 0, 3, 24, 11, 0, 0, 14, 22, 20, 0],
                    [22, 0, 0, 16, 19, 14, 25, 0, 0, 2, 5, 8, 0, 20, 9, 21, 0, 0, 17, 18, 23, 4, 0, 0, 15],
                    [13, 0, 0, 0, 10, 0, 0, 0, 0, 24, 2, 0, 12, 0, 16, 1, 0, 0, 0, 0, 25, 0, 0, 0, 5],
                    [7, 14, 0, 0, 8, 15, 0, 0, 1, 12, 4, 6, 0, 24, 13, 10, 5, 0, 0, 19, 18, 0, 0, 17, 9],
                    [0, 20, 21, 9, 0, 0, 23, 5, 17, 0, 0, 10, 0, 19, 0, 0, 25, 4, 2, 0, 0, 16, 1, 13, 0],
                    [0, 17, 7, 13, 0, 0, 20, 12, 23, 0, 0, 19, 0, 3, 0, 0, 14, 25, 21, 0, 0, 5, 15, 2, 0],
                    [24, 0, 0, 0, 4, 22, 0, 0, 0, 6, 21, 0, 0, 0, 25, 5, 0, 0, 0, 1, 17, 0, 0, 0, 19],
                    [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13],
                    [21, 0, 0, 0, 15, 19, 0, 0, 0, 9, 13, 0, 0, 0, 12, 2, 0, 0, 0, 8, 1, 0, 0, 0, 3],
                    [0, 10, 20, 19, 0, 0, 2, 15, 24, 0, 0, 1, 0, 5, 0, 0, 23, 22, 18, 0, 0, 6, 16, 4, 0],
                    [0, 5, 22, 24, 0, 0, 17, 13, 25, 0, 0, 7, 0, 2, 0, 0, 18, 16, 6, 0, 0, 9, 8, 21, 0],
                    [8, 3, 0, 0, 14, 5, 0, 0, 2, 22, 25, 23, 0, 6, 17, 4, 20, 0, 0, 13, 7, 0, 0, 15, 16],
                    [11, 0, 0, 0, 9, 0, 0, 0, 0, 16, 3, 0, 24, 0, 20, 14, 0, 0, 0, 0, 5, 0, 0, 0, 22],
                    [16, 0, 0, 17, 25, 18, 19, 0, 0, 23, 12, 21, 0, 4, 10, 22, 0, 0, 9, 11, 13, 3, 0, 0, 20],
                    [0, 4, 6, 23, 0, 0, 1, 24, 20, 0, 0, 22, 15, 9, 0, 0, 21, 17, 3, 0, 0, 12, 25, 11, 0],
                    [0, 15, 19, 6, 0, 0, 16, 14, 8, 0, 0, 5, 0, 25, 0, 0, 11, 2, 23, 0, 0, 18, 20, 22, 0],
                    [14, 0, 0, 0, 24, 0, 12, 0, 0, 18, 20, 11, 0, 1, 2, 25, 0, 0, 5, 0, 19, 0, 0, 0, 23],
                    [5, 0, 9, 0, 2, 24, 0, 0, 0, 20, 0, 0, 17, 0, 0, 6, 0, 0, 0, 21, 12, 0, 7, 0, 1],
                    [17, 0, 0, 0, 16, 25, 0, 0, 19, 0, 9, 0, 0, 0, 24, 0, 7, 0, 0, 22, 6, 0, 0, 0, 21],
                    [0, 8, 3, 18, 0, 0, 15, 2, 21, 0, 0, 4, 19, 16, 0, 0, 19, 9, 1, 0, 0, 25, 13, 14, 0],
                ]

    if flag2 == 1:
        try:
            val = int(input_number)
            print(val)
        except:
            pass
        input_number = ""
        flag2 = 0   
    if val != 0:           
        draw_val(val)
        if valid(grid, int(y), int(x), val)== True:
            grid[int(y)][int(x)]= val
            flag1 = 0
        else:
            grid[int(y)][int(x)]= 0
            raise_error2()  
        val = 0   
       
    if error == 1:
        raise_error1() 
    if rs == 1:
        result()       
    draw() 
    if flag1 == 1:
        draw_box()      
    instruction()   
 
    # Update window
    pygame.display.update() 
 
# Quit pygame window   
pygame.quit()    


