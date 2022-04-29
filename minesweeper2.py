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

def auto_solver_hover():
    #Auto solver icon

    if 1626 <= pygame.mouse.get_pos()[0] <= 1762 and 10 <= pygame.mouse.get_pos()[1] <= 98:
        pygame.draw.rect(screen, GREY, pygame.Rect(1674, 10, 88, 88)) 
        pygame.draw.rect(screen, BOARD, pygame.Rect(1680, 16, 88, 88)) 
    else:
        pygame.draw.rect(screen, BOARD, pygame.Rect(1674, 10, 88, 88)) 
        pygame.draw.rect(screen, GREY, pygame.Rect(1680, 16, 88, 88)) 
    
    pygame.draw.rect(screen, BACKGROUND, pygame.Rect(1680, 16, 82, 82)) 

    if auto_solve:
        FACE = ROBOT_ON
        EYES = ROBOT_EYE_ON

        pygame.draw.rect(screen, BLACK, pygame.Rect(1544+152+3, 82+4-2, 8, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(1544+152+3+12, 82+4-2, 8, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(1544+152+3+24, 82+4-2, 8, 8)) 
        pygame.draw.rect(screen, BLACK, pygame.Rect(1544+152+3+36, 82+4-2, 8, 8)) 

    else:
        FACE = ROBOT_OFF
        EYES = ROBOT_EYE_OFF

        pygame.draw.rect(screen, BACKGROUND, pygame.Rect(1544+152+3, 82+4-2, 44, 8)) 

    pygame.draw.rect(screen, FACE, pygame.Rect(1544+152, 32+8-2, 50, 50-16)) 
    pygame.draw.rect(screen, EYES, pygame.Rect(1552+152, 46-8+8-2, 12, 8)) 
    pygame.draw.rect(screen, EYES, pygame.Rect(1574+152, 46-8+8-2, 12, 8)) 
    pygame.draw.rect(screen, EYES, pygame.Rect(1556+152, 60-8+8-2, 26, 8)) 

    pygame.draw.rect(screen, BLACK, pygame.Rect(1544+152+8, 16+8-2, 8, 8)) 
    pygame.draw.rect(screen, BLACK, pygame.Rect(1544+152+34, 16+8-2, 8, 8)) 

    pygame.draw.rect(screen, BLACK, pygame.Rect(1544+152, 24+8-2, 50, 8)) 
    pygame.draw.rect(screen, BLACK, pygame.Rect(1544+152, 82-16+8-2, 50, 8)) 
    pygame.draw.rect(screen, BLACK, pygame.Rect(1536+152, 32+8-2, 8, 34)) 
    pygame.draw.rect(screen, BLACK, pygame.Rect(1594+152, 32+8-2, 8, 34)) 

def open_check(auto_hover_pair):
    ax, ay = auto_hover_pair[0], auto_hover_pair[1]
    open_list = []
    hidden_list = []
    flagged_list = []
    neighbour_ct = 0
    for (x, y) in ((ax+1, ay), (ax-1, ay), (ax, ay+1), (ax, ay-1), (ax+1, ay+1), (ax+1, ay-1), (ax-1, ay+1), (ax-1, ay-1)):
        if 0 <= x < 16 and 0 <= y < 30:
            neighbour_ct += 1
            if click_map[x][y] == 0:
                hidden_list.append([x, y])
            elif click_map[x][y] == 1:
                open_list.append([x, y])
            else:
                flagged_list.append([x, y])
    return neighbour_ct, open_list, hidden_list, flagged_list

def auto_flag(mines_num, hidden_list, auto_mines, auto = False):
    if auto == False:
        for pt1 in hidden_list:
            auto_mines -= 1
            click_map[pt1[0]][pt1[1]] = 2
            flagged_sq.append([pt1[0], pt1[1]])
    else:
        for pt1 in hidden_list:
            drawing_number("F", pt1[1], pt1[0], auto)
            mines_num -= 1

    return mines_num, auto_mines

def auto_open(hidden_list, possible, full_sequence, auto = False):
    for pt2 in hidden_list:
        if numbers[pt2[0]][pt2[1]] == 0:
            show_squares(pt2[0], pt2[1], possible, full_sequence, True)
        else:
            if auto == False:
                drawing_number(numbers[pt2[0]][pt2[1]], pt2[1], pt2[0], auto)
            click_map[pt2[0]][pt2[1]] = 1

def triple_check(the_triple):
    #Used to check the state of a list of squares (not necessarily three)
    hidden_ones = []
    flagged_ones = []
    open_ones = []
    for pt3 in the_triple:
        if 0 <= pt3[0] < 16 and 0 <= pt3[1] < 30:
            if click_map[pt3[0]][pt3[1]] == 0:
                hidden_ones.append([pt3[0], pt3[1]])
            elif click_map[pt3[0]][pt3[1]] == 1:
                open_ones.append([pt3[0], pt3[1]])
            elif click_map[pt3[0]][pt3[1]] == 2:
                flagged_ones.append([pt3[0], pt3[1]])
    return hidden_ones, flagged_ones, open_ones

def square_breakdown(ax, ay):
    #Breakdown of a square's 8 neighbours' state
    open, hidden, flagged = [], [], []
    for (x, y) in ((ax+1, ay), (ax-1, ay), (ax, ay+1), (ax, ay-1), (ax+1, ay+1), (ax+1, ay-1), (ax-1, ay+1), (ax-1, ay-1)):
        if 0 <= x < 16 and 0 <= y < 30:
            if click_map[x][y] == 0:
                hidden.append([x, y])
            elif click_map[x][y] == 1 and numbers[x][y] != 0:
                open.append([x, y])
            elif click_map[x][y] == 2:
                flagged.append([x, y])

    return open, hidden, flagged

def one_two_one(ax, ay, flagged, mines_num, steps, auto_mines):
    #To recognize 1-2-1 and 1-2-2-1 situations

    if numbers[ax][ay] - len(flagged) == 2:                                                                        #Main is a net-flagged 2
        if 1 <= ax <= 14:                                                          
            if click_map[ax-1][ay] == 1 and click_map[ax+1][ay] == 1:                                              #Vertical 1-2-1
                if numbers[ax-1][ay] - len(square_breakdown(ax-1, ay)[2]) == 1 and numbers[ax+1][ay] - len(square_breakdown(ax+1, ay)[2]) == 1:
                    if len(triple_check([[ax-1, ay-1], [ax, ay-1], [ax+1, ay-1]])[0]) == 3:
                        if len(triple_check([[ax-1, ay+1], [ax, ay+1], [ax+1, ay+1]])[0]) == 0 or ay == 29:        #Left is hidden, right is open
                            auto_open([[ax, ay-1]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax-1, ay-1], [ax+1, ay-1]], auto_mines, auto = False)
                            steps[1] += 1
                    elif len(triple_check([[ax-1, ay+1], [ax, ay+1], [ax+1, ay+1]])[0]) == 3:
                        if len(triple_check([[ax-1, ay-1], [ax, ay-1], [ax+1, ay-1]])[0]) == 0 or ay == 0:         #Right is hidden, left is open
                            auto_open([[ax, ay+1]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax-1, ay+1], [ax+1, ay+1]], auto_mines, auto = False)
                            steps[1] += 1

        if 1 <= ay <= 28:                                                          
            if click_map[ax][ay-1] == 1 and click_map[ax][ay+1] == 1:                                              #Horizontal 1-2-1
                if numbers[ax][ay-1] - len(square_breakdown(ax, ay-1)[2]) == 1 and numbers[ax][ay+1] - len(square_breakdown(ax, ay+1)[2]) == 1:
                    if len(triple_check([[ax+1, ay-1], [ax+1, ay], [ax+1, ay+1]])[0]) == 3:
                        if len(triple_check([[ax-1, ay-1], [ax-1, ay], [ax-1, ay+1]])[0]) == 0 or ax == 0:         #Lower is hidden, upper is open
                            auto_open([[ax+1, ay]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax+1, ay-1], [ax+1, ay+1]], auto_mines, auto = False)
                            steps[1] += 1
                    elif len(triple_check([[ax-1, ay-1], [ax-1, ay], [ax-1, ay+1]])[0]) == 3:
                        if len(triple_check([[ax+1, ay-1], [ax+1, ay], [ax+1, ay+1]])[0]) == 0 or ax == 15:        #Upper is hidden, lower is open
                            auto_open([[ax-1, ay]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax-1, ay-1], [ax-1, ay+1]], auto_mines, auto = False)
                            steps[1] += 1
        #1-2-2-1
        if steps[1] == 0:
            if 2 <= ax <= 14: #12-2-1 
                if click_map[ax-2][ay] == click_map[ax-1][ay] == click_map[ax+1][ay] == 1 and numbers[ax-2][ay] - len(square_breakdown(ax-2, ay)[2]) == 1 and numbers[ax-1][ay] - len(square_breakdown(ax-1, ay)[2]) == 2 and numbers[ax+1][ay] - len(square_breakdown(ax+1, ay)[2]) == 1:
                    if len(triple_check([[ax-2, ay-1], [ax-1, ay-1], [ax, ay-1], [ax+1, ay-1]])[0]) > 0:
                        if ay == 29 or len(triple_check([[ax-2, ay+1], [ax-1, ay+1], [ax, ay+1], [ax+1, ay+1]])[0]) == 0:                #Vertical 1221 with low mid 2 hidden on the left
                            auto_open([[ax-2, ay-1], [ax+1, ay-1]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax-1, ay-1], [ax, ay-1]], auto_mines, auto = False)
                            steps[2] += 1
                    elif len(triple_check([[ax-2, ay+1], [ax-1, ay+1], [ax, ay+1], [ax+1, ay+1]])[0]) > 0:
                        if ay == 0 or len(triple_check([[ax-2, ay-1], [ax-1, ay-1], [ax, ay-1], [ax+1, ay-1]])[0]) == 0:                 #Vertical 1221 with low mid 2 hidden on the right
                            auto_open([[ax-2, ay+1], [ax+1, ay+1]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax-1, ay+1], [ax, ay+1]], auto_mines, auto = False)
                            steps[2] += 1
            if steps[2] == 0 and 1 <= ax <= 13:  #1-2-21
                if click_map[ax-1][ay] == click_map[ax+1][ay] == click_map[ax+2][ay] == 1 and numbers[ax-1][ay] - len(square_breakdown(ax-1, ay)[2]) == 1 and numbers[ax+1][ay] - len(square_breakdown(ax+1, ay)[2]) == 2 and numbers[ax+2][ay] - len(square_breakdown(ax+2, ay)[2]) == 1:
                    if len(triple_check([[ax-1, ay-1], [ax, ay-1], [ax+1, ay-1], [ax+2, ay-1]])[0]) > 0:
                        if ay == 29 or len(triple_check([[ax-1, ay+1], [ax, ay+1], [ax+1, ay+1], [ax+2, ay+1]])[0]) == 0:                #Vertical 1221 with high mid 2 hidden on the left
                            auto_open([[ax-1, ay-1], [ax+2, ay-1]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax, ay-1], [ax+1, ay-1]], auto_mines, auto = False)
                            steps[2] += 1
                    elif len(triple_check([[ax-1, ay+1], [ax, ay+1], [ax+1, ay+1], [ax+2, ay+1]])[0]) > 0:
                        if ay == 0 or len(triple_check([[ax-1, ay-1], [ax, ay-1], [ax+1, ay-1], [ax+2, ay-1]])[0]) == 0:                 #Vertical 1221 with high mid 2 hidden on the right
                            auto_open([[ax-1, ay+1], [ax+2, ay+1]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax, ay+1], [ax+1, ay+1]], auto_mines, auto = False)
                            steps[2] += 1
            if steps[2] == 0 and 1 <= ay <= 27: #Horizontal 1-2-21
                if click_map[ax][ay-1] == click_map[ax][ay+1] == click_map[ax][ay+2] == 1 and numbers[ax][ay-1] - len(square_breakdown(ax, ay-1)[2]) == 1 and numbers[ax][ay+1] - len(square_breakdown(ax, ay+1)[2]) == 2 and numbers[ax][ay+2] - len(square_breakdown(ax, ay+2)[2]) == 1: 
                    if len(triple_check([[ax-1, ay-1], [ax-1, ay], [ax-1, ay+1], [ax-1, ay+2]])[0]) > 0:
                        if ax == 15 or len(triple_check([[ax+1, ay-1], [ax+1, ay], [ax+1, ay+1], [ax+1, ay+2]])[0]) == 0:                #Horizontal 1221 with left mid 2 hidden on the top
                            auto_open([[ax-1, ay-1], [ax-1, ay+2]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax-1, ay], [ax-1, ay+1]], auto_mines, auto = False)
                            steps[2] += 1
                    elif ax == 0 or len(triple_check([[ax+1, ay-1], [ax+1, ay], [ax+1, ay+1], [ax+1, ay+2]])[0]) == 0:
                        if ax == 0 or len(triple_check([[ax-1, ay-1], [ax-1, ay], [ax-1, ay+1], [ax-1, ay+2]])[0]) == 0:                 #Horizontal 1221 with left mid 2 hidden on the bottom
                            auto_open([[ax+1, ay-1], [ax+1, ay+2]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax+1, ay], [ax+1, ay+1]], auto_mines, auto = False)
                            steps[2] += 1
            if steps[2] == 0 and 2 <= ay <= 28: #Horizontal 12-2-1
                if click_map[ax][ay-2] == click_map[ax][ay-1] == click_map[ax][ay+1] == 1 and numbers[ax][ay-2] - len(square_breakdown(ax, ay-2)[2]) == 1 and numbers[ax][ay-1] - len(square_breakdown(ax, ay-1)[2]) == 2 and numbers[ax][ay+1] - len(square_breakdown(ax, ay+1)[2]) == 1: 
                    if len(triple_check([[ax-1, ay-2], [ax-1, ay-1], [ax-1, ay], [ax-1, ay+1]])[0]) > 0:
                        if ax == 15 or len(triple_check([[ax+1, ay-2], [ax+1, ay-1], [ax+1, ay], [ax+1, ay+1]])[0]) == 0:                #Horizontal 1221 with right mid 2 hidden on the top
                            auto_open([[ax-1, ay-2], [ax-1, ay+1]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax-1, ay-1], [ax-1, ay]], auto_mines, auto = False)
                            steps[2] += 1
                    elif len(triple_check([[ax+1, ay-2], [ax+1, ay-1], [ax+1, ay], [ax+1, ay+1]])[0]) > 0:
                        if ax == 0 or len(triple_check([[ax-1, ay-2], [ax-1, ay-1], [ax-1, ay], [ax-1, ay+1]])[0]) == 0:                 #Horizontal 1221 with right mid 2 hidden on the bottom
                            auto_open([[ax+1, ay-2], [ax+1, ay+1]], auto = True)
                            mines_num, auto_mines = auto_flag(mines_num, [[ax+1, ay-1], [ax+1, ay]], auto_mines, auto = False)
                            steps[2] += 1
    
    return mines_num, steps

