import pygame, sys, random

def smiley_hover():
    #Smiley icon

    if 842 <= pygame.mouse.get_pos()[0] <= 930 and 10 <= pygame.mouse.get_pos()[1] <= 98:
        pygame.draw.rect(screen, GREY, pygame.Rect(842, 10, 88, 88)) 
        pygame.draw.rect(screen, BOARD, pygame.Rect(848, 16, 88, 88)) 
    else:
        pygame.draw.rect(screen, BOARD, pygame.Rect(842, 10, 88, 88)) 
        pygame.draw.rect(screen, GREY, pygame.Rect(848, 16, 88, 88)) 

    if game_won == False and game_failed == False:
        pygame.draw.rect(screen, BACKGROUND, pygame.Rect(848, 16, 82, 82)) 
        pygame.draw.rect(screen, YELLOW, pygame.Rect(864, 32, 50, 50)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(864, 24, 50, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(864, 82, 50, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(856, 32, 8, 50)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(914, 32, 8, 50)) 

        pygame.draw.rect(screen, BLACK, pygame.Rect(877, 42, 8, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(893, 42, 8, 8)) 

        pygame.draw.rect(screen, BLACK, pygame.Rect(877, 66, 24, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(869, 58, 8, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(901, 58, 8, 8)) 
    elif game_won == True:
        pygame.draw.rect(screen, BACKGROUND, pygame.Rect(848, 16, 82, 82)) 
        pygame.draw.rect(screen, YELLOW, pygame.Rect(864, 32, 50, 50)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(864, 24, 50, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(864, 82, 50, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(856, 32, 8, 50)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(914, 32, 8, 50)) 

        pygame.draw.rect(screen, BLACK, pygame.Rect(869, 40, 16, 12)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(893, 40, 16, 12)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(864, 44, 50, 4)) 

        pygame.draw.rect(screen, BLACK, pygame.Rect(877, 66, 24, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(869, 58, 8, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(901, 58, 8, 8)) 
    elif game_failed == True:
        pygame.draw.rect(screen, BACKGROUND, pygame.Rect(848, 16, 82, 82)) 
        pygame.draw.rect(screen, YELLOW, pygame.Rect(864, 32, 50, 50)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(864, 24, 50, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(864, 82, 50, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(856, 32, 8, 50)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(914, 32, 8, 50)) 

        pygame.draw.rect(screen, BLACK, pygame.Rect(879, 46, 4, 4)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(883, 50, 4, 4)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(875, 42, 4, 4))
        pygame.draw.rect(screen, BLACK, pygame.Rect(875, 50, 4, 4))
        pygame.draw.rect(screen, BLACK, pygame.Rect(883, 42, 4, 4))

        pygame.draw.rect(screen, BLACK, pygame.Rect(895, 46, 4, 4)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(899, 50, 4, 4)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(891, 42, 4, 4))
        pygame.draw.rect(screen, BLACK, pygame.Rect(891, 50, 4, 4))
        pygame.draw.rect(screen, BLACK, pygame.Rect(899, 42, 4, 4))

        pygame.draw.rect(screen, BLACK, pygame.Rect(877, 66, 24, 8)) 

def bigred_number(num, top, left):
    #Display the two red clocks on top

    three_d = [num//100, (num - (num//100*100))//10, num%10]

    for d in range(3):
        for i in range(15):

            d_row = i%5
            d_col = i//5

            if digits[three_d[d]][i] >= 0:
                
                if digits[three_d[d]][i] == 1:
                    d_colour = RED
                elif digits[three_d[d]][i] == 0:
                    d_colour = RED_DARK

                pygame.draw.rect(screen, d_colour, pygame.Rect(left + 8+ 44*d + d_col*13, top + 8 + d_row * 16, 12, 15))

def draw_new_board():
    #Start over
    for i in range(0, 480):
        row_i = i//30
        column_i = i%30
        pygame.draw.rect(screen, (152, 152, 146), pygame.Rect(20+column_i*58, 124+row_i*58, 56, 56)) #(162, 162, 152)
        pygame.draw.rect(screen, COVEREDSQCOLOUR, pygame.Rect(20+column_i*58, 124+row_i*58, 54, 54))

def new_board(mines): 

    mines = [[0] * 30 for _ in range(16)]

    #Ensure the right number of mines
    while sum([sum(i) for i in zip(*mines)]) != mines_num:
        rand_row = random.randint(0, 15)
        rand_col = random.randint(0, 29)
        if mines[rand_row][rand_col] == 0:
            mines[rand_row][rand_col] = 1

    return mines

def determine_numbers(mines, numbers):
    #Calculate the 1-8 numbers

    numbers = [[0] * 30 for _ in range(16)]

    for ir2 in range(16):
        for ic2 in range(30):
            if mines[ir2][ic2] == 1:
                numbers[ir2][ic2] = 9
            else:
                numbers[ir2][ic2] = neighbours(ir2, ic2, mines)
    return numbers

def neighbours(row1, col1, mines):
    #Check number of mine neighbours
    nb_count = 0
    for (xx, yy) in ((row1-1, col1-1), (row1, col1-1), (row1+1, col1-1), (row1-1, col1), (row1+1, col1), (row1-1, col1+1), (row1, col1+1), (row1+1, col1+1)):
        if 0 <= xx <= 15 and 0 <= yy <= 29:
            if mines[xx][yy] == 1:
                nb_count += 1
    return nb_count
    
def recognize_sq():
    cur_x = (pygame.mouse.get_pos()[0] - 20)//58
    cur_y = (pygame.mouse.get_pos()[1] - 124)//58
    pygame.draw.rect(screen, (162, 162, 152), pygame.Rect(20+cur_x*58, 124+cur_y*58, 56, 56))
    pygame.draw.rect(screen, (218, 218, 208), pygame.Rect(20+cur_x*58, 124+cur_y*58, 54, 54))

def drawing_number(number, sqx, sqy):
    #Square graphics
    pygame.draw.rect(screen, SQUARECOLOUR, pygame.Rect(20+sqx*58, 124+sqy*58, 56, 56))
    if number == 0:
        pass

    if number == 1:
        pygame.draw.rect(screen, C1, pygame.Rect(20+17+sqx*58, 124+15+sqy*58, 17, 8))
        pygame.draw.rect(screen, C1, pygame.Rect(20+26+sqx*58, 124+9+sqy*58, 8, 30))
        pygame.draw.rect(screen, C1, pygame.Rect(20+23+sqx*58, 124+21+sqy*58, 3, 17))
        pygame.draw.rect(screen, C1, pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))

    if number == 2:
        pygame.draw.rect(screen, C2, pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C2, pygame.Rect(20+35+sqx*58, 124+16+sqy*58, 8, 8))
        pygame.draw.rect(screen, C2, pygame.Rect(20+13+sqx*58, 124+23+sqy*58, 30, 8))
        pygame.draw.rect(screen, C2, pygame.Rect(20+13+sqx*58, 124+31+sqy*58, 8, 8))
        pygame.draw.rect(screen, C2, pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))

    if number == 3:
        pygame.draw.rect(screen, C3, pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C3, pygame.Rect(20+35+sqx*58, 124+16+sqy*58, 8, 22))
        pygame.draw.rect(screen, C3, pygame.Rect(20+19+sqx*58, 124+23+sqy*58, 24, 8))
        pygame.draw.rect(screen, C3, pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))

    if number == 4:
        pygame.draw.rect(screen, C4, pygame.Rect(20+32+sqx*58, 124+9+sqy*58, 10, 37))
        pygame.draw.rect(screen, C4, pygame.Rect(20+14+sqx*58, 124+23+sqy*58, 28, 8))
        pygame.draw.rect(screen, C4, pygame.Rect(20+18+sqx*58, 124+9+sqy*58, 8, 16))

    if number == 5:
        pygame.draw.rect(screen, C5, pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C5, pygame.Rect(20+13+sqx*58, 124+16+sqy*58, 8, 8))
        pygame.draw.rect(screen, C5, pygame.Rect(20+13+sqx*58, 124+23+sqy*58, 30, 8))
        pygame.draw.rect(screen, C5, pygame.Rect(20+35+sqx*58, 124+31+sqy*58, 8, 8))
        pygame.draw.rect(screen, C5, pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))

    if number == 6:
        pygame.draw.rect(screen, C6, pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C6, pygame.Rect(20+13+sqx*58, 124+16+sqy*58, 8, 22))
        pygame.draw.rect(screen, C6, pygame.Rect(20+13+sqx*58, 124+23+sqy*58, 30, 8))
        pygame.draw.rect(screen, C6, pygame.Rect(20+35+sqx*58, 124+31+sqy*58, 8, 8))
        pygame.draw.rect(screen, C6, pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))
    
    if number == 7:
        pygame.draw.rect(screen, C7, pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C7, pygame.Rect(20+35+sqx*58, 124+16+sqy*58, 8, 30))
    
    if number == 8:
        pygame.draw.rect(screen, C8, pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C8, pygame.Rect(20+13+sqx*58, 124+16+sqy*58, 8, 22))
        pygame.draw.rect(screen, C8, pygame.Rect(20+13+sqx*58, 124+23+sqy*58, 30, 8))
        pygame.draw.rect(screen, C8, pygame.Rect(20+35+sqx*58, 124+16+sqy*58, 8, 22))
        pygame.draw.rect(screen, C8, pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))

    if number == "M":
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+15+sqx*58, 124+15+sqy*58, 26, 26))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+11+sqx*58, 124+19+sqy*58, 34, 18))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+19+sqx*58, 124+11+sqy*58, 18, 34))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+26+sqx*58, 124+7+sqy*58, 4, 42))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+7+sqx*58, 124+26+sqy*58, 42, 4))
        pygame.draw.rect(screen, BOARD, pygame.Rect(20+22+sqx*58, 124+18+sqy*58, 4, 4))

    if number == "F":
        pygame.draw.rect(screen, (162, 162, 152), pygame.Rect(20+sqx*58, 124+sqy*58, 56, 56))
        pygame.draw.rect(screen, COVEREDSQCOLOUR, pygame.Rect(20+sqx*58, 124+sqy*58, 54, 54))
        pygame.draw.rect(screen, C3, pygame.Rect(20+10+sqx*58, 124+15+sqy*58, 6, 6))
        pygame.draw.rect(screen, C3, pygame.Rect(20+16+sqx*58, 124+12+sqy*58, 12, 12))
        pygame.draw.rect(screen, C3, pygame.Rect(20+22+sqx*58, 124+8+sqy*58, 12, 22))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+28+sqx*58, 124+30+sqy*58, 6, 6))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+18+sqx*58, 124+36+sqy*58, 20, 6))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+13+sqx*58, 124+40+sqy*58, 30, 8))
    
    if number == "E":
        pygame.draw.rect(screen, RED_BRIGHT, pygame.Rect(20+sqx*58, 124+sqy*58, 56, 56))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+15+sqx*58, 124+15+sqy*58, 26, 26))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+11+sqx*58, 124+19+sqy*58, 34, 18))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+19+sqx*58, 124+11+sqy*58, 18, 34))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+26+sqx*58, 124+7+sqy*58, 4, 42))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+7+sqx*58, 124+26+sqy*58, 42, 4))
        pygame.draw.rect(screen, BOARD, pygame.Rect(20+22+sqx*58, 124+18+sqy*58, 4, 4))

    if number == "X":
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+15+sqx*58, 124+15+sqy*58, 26, 26))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+11+sqx*58, 124+19+sqy*58, 34, 18))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+19+sqx*58, 124+11+sqy*58, 18, 34))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+26+sqx*58, 124+7+sqy*58, 4, 42))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+7+sqx*58, 124+26+sqy*58, 42, 4))
        pygame.draw.rect(screen, BOARD, pygame.Rect(20+22+sqx*58, 124+18+sqy*58, 4, 4))

        for s1 in range(11):
            pygame.draw.rect(screen, RED, pygame.Rect(20+6+sqx*58+s1*4, 124+6+sqy*58+s1*4, 4, 4))
        for s2 in range(11):
            pygame.draw.rect(screen, RED, pygame.Rect(20+6+sqx*58-s2*4+40, 124+6+sqy*58+s2*4, 4, 4))
        
def reset_clickmap():
    for i in range(0, 480):
        row_i = i//30
        column_i = i%30
        click_map[row_i][column_i] = 0

    return click_map

def show_squares(sqx, sqy):
    #When opening up an empty square

    display_area = []
    display_area.append([sqx, sqy])
    all_neighbours = []

    #Find all connecting empty squares
    found_sth = True
    while found_sth == True:

        found_list = [0]
        for i1 in display_area:
            for (xx, yy) in ((i1[0], i1[1]-1), (i1[0], i1[1]+1), (i1[0]-1, i1[1]), (i1[0]+1, i1[1])):
                if 0 <= xx <= 15 and 0 <= yy <= 29:
                    if numbers[xx][yy] == 0 and [xx, yy] not in display_area:
                        display_area.append([xx, yy])
                        found_list.append(1)
        
        if sum(found_list) < 1:
            found_sth = False
    
    #Find all neighbours of those empty squares
    for i2 in display_area:
        all_neighbours.append(i2)
        for (xx1, yy1) in ((i2[0], i2[1]-1), (i2[0], i2[1]+1), (i2[0]-1, i2[1]), (i2[0]+1, i2[1]), (i2[0]-1, i2[1]-1), (i2[0]-1, i2[1]+1), (i2[0]+1, i2[1]-1), (i2[0]+1, i2[1]+1)):
            if 0 <= xx1 <= 15 and 0 <= yy1 <= 29:
                all_neighbours.append([xx1, yy1])

    #Add unique neighbours (the "shell")
    for i3 in all_neighbours:
        if 0 < numbers[i3[0]][i3[1]] < 9 and i3 not in display_area:
            display_area.append(i3)
    
    #Display entire blank area + "shell"
    for i4 in display_area:
        #Ignore flagged non-mines for next step
        if click_map[i4[0]][i4[1]] == 2 and numbers[i4[0]][i4[1]] != 9:
            pass
        #Normal cases
        else:
            click_map[i4[0]][i4[1]] = 1
            drawing_number(numbers[i4[0]][i4[1]], i4[1], i4[0])

    #Display the wrongly flagged non mines if lost
    if game_failed == True:
        for ir2 in range(16):
            for ic2 in range(30):
                if numbers[ir2][ic2] == 0 and click_map[ir2][ic2] == 2:
                    drawing_number("X", ic2, ir2)
    