def pattern_detection(pair, mines_num, open, hidden, flagged, possible, full_sequence, auto_mines):

    #The "Main" square being examined
    ax, ay = pair[0], pair[1]
    #Neighbours of the "main" square
    nbs = [[ax-1, ay], [ax+1, ay], [ax, ay-1], [ax, ay+1]]
    #The corresponding triple of squares on the other side of the "main" opposite from the neighbours
    oside = [[[ax+1, ay-1], [ax+1, ay], [ax+1, ay+1]], [[ax-1, ay-1], [ax-1, ay], [ax-1, ay+1]], [[ax-1, ay+1], [ax, ay+1], [ax+1, ay+1]], [[ax-1, ay-1], [ax, ay-1], [ax+1, ay-1]]]
    #The triple of squares of the neighbour square away from the "main" square
    nb_oside = [[[ax-2, ay-1], [ax-2, ay], [ax-2, ay+1]], [[ax+2, ay-1], [ax+2, ay], [ax+2, ay+1]], [[ax-1, ay-2], [ax, ay-2], [ax+1, ay-2]], [[ax-1, ay+2], [ax, ay+2], [ax+1, ay+2]]]

    steps = [0,0,0]

    for i in range(4):
        if nbs[i] in open and numbers[nbs[i][0]][nbs[i][1]] > 0:
            nb_flagged = square_breakdown(nbs[i][0], nbs[i][1])[2]                                               #Flagged list of the neighbours
            diff = (numbers[ax][ay] - len(flagged)) - (numbers[nbs[i][0]][nbs[i][1]] - len(nb_flagged))          #Main minus neighbour's "net flag" numbers, with respective flagged ones considered
            oside_hidden = triple_check(oside[i])[0]                                                             #Hidden ones of the triple that are next to the main but away from the neighbour

            if diff > 0:                                                                                         #If the main's net flag number is greater than a neighbour
                if len(oside_hidden) == diff:                                                                    #And the other side has the same number of hidden squares
                    mines_num, auto_mines = auto_flag(mines_num, oside_hidden, auto_mines, auto = False)   ##
                    steps[0] += 1
                    possible.remove(pair)
                    full_sequence.append([2]+oside_hidden)
                    break
            else:                                                                                                #If the main has no greater number of net flags than a neighbour
                nb_oside_hidden = triple_check(nb_oside[i])[0]                                                   #Hidden ones of the far side triple of the neighbour
                if len(nb_oside_hidden) == 0 and len(oside_hidden) > 0:                                          #If the neighbour's net flag number is positive and its own far side is all open 
                    auto_open(oside_hidden, possible, full_sequence, auto = True)                          ##        
                    steps[0] += 1

                    full_sequence.append([1]+oside_hidden)

                    for new_sq in oside_hidden:
                        adding_results = square_breakdown(new_sq[0], new_sq[1])
                        if len(adding_results[0]) > 0 and len(adding_results[1]) > 0 and numbers[new_sq[0]][new_sq[1]] != 0:
                            if len(adding_results[2]) + len(adding_results[0]) < 8:
                                possible.append(new_sq)
                    break

    #if sum(steps) == 0:
    #    mines_num, steps = one_two_one(ax, ay, flagged, mines_num, steps)                                        #1-2-1 and 1-2-2-1 patterns

    return mines_num, possible, full_sequence, auto_mines