def mid_click(sqx, sqy):

    #Try to open up all neighbours when middle-clicking an opened number

    mid_num = numbers[sqx][sqy]
    flag_num = 0
    flagged = []

    #Check the number of flagged squares around
    for (xx, yy) in ((sqx-1, sqy-1), (sqx, sqy-1), (sqx+1, sqy-1), (sqx-1, sqy), (sqx+1, sqy), (sqx-1, sqy+1), (sqx, sqy+1), (sqx+1, sqy+1)):
        if 0 <= xx <= 15 and 0 <= yy <= 29:
            if click_map[xx][yy] == 2:
                flagged.append([xx, yy])
                flag_num += 1
    
    #Flags match the number of the square in question
    if flag_num == mid_num:
        for (xx, yy) in ((sqx-1, sqy-1), (sqx, sqy-1), (sqx+1, sqy-1), (sqx-1, sqy), (sqx+1, sqy), (sqx-1, sqy+1), (sqx, sqy+1), (sqx+1, sqy+1)):
            if 0 <= xx <= 15 and 0 <= yy <= 29:
                #Try to open up unopened squares
                if click_map[xx][yy] == 0:
                    #Not a mine and not empty
                    if 0 < numbers[xx][yy] < 9:
                        drawing_number(numbers[xx][yy], yy, xx)
                        click_map[xx][yy] = 1

                        global game_won
                        global game_on

                        #Won?
                        count_of_1 = 0
                        for xx1 in click_map:
                            count_of_1 += xx1.count(1)
                        if count_of_1 + static_mines_num == 480:
                            game_won = True
                            game_on = False

                    #One of the neighbours is empty - need to check if there's more to open
                    elif numbers[xx][yy] == 0:
                        show_squares(xx, yy)

                    #One of the neighbours is a mine - game over
                    elif numbers[xx][yy] == 9:
                        global game_failed

                        game_failed = True
                        game_on = False

                        for ir2 in range(16):
                            for ic2 in range(30):
                                #Show all mines
                                if numbers[ir2][ic2] == 9:
                                    drawing_number("M", ic2, ir2)
                                
                        #Show the wrongly flagged squares
                        for irx in flagged:
                            if numbers[irx[0]][irx[1]] != 9:
                                drawing_number("X", irx[1], irx[0])
                        
                        #Wrongly flagged
                        for ir2 in range(16):
                            for ic2 in range(30):
                                if numbers[ir2][ic2] == 0 and click_map[ir2][ic2] == 2:
                                    drawing_number("X", ic2, ir2)

    #Flag number doesn't match number of square in question - light up the unopened as a reminder                 
    else:
        for (xx, yy) in ((sqx-1, sqy-1), (sqx, sqy-1), (sqx+1, sqy-1), (sqx-1, sqy), (sqx+1, sqy), (sqx-1, sqy+1), (sqx, sqy+1), (sqx+1, sqy+1)):
            if 0 <= xx <= 15 and 0 <= yy <= 29:
                if click_map[xx][yy] == 0:
                    pygame.draw.rect(screen, (162, 162, 152), pygame.Rect(20+yy*58, 124+xx*58, 56, 56))
                    pygame.draw.rect(screen, (182, 182, 172), pygame.Rect(20+yy*58, 124+xx*58, 54, 54))
                    pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((1778, 1070))
clock = pygame.time.Clock()
pygame.display.set_caption('Minesweeper')

#Colours
BACKGROUND = (202, 202, 196)
BOARD = (232, 232, 222)
COVEREDSQCOLOUR = (202, 202, 192)
SQUARECOLOUR = (212, 212, 202)
GREY = (132, 132, 128)
BLACK = (26, 36, 46)

RED = (200, 22, 28)
RED_DARK = (66, 22, 26)
RED_BRIGHT = (210, 56, 24)

YELLOW = (236, 212, 82)

C1 = (50, 112, 172)
C2 = (76, 128, 68)
C3 = (200, 22, 28)
C4 = (0, 62, 116)
C5 = (126, 68, 58)
C6 = (80, 146, 150)
C7 = (56, 56, 52)
C8 = (132, 132, 128)

#Background and game area
pygame.draw.rect(screen, BACKGROUND, pygame.Rect(0, 0, 1778, 1070))
pygame.draw.rect(screen, BOARD, pygame.Rect(10, 114, 1758, 946))
#Two red clocks 
pygame.draw.rect(screen, BLACK, pygame.Rect(10, 10, 142, 94)) 
pygame.draw.rect(screen, BLACK, pygame.Rect(1626, 10, 142, 94))  

digits = [[1,1,1,1,1,1,-1,0,-1,1,1,1,1,1,1], [0,0,0,0,0,0,-1,0,-1,0,1,1,1,1,1], [1,0,1,1,1,1,-1,1,-1,1,1,1,1,0,1], [1,0,1,0,1,1,-1,1,-1,1,1,1,1,1,1], [1,1,1,0,0,0,-1,1,-1,0,1,1,1,1,1],
          [1,1,1,0,1,1,-1,1,-1,1,1,0,1,1,1], [1,1,1,1,1,1,-1,1,-1,1,1,0,1,1,1], [1,0,0,0,0,1,-1,0,-1,0,1,1,1,1,1], [1,1,1,1,1,1,-1,1,-1,1,1,1,1,1,1], [1,1,1,0,1,1,-1,1,-1,1,1,1,1,1,1]]