def bigred_number(num, top, left):
    #Display the two red clocks on top
    three_d = [num//100, (num - (num//100*100))//10, num%10]

    for d in range(3):
        for i in range(15):
            d_row, d_col = i%5, i//5
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

        #"Normal" random mine distribution
        if special_start == False:
            rand_row = random.randint(0, 15)
            rand_col = random.randint(0, 29)
        
        #"Special" start
        else:
            doable = False
            while not doable:
                rand_row = random.randint(0, 15)
                rand_col = random.randint(0, 29)
                if abs(rand_row-start_pos[0]) + abs(rand_col-start_pos[1]) > 3:                   #Creating a mine-free "hole" in the area around the given point
                    doable = True                                                                 #So the first click can be always lucky

        if mines[rand_row][rand_col] == 0:
            mines[rand_row][rand_col] = 1

    return mines

def determine_numbers(mines):
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
    #Recognizing which square mouse the hovering over
    cur_x = (pygame.mouse.get_pos()[0] - 20)//58
    cur_y = (pygame.mouse.get_pos()[1] - 124)//58
    pygame.draw.rect(screen, (162, 162, 152), pygame.Rect(20+cur_x*58, 124+cur_y*58, 56, 56))
    pygame.draw.rect(screen, (218, 218, 208), pygame.Rect(20+cur_x*58, 124+cur_y*58, 54, 54))

def drawing_number(number, sqx, sqy, auto = False):
    #Square graphics
    pygame.draw.rect(screen, SQUARECOLOUR, pygame.Rect(20+sqx*58, 124+sqy*58, 56, 56))

    idx = 0
    if auto: idx = 1

    if number == 1:
        pygame.draw.rect(screen, C1[idx], pygame.Rect(20+17+sqx*58, 124+15+sqy*58, 17, 8))
        pygame.draw.rect(screen, C1[idx], pygame.Rect(20+26+sqx*58, 124+9+sqy*58, 8, 30))
        pygame.draw.rect(screen, C1[idx], pygame.Rect(20+23+sqx*58, 124+21+sqy*58, 3, 17))
        pygame.draw.rect(screen, C1[idx], pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))

    if number == 2:
        pygame.draw.rect(screen, C2[idx], pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C2[idx], pygame.Rect(20+35+sqx*58, 124+16+sqy*58, 8, 8))
        pygame.draw.rect(screen, C2[idx], pygame.Rect(20+13+sqx*58, 124+23+sqy*58, 30, 8))
        pygame.draw.rect(screen, C2[idx], pygame.Rect(20+13+sqx*58, 124+31+sqy*58, 8, 8))
        pygame.draw.rect(screen, C2[idx], pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))

    if number == 3:
        pygame.draw.rect(screen, C3[idx], pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C3[idx], pygame.Rect(20+35+sqx*58, 124+16+sqy*58, 8, 22))
        pygame.draw.rect(screen, C3[idx], pygame.Rect(20+19+sqx*58, 124+23+sqy*58, 24, 8))
        pygame.draw.rect(screen, C3[idx], pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))

    if number == 4:
        pygame.draw.rect(screen, C4[idx], pygame.Rect(20+32+sqx*58, 124+9+sqy*58, 10, 37))
        pygame.draw.rect(screen, C4[idx], pygame.Rect(20+14+sqx*58, 124+23+sqy*58, 28, 8))
        pygame.draw.rect(screen, C4[idx], pygame.Rect(20+18+sqx*58, 124+9+sqy*58, 8, 16))

    if number == 5:
        pygame.draw.rect(screen, C5[idx], pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C5[idx], pygame.Rect(20+13+sqx*58, 124+16+sqy*58, 8, 8))
        pygame.draw.rect(screen, C5[idx], pygame.Rect(20+13+sqx*58, 124+23+sqy*58, 30, 8))
        pygame.draw.rect(screen, C5[idx], pygame.Rect(20+35+sqx*58, 124+31+sqy*58, 8, 8))
        pygame.draw.rect(screen, C5[idx], pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))

    if number == 6:
        pygame.draw.rect(screen, C6[idx], pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C6[idx], pygame.Rect(20+13+sqx*58, 124+16+sqy*58, 8, 22))
        pygame.draw.rect(screen, C6[idx], pygame.Rect(20+13+sqx*58, 124+23+sqy*58, 30, 8))
        pygame.draw.rect(screen, C6[idx], pygame.Rect(20+35+sqx*58, 124+31+sqy*58, 8, 8))
        pygame.draw.rect(screen, C6[idx], pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))
    
    if number == 7:
        pygame.draw.rect(screen, C7[idx], pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C7[idx], pygame.Rect(20+35+sqx*58, 124+16+sqy*58, 8, 30))
    
    if number == 8:
        pygame.draw.rect(screen, C8[idx], pygame.Rect(20+13+sqx*58, 124+9+sqy*58, 30, 8))
        pygame.draw.rect(screen, C8[idx], pygame.Rect(20+13+sqx*58, 124+16+sqy*58, 8, 22))
        pygame.draw.rect(screen, C8[idx], pygame.Rect(20+13+sqx*58, 124+23+sqy*58, 30, 8))
        pygame.draw.rect(screen, C8[idx], pygame.Rect(20+35+sqx*58, 124+16+sqy*58, 8, 22))
        pygame.draw.rect(screen, C8[idx], pygame.Rect(20+13+sqx*58, 124+38+sqy*58, 30, 8))

    if number == "M":
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+15+sqx*58, 124+15+sqy*58, 26, 26))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+11+sqx*58, 124+19+sqy*58, 34, 18))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+19+sqx*58, 124+11+sqy*58, 18, 34))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+26+sqx*58, 124+7+sqy*58, 4, 42))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+7+sqx*58, 124+26+sqy*58, 42, 4))
        pygame.draw.rect(screen, BOARD, pygame.Rect(20+22+sqx*58, 124+18+sqy*58, 4, 4))

    #Testing purpose
    if number == "F2":
        pygame.draw.rect(screen, (162, 162, 152), pygame.Rect(20+sqx*58, 124+sqy*58, 56, 56))
        pygame.draw.rect(screen, COVEREDSQCOLOUR, pygame.Rect(20+sqx*58, 124+sqy*58, 54, 54))
        pygame.draw.rect(screen, C1[idx], pygame.Rect(20+10+sqx*58, 124+15+sqy*58, 6, 6))
        pygame.draw.rect(screen, C1[idx], pygame.Rect(20+16+sqx*58, 124+12+sqy*58, 12, 12))
        pygame.draw.rect(screen, C1[idx], pygame.Rect(20+22+sqx*58, 124+8+sqy*58, 12, 22))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+28+sqx*58, 124+30+sqy*58, 6, 6))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+18+sqx*58, 124+36+sqy*58, 20, 6))
        pygame.draw.rect(screen, BLACK, pygame.Rect(20+13+sqx*58, 124+40+sqy*58, 30, 8))

    if number == "F":
        pygame.draw.rect(screen, (162, 162, 152), pygame.Rect(20+sqx*58, 124+sqy*58, 56, 56))
        pygame.draw.rect(screen, COVEREDSQCOLOUR, pygame.Rect(20+sqx*58, 124+sqy*58, 54, 54))
        pygame.draw.rect(screen, FLAG[idx], pygame.Rect(20+10+sqx*58, 124+15+sqy*58, 6, 6))
        pygame.draw.rect(screen, FLAG[idx], pygame.Rect(20+16+sqx*58, 124+12+sqy*58, 12, 12))
        pygame.draw.rect(screen, FLAG[idx], pygame.Rect(20+22+sqx*58, 124+8+sqy*58, 12, 22))
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

def sort_list(possible, cur_pt):
    possible.sort(key = lambda p: abs(p[0] - cur_pt[0]) + abs(p[1] - cur_pt[1]))
    return possible

def show_squares(sqx, sqy, possible, full_sequence, special_start = False):
    #When opening up an empty square

    display_area = [[sqx, sqy]]
    all_neighbours = []

    #Find all connecting empty squares
    found_sth = True
    while found_sth:

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
            if special_start == False:
                drawing_number(numbers[i4[0]][i4[1]], i4[1], i4[0])

            if special_start:
                this_sq = square_breakdown(i4[0], i4[1])
                if len(this_sq[0]) > 0 and len(this_sq[1]) > 0:
                    possible.append([i4[0], i4[1]])

    full_sequence.append([1]+display_area)

    #Display the wrongly flagged non mines if lost
    if game_failed == True:
        for ir2 in range(16):
            for ic2 in range(30):
                if numbers[ir2][ic2] == 0 and click_map[ir2][ic2] == 2:
                    drawing_number("X", ic2, ir2)
    
    if special_start:
        for rep1 in full_sequence[-1][1:]:
            if numbers[rep1[0]][rep1[1]] != 0 and rep1 not in possible:
                possible.append(rep1)

        return possible, full_sequence

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
                        show_squares(xx, yy, possible, full_sequence)

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