mines = []
numbers = []
click_map = []

mines_num = 99
static_mines_num = 99
global game_on
game_on = False
game_won = False
game_failed = False
time_elapsed = 0
bigred_number(0, 10, 1626)
click_pair = []
flagged_sq = []
opened_sq = 0

#Initial setup
draw_new_board()
mines = new_board(mines)
numbers = determine_numbers(mines, numbers)

click_map = []
while len(click_map) < 16:
    click_map.append([])
for rowc in click_map:
    while len(rowc) < 30:
        rowc.append(0)
mouse_down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            click_pair = []

            #Redraw all unopened & unflagged squares
            if game_on == True:
                for cx in range(16):
                    for cy in range(30):
                        if click_map[cx][cy] == 0:
                            pygame.draw.rect(screen, (162, 162, 152), pygame.Rect(20+cy*58, 124+cx*58, 56, 56))
                            pygame.draw.rect(screen, COVEREDSQCOLOUR, pygame.Rect(20+cy*58, 124+cx*58, 54, 54))

        #Clicking Smiley
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.button != 3 and 842 <= pygame.mouse.get_pos()[0] <= 930 and 10 <= pygame.mouse.get_pos()[1] <= 98:
        
            #Reset
            game_won = False
            game_failed = False
            game_on = False
            time_elapsed = 0
            mines_num = 99
            #mines_num = 399

            bigred_number(0, 10, 1626)
            draw_new_board()
            mines = new_board(mines)
            numbers = determine_numbers(mines, numbers)
            reset_clickmap()
            flagged_sq = []
            #opened_sq = 0

        #Clicking any square
        if event.type == pygame.MOUSEBUTTONDOWN and 20 <= pygame.mouse.get_pos()[0] <= 1758 and 124 <= pygame.mouse.get_pos()[1] <= 1050:

            #Game still on
            if game_won == False and game_failed == False:
                sqy = (pygame.mouse.get_pos()[0] - 20)//58
                sqx = (pygame.mouse.get_pos()[1] - 124)//58

                #Left click
                if event.button == 1:
                    click_pair.append(1)

                    #Opened and double clicking
                    if click_map[sqx][sqy] == 1 and click_pair[0] == 3:
                        mid_click(sqx, sqy)

                    #Unopen and single click
                    elif click_map[sqx][sqy] == 0 and len(click_pair) == 1:
                        #Not mine
                        if numbers[sqx][sqy] != 9:
                            #Start clock
                            if game_on == False:
                                game_on = True
                            #Empty square
                            if numbers[sqx][sqy] == 0:
                                show_squares(sqx, sqy)
                            #Number
                            else:
                                drawing_number(numbers[sqx][sqy], sqy, sqx)
                                click_map[sqx][sqy] = 1

                                #Won?
                                count_of_1 = 0
                                for xx1 in click_map:
                                    count_of_1 += xx1.count(1)
                                #If all non-mine squares opened
                                if count_of_1 + static_mines_num == 480:
                                    game_won = True
                                    game_on = False
                        #Clicked mine
                        else:

                            #Clicked mine on new game => Automatically setup a new game to avoid this
                            ########
                            if sum([sum(i) for i in zip(*click_map)]) == 0:

                                #While the first click of the game is a mine -- keeps resetting
                                while numbers[sqx][sqy] == 9:

                                    bigred_number(0, 10, 1626)

                                    game_won, game_failed, game_on = False, False, True
                                    time_elapsed = 0
                                    mines_num = 99

                                    draw_new_board()
                                    mines = new_board(mines)
                                    numbers = determine_numbers(mines, numbers)
                                    reset_clickmap()
                                    flagged_sq = []

                                    if numbers[sqx][sqy] == 0:
                                        show_squares(sqx, sqy)
                                    else:
                                        drawing_number(numbers[sqx][sqy], sqy, sqx)
                                        click_map[sqx][sqy] = 1
                            ########

                            else:
                                for ir2 in range(16):
                                    for ic2 in range(30):
                                        #Show all mines
                                        if numbers[ir2][ic2] == 9:
                                            if click_map[ir2][ic2] == 0: ### Added so that when hit a mine the correctly flagged ones don't change
                                                drawing_number("M", ic2, ir2)
                                        #Wrongly flagged
                                        if click_map[ir2][ic2] == 2 and numbers[ir2][ic2] != 9:
                                            drawing_number("X", ic2, ir2)

                                #Exploded
                                drawing_number("E", sqy, sqx)
                                #Game over
                                game_failed = True
                                game_on = False

                #Right click
                if event.button == 3:
                    click_pair.append(3)
                    #Opened and double clicking
                    if click_map[sqx][sqy] == 1 and click_pair[0] == 1:
                        mid_click(sqx, sqy)
                    #Unopen and single click
                    elif len(click_pair) == 1:
                        if click_map[sqx][sqy] == 0:
                            #Can still flag
                            if mines_num > 0:
                                drawing_number("F", sqy, sqx)
                                click_map[sqx][sqy] = 2
                                flagged_sq.append([sqx, sqy])
                                #print("flagged_sq","#", len(flagged_sq) ,"#",flagged_sq)
                                mines_num -= 1
                                #Possibly flagged all mines
                                if mines_num == 0:
                                    exception_num = 0
                                    for ch1 in flagged_sq:
                                        if numbers[ch1[0]][ch1[1]] != 9:
                                            exception_num += 1
                                    #All flagged squares are indeed mines
                                    if exception_num == 0:
                                        game_won = True
                                        game_on = False

                        #Remove flag when already flagged
                        elif click_map[sqx][sqy] == 2:
                            pygame.draw.rect(screen, (152, 152, 146), pygame.Rect(20+sqy*58, 124+sqx*58, 56, 56))
                            pygame.draw.rect(screen, COVEREDSQCOLOUR, pygame.Rect(20+sqy*58, 124+sqx*58, 54, 54))
                            click_map[sqx][sqy] = 0
                            mines_num += 1      
                            flagged_sq.remove([sqx, sqy]) 

                #Clicking scroll wheel
                if event.button == 2:
                    if 0 < numbers[sqx][sqy] < 9 and click_map[sqx][sqy] == 1:
                        mid_click(sqx, sqy)
        
        #For testing - could be a cheat
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #print("numbers")
                for x2 in numbers:
                    print(x2)
                print(" ")
                for x3 in click_map:
                    print(x3)

    bigred_number(mines_num, 10, 10)

    smiley_hover()

    pygame.display.update()

    #Game clock
    if game_on == True:
        time_elapsed += 1/30
        bigred_number(int(time_elapsed), 10, 1626)

        #Time's up
        if time_elapsed > 999:
            game_failed = True
            game_on = False

    clock.tick(30)