def display_sequence(full_sequence, mines_num):
    
    current_time = 0
    while len(full_sequence) > 0:

        clock_speed = 300
        clock.tick(clock_speed)
        current_time += 1

        if current_time%10 == 0:
            latest_entry = full_sequence.pop(0)
            if latest_entry[0] == 1:
                for pt1 in latest_entry[1:]:
                    drawing_number(numbers[pt1[0]][pt1[1]], pt1[1], pt1[0], True)
                    pygame.display.update()
            else:
                for pt1 in latest_entry[1:]:
                    drawing_number("F", pt1[1], pt1[0], True)
                    mines_num -= 1
                    bigred_number(mines_num, 10, 10)
                    pygame.display.update()
        
        if current_time%clock_speed == 0:
            bigred_number(current_time//clock_speed, 10, 1626-104)
            pygame.draw.rect(screen, BACKGROUND, pygame.Rect(1544+152+3, 82+4-2, 44, 8))        #Cover up the blinking dots
            pygame.draw.rect(screen, ROBOT_EYE_ON, pygame.Rect(1552+152, 46-8+8-2, 12, 8))      #Robot eyes darker
            pygame.draw.rect(screen, ROBOT_EYE_ON, pygame.Rect(1574+152, 46-8+8-2, 12, 8))      #Robot eyes darker
            pygame.display.update()
        if current_time%clock_speed == clock_speed//2:
            pygame.draw.rect(screen, DARK_YELLOW, pygame.Rect(1552+152, 46-8+8-2, 12, 8))       #Robot eyes shine
            pygame.draw.rect(screen, DARK_YELLOW, pygame.Rect(1574+152, 46-8+8-2, 12, 8))       #Robot eyes shine
            pygame.display.update()    
        elif current_time%clock_speed == clock_speed//5:                                        #Four blinking dots below
            pygame.draw.rect(screen, C1[1], pygame.Rect(1544+152+3, 82+4-2, 8, 8))
            pygame.display.update()
        elif current_time%clock_speed == (clock_speed//5) * 2:
            pygame.draw.rect(screen, C2[1], pygame.Rect(1544+152+3, 82+4-2, 8, 8))
            pygame.draw.rect(screen, C2[1], pygame.Rect(1544+152+3+12, 82+4-2, 8, 8))
            pygame.display.update()
        elif current_time%clock_speed == (clock_speed//5) * 3:
            pygame.draw.rect(screen, C3[1], pygame.Rect(1544+152+3, 82+4-2, 8, 8))
            pygame.draw.rect(screen, C3[1], pygame.Rect(1544+152+3+12, 82+4-2, 8, 8))
            pygame.draw.rect(screen, C3[1], pygame.Rect(1544+152+3+24, 82+4-2, 8, 8)) 
            pygame.display.update()
        elif current_time%clock_speed == (clock_speed//5) * 4:
            pygame.draw.rect(screen, C4[1], pygame.Rect(1544+152+3, 82+4-2, 8, 8))
            pygame.draw.rect(screen, C4[1], pygame.Rect(1544+152+3+12, 82+4-2, 8, 8))
            pygame.draw.rect(screen, C4[1], pygame.Rect(1544+152+3+24, 82+4-2, 8, 8)) 
            pygame.draw.rect(screen, C4[1], pygame.Rect(1544+152+3+36, 82+4-2, 8, 8))
            pygame.display.update()

    return mines_num

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

ROBOT_OFF = (168, 176, 146)
ROBOT_OFF = (82, 82, 100)
ROBOT_ON = (136, 192, 186)
ROBOT_EYE_WHITE = (212, 216, 212)
ROBOT_EYE_OFF = (52, 46, 66)
ROBOT_EYE_ON = (68, 72, 92)

YELLOW = (236, 212, 82)
DARK_YELLOW = (218, 156, 52)

# C1 LIGHT
C1 = [(50, 112, 172), (80, 146, 150)]
C2 = [(76, 128, 68), (36, 108, 106)]
C3 = [(200, 22, 28), (16, 102, 152)]
C4 = [(0, 62, 116), (18, 80, 122)]
C5 = [(126, 68, 58), (6, 66, 112)]
C6 = [(80, 146, 150), (0, 52, 96)]
C7 = [(56, 56, 52), (0, 32, 56)]
C8 = [(132, 132, 128), (18, 38, 78)]
FLAG = [(200, 22, 28), (0, 112, 116)]

#Background and game area
pygame.draw.rect(screen, BACKGROUND, pygame.Rect(0, 0, 1778, 1070))
pygame.draw.rect(screen, BOARD, pygame.Rect(10, 114, 1758, 946))
#Two red clocks 
pygame.draw.rect(screen, BLACK, pygame.Rect(10, 10, 142, 94)) 
pygame.draw.rect(screen, BLACK, pygame.Rect(1626-104, 10, 142, 94))  

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
bigred_number(0, 10, 1626-104)
click_pair = []
flagged_sq = []
opened_sq = 0
auto_solve = False
auto_hover_pair = [-1, -1]
lucky_mode = False
special_start = True
start_pos = [7, 14]
possible = []
full_sequence = []
auto_mines = 0

#Initial setup
draw_new_board()
mines = new_board(mines)
numbers = determine_numbers(mines)

click_map = [[0] * 30 for _ in range(16)]

mouse_down = False

while True:
    if auto_solve:
        if game_won == False and game_failed == False:
            if game_on == False:
                game_on = True
                possible, full_sequence = [], []
                open_results = show_squares(start_pos[0], start_pos[1], possible, full_sequence, True)
                possible, full_sequence = open_results[0], open_results[1]
                possible = sort_list(possible, start_pos)
            else:
                if auto_mines > 0:
                    for asq in possible:
                        check_result = open_check(asq)
                        neighbour_num, open_list, hidden_list, flagged_list = check_result[0], check_result[1], check_result[2], check_result[3]

                        if len(hidden_list)+len(flagged_list) == numbers[asq[0]][asq[1]] and hidden_list:
                            mines_num, auto_mines = auto_flag(mines_num, hidden_list, auto_mines, auto = False)
                            full_sequence.append([2]+hidden_list)
                            possible.remove(asq)

                    for asq in possible:
                        check_result = open_check(asq)
                        neighbour_num, open_list, hidden_list, flagged_list = check_result[0], check_result[1], check_result[2], check_result[3]

                        if len(flagged_list) == numbers[asq[0]][asq[1]] and len(hidden_list) > 0:
                            auto_open(hidden_list, possible, full_sequence, True)
                            full_sequence.append([1]+hidden_list)
                            for new_sq in hidden_list:
                                adding_results = square_breakdown(new_sq[0], new_sq[1])
                                if len(adding_results[0]) > 0 and len(adding_results[1]) > 0 and numbers[new_sq[0]][new_sq[1]] != 0:
                                    if len(adding_results[2]) + len(adding_results[0]) < 8:
                                        possible.append(new_sq)

                    for repair in possible:
                        repair_update = square_breakdown(repair[0], repair[1])
                        if len(repair_update[1]) == 0:
                            possible.remove(repair)

                    for asq in possible:
                        results = square_breakdown(asq[0], asq[1])
                        open, hidden, flagged = results[0], results[1], results[2]
                        if open and hidden:
                            mines_num, possible, full_sequence, auto_mines = pattern_detection(asq, mines_num, open, hidden, flagged, possible, full_sequence, auto_mines)

                    unopened_nums = []

                    for ix in range(16):
                        for iy in range(30):
                            if click_map[ix][iy] == 0:
                                if numbers[ix][iy] != 9:
                                    unopened_nums.append([ix, iy])
                                    if len(unopened_nums) >= 50:
                                        break

                    if unopened_nums != []:
                        to_open = unopened_nums[-1]

                        auto_open([to_open], possible, full_sequence, True)
                        full_sequence.append([1]+[to_open])

                        adding_results = square_breakdown(to_open[0], to_open[1])
                        if len(adding_results[0]) > 0 and len(adding_results[1]) > 0 and numbers[to_open[0]][to_open[1]] != 0:
                            if len(adding_results[2]) + len(adding_results[0]) < 8:
                                possible.append(to_open)
                    
                else:
                    mines_num = display_sequence(full_sequence, mines_num) 
                    game_won = True
                    game_on = False

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
            auto_mines = 99

            bigred_number(0, 10, 1626-104)
            draw_new_board()
            mines = new_board(mines)
            numbers = determine_numbers(mines) #, numbers
            reset_clickmap()
            flagged_sq = []

        #Clicking Auto-Solve
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and event.button != 3 and 1626 <= pygame.mouse.get_pos()[0] <= 1762 and 10 <= pygame.mouse.get_pos()[1] <= 98:
            if auto_solve:
                auto_solve = False
            else:
                auto_solve = True
                lucky_mode = True
                auto_mines = mines_num * 1

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
                                show_squares(sqx, sqy, possible, full_sequence, False)
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

                                    bigred_number(0, 10, 1626-104)

                                    game_won, game_failed, game_on = False, False, True
                                    time_elapsed = 0
                                    mines_num = 99

                                    draw_new_board()
                                    mines = new_board(mines)
                                    numbers = determine_numbers(mines) #, numbers
                                    reset_clickmap()
                                    flagged_sq = []

                                    if numbers[sqx][sqy] == 0:
                                        show_squares(sqx, sqy, possible)
                                    else:
                                        drawing_number(numbers[sqx][sqy], sqy, sqx)
                                        click_map[sqx][sqy] = 1
                            ########

                            else:
                                for ir2 in range(16):
                                    for ic2 in range(30):
                                        #Show all mines
                                        if numbers[ir2][ic2] == 9:
                                            if click_map[ir2][ic2] == 0: ### Added so that when hit a mine (and ending the game) the other correctly flagged ones don't change
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
                for x2 in numbers:
                    print(x2)

    bigred_number(mines_num, 10, 10)

    smiley_hover()
    auto_solver_hover()

    pygame.display.update()

    #Game clock
    if game_on == True:
        time_elapsed += 1/30
        bigred_number(int(time_elapsed), 10, 1626-104)

        #Time's up
        if time_elapsed > 999:
            game_failed = True
            game_on = False

    clock.tick(30)

'''
### Mouseover auto solve code - placed in the main loop
if auto_solve:
    if game_won == False and game_failed == False and 20 <= pygame.mouse.get_pos()[0] <= 1758 and 124 <= pygame.mouse.get_pos()[1] <= 1050:

        sqy = (pygame.mouse.get_pos()[0] - 20)//58
        sqx = (pygame.mouse.get_pos()[1] - 124)//58
        cur_pair = [sqx, sqy]
        
        if auto_hover_pair != cur_pair and click_map[sqx][sqy] == 1 and numbers[sqx][sqy] != 0:
            
            auto_hover_pair[0], auto_hover_pair[1] = cur_pair[0], cur_pair[1]

            check_result = open_check(auto_hover_pair)
            neighbour_num, open_list, hidden_list, flagged_list = check_result[0], check_result[1], check_result[2], check_result[3]

            if len(hidden_list)+len(flagged_list) == numbers[sqx][sqy] and hidden_list:
                mines_num = auto_flag(mines_num, hidden_list, auto_mines, auto = True)

                if mines_num == 0:
                    exception_num = 0

                    for ch1 in flagged_sq:
                        if numbers[ch1[0]][ch1[1]] != 9:
                            exception_num += 1
                    #All flagged squares are indeed mines
                    if exception_num == 0:
                        game_won = True
                        game_on = False
            
            if len(flagged_list) == numbers[sqx][sqy] and len(hidden_list) > 0:
                auto_open(hidden_list, auto = True)
            
            ax, ay = auto_hover_pair[0], auto_hover_pair[1]
            results = square_breakdown(ax, ay)
            open, hidden, flagged = results[0], results[1], results[2]
            if open and hidden:
                mines_num = pattern_detection(auto_hover_pair, mines_num, open, hidden, flagged)

### Incomplete concept - when a human player encounters a must guess situation, whichever square clicked will always be a good click
def lucky_move(unopened_mines, unopened_nums, possible, full_sequence, auto_lucky):

    to_open = []

    for u_mine in unopened_mines:
        for u_num in unopened_nums:

            test_mines = ([0]+mines)[1:]
            test_mines[u_mine[0]][u_mine[1]] = 0
            test_mines[u_num[0]][u_num[1]] = 1
            test_output = determine_numbers(test_mines)

            they_match = True

            for rowx in range(16):
                for rowy in range(30):
                    if [rowx, rowy] not in unopened_mines and [rowx, rowy] not in unopened_nums:
                        if test_output[rowx][rowy] != numbers[rowx][rowy]:
                            they_match = False
                            break
            
            if they_match:
                pass
                break

    rand_sq = unopened[0]
    if numbers[rand_sq[0]][rand_sq[1]] == 9:        
        not_working = True

        while not_working:
            test_mines = [[0] * 30 for _ in range(16)]
            for a in range(16):
                for b in range(30):
                    if mines[a][b] == 1:
                        test_mines[a][b] = 1

        starting_pt = 1
        for replace_sq in unopened[starting_pt:]:
            if mines[replace_sq[0]][replace_sq[1]] == 0:
                test_mines[rand_sq[0]][rand_sq[1]] = 0
                test_mines[replace_sq[0]][replace_sq[1]] = 1

                test_output = determine_numbers(test_mines)

                they_match = True

                for rowx in range(16):
                    for rowy in range(30):
                        if [rowx, rowy] not in unopened:
                            if test_output[rowx][rowy] != numbers[rowx][rowy]:
                                they_match = False
                                break
                
                if they_match:
                    mines[rand_sq[0]][rand_sq[1]] = 0
                    test_mines[replace_sq[0]][replace_sq[1]] = 1
                    numbers[rand_sq[0]][rand_sq[1]] = neighbours(rand_sq[0], rand_sq[1], mines)
                    numbers[replace_sq[0]][replace_sq[1]] = 9

                    not_working = False
                else:
                    starting_pt = unopened.index(replace_sq) + 1

    auto_open([rand_sq], possible, full_sequence, False)

        #print(mines)

    return possible, full_sequence

    ### Main loop part
    # 
    ####Human click logic - if wrong click, make it right
                    
    unopened_mines, unopened_nums = [], []

    for ix in range(16):
        for iy in range(30):
            if click_map[ix][iy] == 0:
                if numbers[ix][iy] == 9:
                    unopened_mines.append([ix, iy])
                else:
                    unopened_nums.append([ix, iy])
    
    possible, full_sequence = lucky_move(unopened_mines, unopened_nums, possible, full_sequence, auto_lucky = True)


'''

